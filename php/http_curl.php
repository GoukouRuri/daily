<?php
// 网络通信,模拟请求数据接口

// 第一种 CURL 方式通信 (基于curl库)
class CurlServer {
	public $joinHash = false;
    protected static $instance;
    const API_HASH_KEY = "XCHKSAtyYDZTveXqi1I4BFf0xBviSain"

    /**
     * @return CurlServer
     */
    public static function init()
    {
        if (!self::$instance) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    /**
     * 发送远程api请求
     * @param  [type] $url  [description]
     * @param  array  $data [description]
     * @return [type]       [description]
     */
    public static function request($url, array $data, $type = "GET")
    {
		$self = self::init();

        $data['time'] = time();
        if ($self->joinHash) {
            $data['hash'] = $self->genHash($data);
        }
        
        if ($type == "GET") {
        	$res = $this->get($url, $data);
        } else {
        	$res = $this->post($url, $data);
        }
        
        if ($res && $resp = json_decode($res, true)) {
            return $resp;
        } else {
            return $res;
        }
    }

    public function get($url, array $data)
    {
    	$url = $url . '?' . http_build_query($data);  //http_build_query做一层过滤
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);  //这里可以省略直接写到curl_init初始化里
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_TIMEOUT, 60); 
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
        curl_setopt($ch, CURLOPT_HEADER, false)
        $res = curl_exec($ch);
        if (curl_errno($ch)) {
        	throw new \Exception(curl_error($ch));
        }
        curl_close($ch);
        return $res;
    }

    public static function post($url, array $data)
    {
    	$ch = curl_init(); 
        curl_setopt($ch, CURLOPT_URL, $url); 
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false); // 对认证证书来源的检查
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false); // 从证书中检查SSL加密算法是否存在
        curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']); // 模拟用户使用的浏览器
        curl_setopt($ch, CURLOPT_POST, true); 
        curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data)); // Post提交的数据包
        curl_setopt($ch, CURLOPT_TIMEOUT, 60); // 设置超时限制防止死循环
        curl_setopt($ch, CURLOPT_HEADER, false); // 显示返回的Header区域内容
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); // 获取的信息以文件流的形式返回
        $res = curl_exec($ch);
        if (curl_errno($ch)) {
        	throw new \Exception(curl_error($ch));
        }
        curl_close($curl); 
        return $res;
    }

    /**
     * 附带hash CurlServer::joinHash()->request()
     * @param bool $yes
     * @return CurlServer
     */
    public static function joinHash($yes = true)
    {
        self::instance()->joinHash = $yes;
        return self::instance();
    }

    /**
     * 生成hash串
     * @param  [type] $data [description]
     * @return [type]       [description]
     */
    public function genHash($data)
    {
        foreach ($data as $k => $v) {
            if ($v === null) {
                $data[$k] = '';
            }
        }
        ksort($data);
        $string = http_build_query($data) . self::API_HASH_KEY;
        return md5($string);
    }

    /**
     * [checkHash description]
     * @return [type] [description]
     */
    public function checkHash()
	{
		$data = $_REQUEST;
		$hash = trim($_REQUEST['hash']);
	    unset($data['hash']);
	    ksort($data);
	    $_hash = md5(http_build_query($data) . self::API_HASH_KEY);
	    return $_hash == $hash ? true : false;
	}
}