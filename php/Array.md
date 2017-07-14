> 常用的数组函数

- [array_chunk](http://php.net/manual/zh/function.array-chunk.php) 将一个数组分割成多个数组
- [array_column](http://php.net/manual/zh/function.array-column.php) 返回input数组中键值为column_key的列， 如果指定了可选参数index_key，那么input数组中的这一列的值将作为返回数组中对应值的键。
- [array_combine](http://php.net/manual/zh/function.array-combine.php) 创建一个数组，用一个数组的值作为其键名，另一个数组的值作为其值
- [array_count_values](http://php.net/manual/zh/function.array-count-values.php) 返回一个数组： 数组的键是 array 里单元的值； 数组的值是 array 单元的值出现的次数。
- [array_fill_keys](http://php.net/manual/zh/function.array-fill-keys.php) 使用 value 参数的值作为值，使用 keys 数组的值作为键来填充一个数组。
- [array_fill](http://php.net/manual/zh/function.array-fill.php) 用 value 参数的值将一个数组填充 num 个条目，键名由 start_index 参数指定的开始。






***

> 不常用的数组函数

- array_change_key_case 将数组中的所有键名修改为全大写或小写

***

- array_diff_assoc 返回一个数组，该数组包括了所有在 array1 中但是不在任何其它参数数组中的值。注意和 array_diff() 不同的是键名也用于比较。
- array_diff_key 根据 array1 中的键名和 array2 进行比较，返回不同键名的项。 本函数和 array_diff() 相同只除了比较是根据键名而不是值来进行的。
- array_diff_uassoc 对比了 array1 和 array2 并返回不同之处。 注意和 array_diff() 不同的是键名也用于比较。和 array_diff_assoc() 不同的是使用了用户自定义的回调函数，而不是内置的函数。
- array_diff_ukey 返回一个数组，该数组包括了所有出现在 array1 中但是未出现在任何其它参数数组中的键名的值。注意关联关系保留不变。本函数和 array_diff() 相同只除了比较是根据键名而不是值来进行的。
- array_diff 对比 array1 和其他一个或者多个数字，返回在 array1 中但是不在其他 array 里的值。

***










