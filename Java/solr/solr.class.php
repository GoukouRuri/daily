<?php
/**
 * Created by PhpStorm.
 * User: GoukouRuri
 * Date: 2017/12/21
 * Time: 16:01
 */
namespace Org\Solr;
require_once( APP_PATH.'../../SolrPhpClient/Apache/Solr/Service.php'); // 具体路径请自行修改
/**
 * Solr 工具类
 * 提供一系列的Solr搜索引擎操作方法
 * @author    GoukouRuri <lovenico2016@gmail.com>
 */
class Solr {
    const SOLR_HOST = 'localhost';
    const SOLR_PORT = '8983';
    const SOLR_URL  = '/solr/core_test/';

    /**
     * php通过solr文件包连接服务器端
     */
    public static function solr_server(){
        $solrSearcher = new \Apache_Solr_Service( self::SOLR_HOST, self::SOLR_PORT, self::SOLR_URL );
        if ( !$solrSearcher->ping() ) {
            echo 'Solr service not responding.';
            exit;
        }
        return $solrSearcher;
    }

    /**
     * php通过solr扩展连接服务器端
     */
    public static function extention_solr_server()
    {
        $extention_solrconfig = array('hostname' => self::SOLR_HOST,'port'=>self::SOLR_PORT);
        try {
            $solrSearcher = new \SolrClient($extention_solrconfig);
            $solrSearcher->ping();
        } catch (\Exception $e) {
            echo "Solr extention service connect fail.";
            exit;
        }
        return $solrSearcher;
    }

    /**
     * php文件包方式查询方法
     */
    public static function solr_query($options = array(), $pageinfo = array('offset' => 0, 'limit' => 20), $params = array('sort' => 'id asc', 'fl' => '', 'fq' => array()))
    {
        $solrSearcher = self::solr_server();
        if (empty($options)) return false;
        $q = '*:*'; // 默认q查询字段时默认取全部, 有条件取并集缩小范围
        // *:* AND (name:*S* OR name:(A* L*))
        // keyword 等值查询
        if (isset($options['keyword'])) {
            $q = $q.' AND (keyword='.trim($options['keyword']);
        } else {
            $q = $q.' AND (keyword=null';
        }
        // q单字段查询
        if (isset($options['name'])) {
            if (is_array($options['name'])) {
                // 多个值
                array_walk($options['name'], function(&$v, $k) {
                    $v = '*'.$v.'*';
                });
                $tmp = "name:(" . implode(" ", $options['name']) .")";
            } else {
                $tmp = 'name:*'.trim($options['name']).'*';
            }
            $q .= ' OR '. $tmp;
        }
        $q .= ')';

        //$params['fl'] = $params['fl'] ? $params['fl'] : "*";
        $response = $solrSearcher->search( $q, $pageinfo['offset'], $pageinfo['limit'], $params);

        $result = array();
        $found_num = 0;
        $http_status=$response->getHttpStatus();

        if ( $http_status == 200 ) {
            $response_result = $response->response;
            $found_num = $response_result->numFound;

            if ( $found_num > 0 ) {
                $search_docs = $response_result->docs;
                //$highlighting = $response->highlighting;
                foreach ($search_docs as $s_k=>$s_v){
                    $lists = get_object_vars($s_v->getIterator());
                    //使用高亮
                    //$lists['goods_color_name'] = empty($highlighting->$lists['goods_id']->goods_name[0]) ? $lists['goods_name'] : $highlighting->$lists['goods_id']->goods_name[0];
                    $result['lists'][] = $lists;
                }
            }
            // 此处可以自定义一些返回的key和value
            $result['total'] = $found_num;
        }
        else {
            echo $response->getHttpStatusMessage();
        }

        return $result;
    }

}