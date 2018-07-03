### Mysql5.7的使用注意事项

------



- **尽量不要使用对字段使用UNSIGNED。**因为可能会带来一些意想不到的效果 ，而且对于INT类型可能存放不了的数据，INT UNSIGNED同样可能存放不了，与其如此，还不如在数据库设计阶段将INT类型提升为BIGINT类型。 

  

- **尽量使用NOT NULL DEFAULT '' 而不要允许NULL。**因为空值是不占用空间的 ，而MySQL中的NULL其实是占用空间的并且不走索引，对于空值的判断到底是使用is null 还是 =''要根据实际业务来进行区别 

  

- **InnoDB表建议用自增列做主键。**写入顺序能和B+树索引的叶子节点顺序一致的，这时候存取效率是最高的 

  

- ***删除和清空表时候要小心，小心使用 drop 和 truncate*** 。尤其没有备份的时候.否则哭都来不及 使用上,想删除部分数据行用 delete，注意带上where子句. 回滚段要足够大. 想删除表,当然用 drop 想保留表而将所有数据删除，如果和事务无关，用truncate即可。如果和事务有关,或者想触发trigger,还是用delete。 如果是整理表内部的碎片，可以用truncate跟上reuse stroage，再重新导入/插入数据。 [参考资料](https://www.cnblogs.com/SaraMoring/p/5607537.html)

  

- **添加外键需要慎重**。考虑约束和级联两种模式在ON DELETE和ON UPDATE的区别，并且外键约束不能跨引擎使用。[参考资料](https://blog.csdn.net/dingding_12345/article/details/47905715)

  

- **日期时间尽量用datetime不要用timestamp，因为timestamp时间范围小**

  

- **插入时数据的值或字节数超过字段的设定时，在不严格会自动截断和取最大值，但是严格模式下会直接报错**`Data too long for column`

  

- **mysql中慎用BLOB和TEXT类型。**BLOB与TEXT是为了存储极大的字符串而设计的数据类型，采用二进制与字符串方式存储。在实际使用中应该慎用这两个类型，尤其是会创建临时表的情况下，因为如果临时表大小超过max_heap_table_size或者tmp_table_size，就会将临时表存储在磁盘上，进而导致整体速度下降！ 不要用它们来存音频和图片等信息，那些应该只需要存具体路径就行，可以用cnd加速，mysql不适合存大文件信息，无法进行性能优化。

  

- **ENGINE=InnoDB DEFAULT CHARSET=utf8 CHECKSUM=1 DELAY_KEY_WRITE=1 ROW_FORMAT=DYNAMIC 详解** 。[参考资料](https://blog.csdn.net/fdsfdf3434/article/details/78356234)

  

- **安全等于运算符**`<=>`**可以对NULL进行判断**

  