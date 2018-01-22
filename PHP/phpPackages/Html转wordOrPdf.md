### Linux下wkhtmltopdf的使用(html转pdf)

  - 下载链接wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
  - xz -d wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
  - tar -xvf wkhtmltox-0.12.4_linux-generic-amd64.tar
  - cp wkhtmltox/bin/wkhtmltopdf /usr/bin
  - wkhtmltopdf https://www.baidu.com test.pdf
  
  - 如有需要需要改成php执行时的用户和用户组
     - echo shell_exec("id -a"); 查看用户组和用户
     - chown root:root wkhtmltopdf
     
### html转word

  ```php
  <?php
  ob_start();
  echo '<html xmlns:o="urn:schemas-microsoft-com:office:office"  xmlns:w="urn:schemas-microsoft-com:office:word"  xmlns="http://www.w3.org/TR/REC-html40">
                     <head>
                          <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
                          <xml><w:WordDocument><w:View>Print</w:View></xml>
                   </head>';
  
  echo $html; //主体部分
  
  Header("Cache-Control: public");
  Header("Content-type: application/octet-stream");
  Header("Accept-Ranges: bytes");
  Header('Content-Disposition: attachment; filename=' . $wordname);
  Header("Pragma:no-cache");
  Header("Expires:0");
  ob_end_flush();
  exit;
  
 
  ```
### wkhtmltopdf生成pdf
  ```php
  <?php
  
  $wkhtmltopdf_exec_url = "wkhtmltopdf";
  $html = 'http://'.$_SERVER['HTTP_HOST'] . '/Admin_apkCheck/generateHtml.html?id=' . $info['id'];
  $path =  './public/images/admin/apk_pdf/' . date('Ym', time()) . '/';
  if (!is_dir($path)) {
      mkdir($path, 0777, true);
  }

  $path = $path . "APP安全检测报告-". $info['name'] . $info['version'] .".pdf";
  $pdf_name = $_SERVER['DOCUMENT_ROOT'] . substr($path, 1);

  try {
      $pdf_name = iconv('UTF-8', 'GB2312', $pdf_name); //中文文件名和目不会被命令识别，也不会被file_exists识别，需要转码
      shell_exec("$wkhtmltopdf_exec_url  --zoom 0.75 $html  $pdf_name");

      if (!file_exists($pdf_name)) {
          $this->message($code = -1, 'pdf文件生成失败');
      }
  } catch (\Exception $e) {
      $this->message($code = 1, $e->getMessage());
  }
  return $path;

  ```
### 读取pdf文件
  ```php
  <?php
  
  try {
      $file_name = $this->fillIntoPdf($info);

      $arr = explode('/', $file_name);

      header('Content-type: application/pdf');
      header('Content-Disposition: attachment; filename="'.array_pop($arr).'"');
      readfile($file_name);
      exit;
  } catch (\Exception $e) {
      $this->message($code = -1, '下载失败');
  }

  ```