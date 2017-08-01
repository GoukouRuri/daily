[TOC]

## 常用类型
  string字符串、有序集合
## 概述
  Redis绝大多数的应用场景为：数据缓存服务器。与memcached的角色保持一致。
  但实质上, redis是一个：缓存数据库服务器
  在提供缓存的基础上，同时提供数据持久化（复制）等数据层面的功能。
  实现机制： 操作时，操作的内存，允许设置同步到磁盘上。

### Key-Value NoSQL
  数据模型是基于Key-Value

### 多数据类型的支持
  相比memcached的类型会多一些
  字符串、位图、链表、集合、有序集合、HyperLog(基数统计)
  结果就是操作变得繁琐。针对于每种类型，提供各种各样的命令完成操作。

### memcached pk redis
  功能： memcached单一，redis全面一些
  稳定性：memcached经典一些，redis更新潮一些
  速度：无结论

## 安装Redis
  make

  mkdir /usr/local/redis
  mkdir /usr/local/redis/bin
  mkdir /usr/local/redis/etc

  cp src/redis-server src/redis-cli src/redis-benchmark src/redis-sentinel /usr/local/redis/bin

  cp redisl.conf /usr/local/redis/etc
## 管理redis
  bin/redis-server 通常需要指定其配置文件 //启动
  --help //帮助
  kill -9 进程ID //停止
  kill [-9] `cat /var/run/redis.pid`
  反引号 ` 为执行引号，会将引号内容以命令方式来执行

### 配置文件 /etc/redis.conf
![](leanote://file/getImage?fileId=57918569a83d1b680a000000)

  // 前台运行，建议改成 yes 表示以守护进程的方式运行
  daemonize no/yes

  // 配置日志
  logfile '/var/log/redis.log'

  // 日志级别
  loglevel debug/verbose/notice/warning

  // 数据库数量
  databases 16;
### redis客户端
  bin/redis-cli [-h 127.0.0.1] [-p 6370]

### 快速使用
  set: set name abcdefg
  get: get name

## 通用指令
### help 获得帮助信息
  help set //获得set指令的帮助信息
  help @string //获取某种类型的所有帮助信息
  help @generic //获取能用元素操作

### clear 清除显示
  清除显示
### quit 退出

### :set nohints //关闭提示
### :set hints //显示提示

## 缓存项操作，KEY的操作
### DEL key
  删除一个key和它所对应的值

### KEYS
  keyps pattern
  keys * //显示所有数据
  keys na* //显示所有以na开头的键

### RANDOMKEY 随机取得一个key
  随机取得一个key
  randomkey 返回的是key，不是值

### TTL time to live
  TTL key
  有效期检测，key还能活多久，单位（秒），-1表示不会过期

### PTTL
  pttl key
  以毫秒为单位返回key的剩余过期时间

### EXISTS
  exists key
  检查给定key是否存在

### MOVE key db
  move key db
  将当前数据库的key移动到给定数据库db当中

  如 move title 1 //将title 移动到1库中

### RENAME
  RENAME key newkey
  修改 key 的名称

### RENAMENX 改名时判断新key是否存在
  renamenx key newkey
  仅当newkey不存在时，将key改名为newkey

### TYPE
  type key
  获取key存储值的类型

### EXPIRE
  expire key seconds
  为给定的key设置有效期，以秒为单位

### PEXPIRE
  pexpire key milliseconds
  为给定的key设置有效期，以毫秒为单位

### EXPIREAT
  expireat key timestamp
  为key设置过期时间，参数是unix时间戳(unix timestamp)

### PEXPIREAT
  pexpireat key milliseconds-timestamp
  设置key过期时间的时间戳(timestamp)，以毫秒计

### PERSIST 永不失效
  persist key
  移除key的过期时间，key永远不生效

### SORT
  sort key
  sort key desc
  sort key alpha
  sort key aplha desc

  返回或保存给定列表、集合、有序集合key中经过排序的值

### DUMP
  dump key
  将key的数据进行额外编码，序列化，并返回序列化后的结果
  比较类似encode编码

## 数据库
  将key划分到不同的数据库进行管理
  数据库没有名字，也不支持操作。只是名称上的划分，类似命名空间。默认以0～15进行标号，共16个库。在redis.conf配置文件中可以对其进行配置：databases 16;

  切换不同的库： select 0/1/2/3....15
![](leanote://file/getImage?fileId=57918a38a83d1b680a000001)
  在实际开发中，很少会切换库，
  一般使用0库，以添加数据前缀的方式来区分数据

  库是可以将key进行分开管理的， 当前库不能访问到其它库的key。
  例如：0库下定义的name，不能在1库中访问
![](leanote://file/getImage?fileId=57918a83a83d1b680a000002)

## 数据类型的支持
  字符串string：还用说嘛...
  位图bitmap：bitarray, 可理解成由0或1组成的字符串: 0010101
  链表list：只允许在首尾进行操作的数据列表，想深入去看数据结构
  集合set：元素的无序列表，比较倾向于数组概念，唯一
  有序集合sorted-set：在集合的基础上，为每个元素加权（分值）。加权指的是增加一个属性，表示该元素的权重。
  哈希表hash：简单理解为关联数组，key-value的数据表
  HyperLogLog(基数统计)：统计基数而用。基数表示集合当中不重复的元素个数。类似于mysql中的count(distinct value)

### 编程界在定义函数（功能时）有两套文案
  方案一：函数少，参数多
  函数内部，判断大量的参数默认值，给定的状态，去执行对应的功能

  方案二：函数多，参数少
  需要通过大量的函数名区分各种功能

### [常用]字符串类型的操作
#### SET
  设置值
  set key value

#### GET
  获取指定key的值
  get key

#### SETNX
  setnx key value
  设置值，判断key是否存在，存在则设置成功，不存在则失败

  类似：
  if(isset(key)){
  return 0;
  } else {
  set(key,value);
  }

#### SETEX
  setex key seconds value
  设置指定key的值，同时设置过期时间，单位为秒

#### SETRANGE
  从索引位置进行替换
  setrange key offset value
  用value参数覆写给定key所存储的字符串值，从偏移量offset开始
![](leanote://file/getImage?fileId=57919489a83d1b680a000003)
  如：
  set str 0123456789
  setrange str 3 hello
  get str: 012hello89

#### MSET
  一次性设置多个key value
  MSET key1 value1 key2 value2 key3 value3 ...

#### MSETNX
  MSETNX key value [key value...]
  一次性设置多个key value，且<！全部key都不存在！>才可以设置成功

#### PSETEX
  psetex key milliseconds value
  设置指定key的指，同时设置过期时间，单位为毫秒

#### APPEND
  append key value
  如果 key 已经存在并且是一个字符串， APPEND 命令将 value 追加到 key 原来的值的末尾

#### DECR
  decr key
  将key中存储的数字值减一

#### DECRBY 递减给定数值
  decrby key number
  将key中存储的数值每次减去给定的量的值（number）

#### INCR 递增一
  INCR key
  将key中存储的数值递增一
#### INCRBY 递增指定数量
  INCRBY key number
  将key中存储的数值递增给定量的值（number）

#### INCRBYFLOAT 浮点数递增
  incrbyfloat key flot_increment
  将key所存储的值加上给定的浮点增量值（flot_increment）

  如：incrbyfloat key 4.4

#### GETSET 设置新值，返回旧值
  getset key value
  将给定的key的值设置为value，并返回key的旧值（old value）

#### GETRANGE
  getrange key start end
  返回key中字符串的子字符
  如：
  set title abcdefghijk
  getrange title 2 4
  结果：cde
#### STRLEN
  strlen key
  返回key所存储的字符串值的长度

#### MGET
  mget key1 key2 key3 ...
  同时获取多个key对应的值

### LIST 链表类型
  概述：
  连续的列表数据，类似于索引数组，下标从0-N。操作某个索引下标对应的元素，或操作首尾的元素。

#### LPUSH
  lpush key value [value ...]
  将值value插入到列表key的表头

  如： LPUSH stuList '张无忌'

#### LPUSHX
  lpushx key value
  将值value插入到列表key的表头，当且仅当key存在并且是一个列表
  即：key不存在或不是列表类型 就不能成功添加成功

#### RPUSH
  rpush key value[value...]
  将值value插入到列表key的表尾（末尾）

#### RPUSHX
  rpushx key value
  将值value插入到列表key的末尾，当且仅当key存在并且是一个列表
  即：key不存在或不是列表类型 就不能成功添加成功

#### LPOP
  lpop key
  移除并返回列表key的头元素

#### RPOP
  rpop key
  移除并返回列表key的尾元素

#### BLPOP
  blpop key [key...] timeout
  LPOP命令的阻塞版本，当给定列表内没有任何元素可供弹出的时候，

  连接将被BLPOP最多阻塞 timeout 时长，若有数据，则直接弹出
  从左边弹出数据

#### BRPOP
  brpop key [key...] timeout
  RPOP命令的阻塞版本，当给定列表内没有任何元素可供弹出的时候，

  连接将被BRPOP最多阻塞 timeout 时长，若有数据，则直接弹出
  从右边弹出数据

#### LLEN
  LLEN key
  返回列表key的长度

#### LRANGE
  lrange key start stop
  返回列表key中指定区间内的元素，区间以偏移量start和stop指定
  lrange title 0 100

#### LRANGEX

#### LREM 从左开始移除
  REM: remove
  LREM key count value
  根据参数count的值，移除列表中与参数value相等的元素

  count = 0 : 表示移除所有与value相匹配的元素
  count > 0 : 从表头开始向表尾搜索，
  移除与value相等的值，数量为count的绝对值
  count < 0 : 从表尾开始向表头搜索，
  移除与value相等的值，数量为count的绝对值

  如: lrem name 0 '张无忌' //移除表中全部的'张无忌'

#### LSET
  LSET key index value
  将列表key下标为index的元素的值设置为value

  如： LSET user 1 setme //将user中的下标索引为1的值改为setme

#### LTRIM
  LTRIM key start stop
  对一个列表进行修剪(trim)，就是说，让列表只保留指定区间内的元素，不在指定区间之内的元素都将被删除

  如：
  ltrim userlist 1 2 //索引位置小于1，大于2的元素被裁剪掉

#### LINDEX
LINDEX key index
返回列表key中，下标为index的元素
根据索引位置返回索引对应的元素的值

#### LINSERT 在某一个位置插入值
LINSERT key BEFORE|AFTER pivot value
将值value插入到列表key当中，位于值pivot之前或之后

  linsert users before HELLO kang //在HELLO前插入kang
  linsert users after setMe haha //在setMe之后插入haha

#### RPOPLPUSH
RPOPLPUSH source destination
将列表source中的最后一个元素(尾元素)弹出，并返回给客户端。
将source弹出的元素插入到列表destination，作为destination列表的的头元素

实验需要2个list
//将userList中的最后一个元素弹出，并插入到stuList的表头
rpoplpush userList stuList

#### BRPOPLPUSH
BRPOPLPUSH source destination timeout
BRPOPLPUSH是RPOPLPUSH的阻塞版本，当给定列表source不为空时，BRPOPLPUSH的表现和RPOPLPUSH一样。
当列表source为空时，BRPOPLPUSH命令将阻塞连接，直到等待超时，或有另一个客户端对source执行LPUSH或RPUSH命令为止。
超时参数timeout接受一个以秒为单位的数字作为值。
超时参数设为0表示阻塞时间可以无限期延长(block indefinitely)

### set集合操作
  set：不重复的元素的集合
![](leanote://file/getImage?fileId=5791e272a83d1b680a000006)

#### SADD
  SADD key member
将member元素加入到集合key当中

不能重复添加

#### SREM
SREM key member
移除集合中的member元素

#### SMEMBERS 返回集合中所有有素
SMEMBERS key
返回集合key中的所有成员

#### SISMEMBER
SISMEMBER key member
判断集合key中是否存在member成员

#### SCARD
SCARD key
返回集合key的基数(集合中元素的数量)

基数：元素个数的意思

#### SMOVE
SMOVE source destination member
将member元素从source集合移动到destination集合

#### SPOP 随机移除并返回一个元素
SPOP key
移除并返回集合中的一个随机元素

#### SRANDMEMBER
SRANDMEMBER key
返回集合中的一个随机元素

#### SINTER 返回多个集合的交集
SINTER key [key ...]
返回多个集合的交集（即各集合中相同的元素）

![交集](leanote://file/getImage?fileId=5791dfada83d1b680a000005)

#### SINTERSTORE
SINTERSTORE destination key [key ...]
返回交集，并保存到destination集合

#### SUNION
SUNION key [key ...]
返回多个集合的并集

#### SUNIONSTORE
SUNIONSTORE destination key [key ...]
返回并集，将结果保存到destination集合

#### SDIFF
SDIFF key [key ...]
计算差集

SDIFF groupA groupB //groupA - groupB 保留groupA中剩余的元素
SDIFF groupB groupA //groupB - groupA 保留groupB中剩余的元素

#### SDIFFSTORE
SDIFFSTORE destination key [key ...]
计算差集，将结果保存到destination

### [常用]sorted-set加权(有序)集合
  与集合相比，每个元素，多了一个额外的属性，称之为score（分/权）
![](leanote://file/getImage?fileId=5791e398a83d1b680a000008)

  在所有数据类型中相对来说用得比较多：销售排行榜、点击排行榜...

  集合内，按照sorte数排序存储，不是按照插入顺序（list就是add添加顺序），而可以按sorte来进行排序。
  人为指定score，按照定义的业务逻辑，存储数据！很适用 TOP N类程序！

#### ZADD 添加元素到有序集合
  ZADD key score member
将member元素及其score值加入到有序集key当中

#### ZREM
ZREM key member
移除有序集key中的成员member

#### ZCARD
ZCARD key
返回有序集key的基数（成员个数）

#### ZCOUNT
ZCOUNT key min max
返回有序集key中，score值在min和max之间(默认包括score值等于min或max)的成员

#### ZSCORE 返回指定成员的权值
ZSCORE key member
返回有序集key中，成员member的score值

#### ZINCRBY
ZINCRBY key increment member
为有序集key的成员member的score值加上增量increment

#### ZRANGE （从小到大 区域返回）
![](leanote://file/getImage?fileId=5791e64ca83d1b680a000009)
ZRANGE key start stop [WITHSCORES]
返回有序集key中，指定区间内的成员
成员的位置按score值递增(从小到大)来排序
下标0表示有序集第一个成员，1表示有序集第二个成员
-1表示最后一个成员，-2表示倒数第二个成员
WITHSCORES选项，来让成员和它的score值一并返回

#### ZREVRANGE （从大到小 区域返回）
ZREVRANGE key start stop [WITHSCORES]
返回有序集key中，指定区间内的成员
其中成员的位置按score值递减(从大到小)来排列
下标0表示有序集第一个成员，1表示有序集第二个成员
-1表示最后一个成员，-2表示倒数第二个成员
WITHSCORES选项，来让成员和它的score值一并返回

#### ZRANGEBYSCORE
ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]
返回有序集key中，所有score值介于min和max之间(包括等于min或max)的成员。有序集成员按score值递增(从小到大)次序排列
WITHSCORES参数决定结果集是单单返回有序集的成员，还是将有序集成员及其score值一起返回
的LIMIT参数指定返回结果的数量及区间
min和max可以是-inf和+inf，表示最低和最高score值
默认闭区间，参数前增加(符号来使用可选的开区间

如：
ZRANGEBYSCORE buyList 50 100 //取得分数：50～100之间的
ZRANGEBYSCORE buyList 50 100 withscores //同时携带分数
ZRANGEBYSCORE buyList 50 100 withscores limit 1 2 //跳过1条取2条

如果对分数需要执行 大于 或 小于 独立的逻辑而不是区间逻辑，
使用-inf 和 +inf表示 负无穷 和 正无穷

ZRANGEBYSCORE buyList 50 +inf //表示大于50的数据
ZRANGEBYSCORE buyList -inf 50 //表示小于50的数据

  也提供开区间，不包含边界值
ZRANGEBYSCORE buyList (70 +inf //表示大于70的数据,且不包含70

#### ZREVRANGEBYSCORE
ZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count]
返回有序集key中，score值介于max和min之间(默认包括等于max或min)的所有的成员。有序集成员按score值递减(从大到小)的次序排列
WITHSCORES参数决定结果集是单单返回有序集的成员，还是将有序集成员及其score值一起返回
的LIMIT参数指定返回结果的数量及区间
min和max可以是-inf和+inf，表示最低和最高score值
默认闭区间，参数前增加(符号来使用可选的开区间

#### ZRANK 取排名
ZRANK key member
返回有序集key中成员member的排名。其中有序集成员按score值递增(从小到大)顺序排列

#### ZREVRANK 取倒序排名
ZREVRANK key member
返回有序集key中成员member的排名。其中有序集成员按score值递减(从大到小)排序
区间分别以下标参数start和stop指出，包含start和stop
0表示有序集第一个成员，以1表示有序集第二个成员
-1表示最后一个成员，-2表示倒数第二个成员

#### ZREMRANGEBYRANK 根据排名移除成员
ZREMRANGEBYRANK key start stop
移除有序集key中，指定排名(rank)区间内的所有成员

#### ZREMRANGEBYSCORE
ZREMRANGEBYSCORE key min max
移除有序集key中，所有score值介于min和max之间(包括等于min或max)的成员
min和max可以是-inf和+inf，表示最低和最高score值
默认闭区间，参数前增加(符号来使用可选的开区间

#### ZINTERSTORE
ZINTERSTORE destination numkeys key [key ...] [WEIGHTS weight [weight ...]] [AGGREGATE SUM|MIN|MAX]
计算给定的一个或多个有序集的交集
numkeys参数表示给定key的数量
结果集中某个成员的score值是所有给定集下该成员score值的和

weight：表示分数的权重
  SUM|MIN|MAX ： max:取最大值、min：最小值、sum：默认求合

//将viewList和buyList的交集的结果存入viewIbuy
//2表示几个集合做交集运算
//结果分值会累加
ZINTERSTORE viewIbuy 2 viewList buyList

修改分数处理方式
ZINTERSTORE viewIbuy 2 viewList buyList weight 1 1 AGGREGATE max

![有几个集合就应该有几个权重](leanote://file/getImage?fileId=5791ef73a83d1b680a00000a)

#### ZUNIONSTORE
ZUNIONSTORE destination numkeys key [key ...] [WEIGHTS weight [weight ...]] [AGGREGATE SUM|MIN|MAX]
计算给定的一个或多个有序集的并集
numkeys参数表示给定key的数量
结果集中某个成员的score值是所有给定集下该成员score值的和
WEIGHTS选项，可以为每个给定有序集分别指定一个乘法因子，有序集的所有成员的score值在传递给聚合函数(aggregation function)之前都要先乘以该有序集的因子，几个有续集集合几个因子
AGGREGATE选项，你可以指定并集的结果集的聚合方式，默认使用的参数SUM，可以将所有集合中某个成员的score值之和作为结果集中该成员的score值；使用参数MIN，可以将所有集合中某个成员的最小score值作为结果集中该成员的score值；而参数MAX则是将所有集合中某个成员的最大score值作为结果集中该成员的score值

### hash表
  关联数组，键值对列表
  一个数据由一组key-value键值对构成
#### HSET
HSET key field value
将哈希表 key 中的字段 field 的值设为 value

#### HSETNX
HSETNX key field value
获取哈希表中所有值
  HSETNX key field value

#### HMSET
HMSET key field1 value1 [field2 value2 ]
同时将多个 field-value (域-值)对设置到哈希表 key 中

#### HMGET
HMGET key field1 [field2]
获取所有给定字段的值
  获取哈希表中所有值

#### HGET 获取hash表中的key的值
HGET key field
获取存储在哈希表中指定字段的值

#### HGETALL
HGETALL key
获取在哈希表中指定 key 的所有字段和值

#### HDEL
HDEL key field2 [field2]
删除一个或多个哈希表字段

#### HLEN 获取hash表里面字段数量
HLEN key
获取哈希表中字段的数量

#### HEXISTS 指定字段是否存在
HEXISTS key field
查看哈希表 key 中，指定的字段是否存在

#### HINCRBY 字段的值增加 或 减少
HINCRBY key field increment
为哈希表 key 中的指定字段的整数值加上增量 increment

  increment 正负数

#### HINCRBYFLOAT 字段的值增加,浮点数
HINCRBYFLOAT key field increment
为哈希表 key 中的指定字段的浮点数值加上增量 increment

#### HKEYS
HKEYS key
获取所有哈希表中的字段

#### HVALS
HVALS key
获取所有哈希表中的字段值

#### HSCAN
HSCAN key cursor [MATCH pattern] [COUNT count]
迭代哈希表中的键值对

### 位图(bitMap)，BitsArray，位数组，位的集合
  概述：由1或0组成的字符串。例如：11010110101010201001

#### SETBIT
SETBIT key offset value
对 key 所储存的字符串值，设置或清除指定偏移量上的位(bit)

  setbit weather 0 1 //设置第0位是1
  setbit weather 1 0 //设置第1位是0
  setbit weather 2 0 //设置第2位是0

#### GETBIT
GETBIT key offset
对 key 所储存的字符串值，获取指定偏移量上的位(bit)

getbit weather 0 //获取第0位
getbit weather 1 //获取第1位
getbit weather 2 //获取第2位

### HyperLogLog基数统计类型
  概述：
  基数统计，不记录数据，而仅仅记录不重复的数据个数（数据量）
  参考SCARD

#### PFADD
PFADD key element [element ...]
添加指定元素到 HyperLogLog 中

  PFADD stuLog kang
  pfadd stuLog hello
  pfadd stuLog world //重复不记数，取值的时候是得不到hello等字符串的
  pfadd stuLog kang //仅可以获得记录数量

#### PFCOUNT
PFCOUNT key [key ...]
返回给定 HyperLogLog 的基数估算值

#### PFMERGE
PFMERGE destkey sourcekey [sourcekey ...]
将多个 HyperLogLog 合并为一个 HyperLogLog

若出现重复的key，则仅统计1个
  PFADD stuLog kang
  PFADD userLog kang //重复
  PFADD userLog hello
  PFMERGE stuLog userLog //PFCOUNT stuLog只有2个

## 持久化
  当服务器重新启动时，会依据数据库文件，进行初始化redis中的redis的key-value数据。

  原理如下：
![](leanote://file/getImage?fileId=57942133eeb129794e000000)
  缓存数据库服务器：
  缓存：数据存储在内存
  数据库：数据存储在磁盘上

  执行指定时，都是自支因内存中增加数据。

### 持久化方式
#### 配置文件选项：
  dir /opt/database/redis //数据文件存放位置
  appendonly yes //是否开启aof方式的持久化文件

  redis支持同时开启： 增量（AOF）+ 快照方式

  save 60 10000 //数据备份算法,在60秒内,有10000个改动，则生成快照
  save 900 1 //数据备份算法,在900秒内,有1个改动，则生成快照

  如果将所有save注释，没有save配置，表示关闭数据快照（纯粹的内存缓存，可以选择关闭快照） 配合开启appenonly后，表示内存数据 + 增量备份

#### 支持：
  数据快照：每隔多久，将内存中的数据写入磁盘上。
  追回文件(AOF，append only file)：将数据的改动指令，记录下来，然后重复执行(增量备份)
  对应的文件如下：
  appendony.aof //aof方式的备份文件
  dump.rdb //数据快照方式生成的备份文件（处理大量数据时效率比较低）

#### 备份文件
  cp dump.rdb dump.rdb.20160708 //备份
  cp dump.rdb.20160708 dump.rdb //还原

#### 操作指令
  >save //立即存储快照
  >bgsave //后台立即存储快照
  >lastsave //获取最后的快照生成时间

## 事务 transaction
  ACID (原子性、一致性、隔离性、持久性)
  redis中的事务是简单事务，只实现了原子性，没有隔离性的概念
  redis，将所有待执行的命令，当作一个队列来处理。一次性全部执行！

  提供了watch 和 unwatch指令 进行一致和隔离的处理

### multi 开启事务
  开启执行多条命令！
  后续的执行的命令，就被排队，等待最终执行

### 执行常规命令
![](leanote://file/getImage?fileId=57942d5bd625be16d7000000)

### exec 提交执行
  事务队列中的命令，依次执行

### discard 回滚
  放弃队列中的命令，并退出事务

### watch 监视key
  用于检视某个key
  如果所监视的key，被其它客户端修改了，则当前事务直接放弃

### unwatch 放弃监视key
  放弃监视某个key

## 复制 Replication
### 主从复制
  支持一主多从的配置方式
![](leanote://file/getImage?fileId=579435fad625be16d7000002)

  用来解决：
  一、服务器压力 。利用负载均衡，可以做压力分摊，读写分享
  二、做即时备份冗余服务器

### 配置实现
  配置从服务器即可
  修改从服务器的配置文件：
  从服务器：
  slaveof masterIP masterPort

  主服务器：
  保持主服务器运行，并允许从服务器连接，注意绑定ip
  bind 127.0.0.1 192.168.0.111

## 使用
### 缓存
### 特定的数据结构：lists, sorted-set
  实操中：需要立即响应给客户端结果，同时在服务器端慢慢的处理业务逻辑
  如：
  生成订单的逻辑：
  购买高峰，同时迸发订单很多，由于订单要保证数据的完整性，业务逻辑完成得慢
  此时：
  用户点击生成订单时，立即响应给用户：订单生成成功，与此同时，将任务，加入到任务列表中（就可以使用redis的list结构实现，或者sorted-set(存在优先级)）

  后台独立程序，读取list或者sorted-set，将 里边的任务依次实现

### web程序的架构，双层数据库
  内存型数据库 -> 磁盘型数据库

## 支持密码认证
### 开启配置
  requirepass pwd123456 //连接时需要密码，密码为pwd123456

### 客户端提供验证
  > auth 密码

### 连接时提供密码
  redis-cli -a 密码
