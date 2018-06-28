> ### 合理的均分方法可以固定小数位，比如100元平均分成N份(保留2为小数)并计算尾差

  - http://php.net/manual/zh/ref.bc.php
    http://php.net/manual/zh/ref.gmp.php
```php
<?php
header('Content-Type: text/plain; charset=utf-8');
function tail($num, $fen) {
    $avg  = bcdiv($num, $fen, 2); //除
    $tail = bcsub($num, $avg*($fen-1), 2); //减
    echo $num.'='.str_repeat($avg.'+', $fen-1).$tail."\n";
    echo "$num=$avg*($fen-1)+$tail\n";
    return array($avg, $tail);
}
var_export(tail(100, 3));
var_export(tail(100, 6));
/*输出:
100=33.33+33.33+33.34
100=33.33*(3-1)+33.34
array (
  0 => '33.33',
  1 => '33.34',
)
100=16.66+16.66+16.66+16.66+16.66+16.70
100=16.66*(6-1)+16.70
array (
  0 => '16.66',     
  1 => '16.70',
)
bcdiv和bcsub都是PHP自带的bcmath扩展函数,类似还有GMP:
*/
```