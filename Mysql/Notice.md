### Mysql5.7的使用小结

------



- **尽量不要使用对字段使用UNSIGNED**，因为可能会带来一些意想不到的效果 ，而且对于INT类型可能存放不了的数据，INT UNSIGNED同样可能存放不了，与其如此，还不如在数据库设计阶段将INT类型提升为BIGINT类型。 

  

- **尽量使用NOT NULL DEFAULT '' 而不要允许NULL**，因为空值是不占用空间的 ，而MySQL中的NULL其实是占用空间的并且不走索引，对于空值的判断到底是使用is null 还是 =''要根据实际业务来进行区别 

  

- **InnoDB表建议用自增列做主键**，写入顺序能和B+树索引的叶子节点顺序一致的，这时候存取效率是最高的 

  

-  ***删除和清空表时候要小心，小心使用 drop 和 truncate*** ，尤其没有备份的时候.否则哭都来不及 使用上,想删除部分数据行用 delete，注意带上where子句. 回滚段要足够大. 想删除表,当然用 drop 想保留表而将所有数据删除，如果和事务无关，用truncate即可。如果和事务有关,或者想触发trigger,还是用delete。 如果是整理表内部的碎片，可以用truncate跟上reuse stroage，再重新导入/插入数据。 

  - [参考资料](https://www.cnblogs.com/SaraMoring/p/5607537.html)

    

- 

