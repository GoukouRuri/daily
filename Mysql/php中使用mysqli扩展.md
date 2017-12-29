### 简单的db类(未对sql做过滤处理.)
```php
<?php
class DB_new {
    private $mysql_conn = '';
    public function __construct($array)
    {
        $mysql_conf = array(
            'host'    => $array['host'],
            'db'      => $array['db'],
            'db_user' => $array['db_user'],
            'db_pwd'  => $array['db_pwd'],
        );
        $this->mysql_conn = @mysqli_connect($mysql_conf['host'], $mysql_conf['db_user'], $mysql_conf['db_pwd']);
        if (!$this->mysql_conn) {
            exit("could not connect to the database");//诊断连接错误
        }
        mysqli_query($this->mysql_conn, "set character set 'utf8'");//读库
        mysqli_query($this->mysql_conn, "set names 'utf8'");//写库
        $select_db = mysqli_select_db($this->mysql_conn, $mysql_conf['db']);
        if (!$select_db) {
            exit("could not connect to the db");
        }
    }

    public function query($sql)
    {
        $res = mysqli_query($this->mysql_conn, $sql);

        if (!$res) {
            exit("could get the res:\n" . $sql);
        }
        $array = array();
        while ($row = mysqli_fetch_assoc($res)) {
            $array[] = $row;
        }
        mysqli_close($this->mysql_conn);
        return $array;
    }
}

```
