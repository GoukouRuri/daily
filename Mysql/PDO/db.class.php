<?php
/**
 * A simple database class about pdo, you should use php>=5.4
 * @author       GoukouRuri(https://github.com/GoukouRuri)
 * @link         http://php.net/manual/zh/book.pdo.php
 * @example
 * <pre>
 * $array = [
 *   'dsn'   => 'mysql:dbname=dbtest;host=127.0.0.1:3306',
 *   'user'  => 'root',
 *   'pass'  => '123456',
 *   'driver'=> array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8")
 * ]
 * $pdo = new DB_pdo($array);
 * // 1. Read friendly method  
 * $db->bind("id","1");
 * $db->bind("firstname","John");
 * $person   =  $db->query("SELECT * FROM Persons WHERE firstname = :firstname AND id = :id");
 * // 2. Bind more parameters
 * $db->bindMore(array("firstname"=>"John","id"=>"1"));
 * $person   =  $db->query("SELECT * FROM Persons WHERE firstname = :firstname AND id = :id"));
 * // 3. Or just give the parameters to the method
 * $person   =  $db->query("SELECT * FROM Persons WHERE firstname = :firstname",array("firstname"=>"John","id"=>"1"));
 * </pre>
 */
class DB_pdo {
    protected $config;

    protected $pdo;

    protected $connect_status;

    protected $query;

    protected $parameters;

    protected $log;

    /**
     *  Default Constructor
     *
     *	1. Instantiate Log class.
     *	2. Connect to database.
     *	3. Creates the parameter array.
     */
    public function __construct(array $array)
    {
        try
        {
            $this->config = $array;
            $this->pdo = new PDO($array['dsn'], $array['user'], $array['pass'], $array['driver']);
            // 是否启动预处理语句的模拟/Disable emulation of prepared statements, use REAL prepared statements instead.
            $this->pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
            // 设置pdo的错误处理模式/We can now log any exceptions on Fatal error.
            $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            // 连接成功后标识状态/Connection succeeded, set the boolean to true.
            $this->connect_status = true;
        }
         catch (PDOException $e)
        {
            // Write into log
            echo $this->ExceptionLog($e->getMessage());
            exit();
        }


    }

    /**
     *  If the SQL query contains a SELECT or SHOW statement it returns an array containing all of the result set row
     *	If the SQL statement is a DELETE, INSERT, or UPDATE statement it returns the number of affected rows
     *
     *  @param  string $query
     *	@param  array  $params
     *	@param  int    $fetchmode
     *	@return mixed
     */
    public function query($query, $params = null, $fetchmode = PDO::FETCH_ASSOC)
    {
        $query = trim($query);
        $this->init($query,$params);
        $rawStatement = explode(" ", $query);

        # Which SQL statement is used
        $statement = strtolower($rawStatement[0]);

        if ($statement === 'select' || $statement === 'show') {
            return $this->query->fetchAll($fetchmode);
        }
        elseif ( $statement === 'insert' ||  $statement === 'update' || $statement === 'delete' ) {
            return $this->query->rowCount();
        }
        else {
            return NULL;
        }
    }

    /**
     *	Every method which needs to execute a SQL query uses this method.
     *
     *	1. If not connected, connect to the database.
     *	2. Prepare Query.
     *	3. Parameterize Query.
     *	4. Execute Query.
     *	5. On exception : Write Exception into the log + SQL query.
     *	6. Reset the Parameters.
     */
    private function init($query, $parameters = "")
    {
        // Connect to database
        if(!$this->connect_status) {
            self::__construct($this->config);
        }
        try {
            // Prepare query
            $this->query = $this->pdo->prepare($query);

            // Add parameters to the parameter array
            $this->bindMore($parameters);
            // Bind parameters
            if(!empty($this->parameters)) {
                foreach($this->parameters as $param)
                {
                    $parameters = explode("\x7F", $param);
                    $this->query->bindParam($parameters[0], $parameters[1]);
                }
            }
            // Execute SQL
            $this->success = $this->query->execute();
        }
        catch (PDOException $e)
        {
            // Write into log and display Exception
            $this->ExceptionLog($e->getMessage(), $query);
        }
        // Reset the parameters
        $this->parameters = array();
    }

    /**
     * Writes the log and returns the exception
     *
     * @param  string $message
     * @param  string $sql
     * @return string
     */
    private function ExceptionLog($message , $sql = "")
    {
        $exception  = 'You have some exceptions. <br />';
        $exception .= $message;
        $exception .= "<br /> You can find the error back in the log.";
        if(!empty($sql)) {
            // Add the Raw SQL to the Log
            $message .= "\r\nRaw SQL : "  . $sql;
        }
        // Write into log
        $this->log->write($message);

        //Return exception;
        throw new Exception($message);

    }

    /**
     *	Add the parameter to the parameter array
     *
     *	@param string $para
     *	@param string $value
     *  @return void
     */
    public function bind($para, $value)
    {
        $this->parameters[sizeof($this->parameters)] = ":" . $para . "\x7F" . utf8_encode($value);
    }

    /**
     * Add more parameters to the parameter array
     *
     * @param array $parray
     * @return void
     */
    public function bindMore($parray)
    {
        if(empty($this->parameters) && is_array($parray)) {
            $columns = array_keys($parray);
            foreach($columns as $i => &$column)	{
                $this->bind($column, $parray[$column]);
            }
        }
    }

    /**
     *  Returns the last inserted id.
     *  @return string
     */
    public function lastInsertId() {
        return $this->pdo->lastInsertId();
    }

    /**
     *	Returns an array which represents a column from the result set
     *
     *	@param  string $query
     *	@param  array  $params
     *	@return array
     */
    public function column($query, $params = null)
    {
        $this->init($query, $params);
        $Columns = $this->query->fetchAll(PDO::FETCH_NUM);

        $column = null;
        foreach($Columns as $cells) {
            $column[] = $cells[0];
        }
        return $column;

    }

    /**
     *	Returns an array which represents a row from the result set
     *
     *	@param  string $query
     *	@param  array  $params
     *  @param  int    $fetchmode
     *	@return array
     */
    public function row($query, $params = null, $fetchmode = PDO::FETCH_ASSOC)
    {
        $this->init($query, $params);
        return $this->query->fetch($fetchmode);
    }

    /**
     *	Returns the value of one single field/column
     *
     *	@param  string $query
     *	@param  array  $params
     *	@return string
     */
    public function single($query, $params = null)
    {
        $this->init($query, $params);
        return $this->query->fetchColumn();
    }

}