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
