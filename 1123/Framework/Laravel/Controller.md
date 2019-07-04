### Request类

### session普通用法(还可以使用Session类)

  - session()->put('name', 'value');  // 添加单个
  - session(['name'=>'value']);   // 添加数组形式
  - session()->push('arr', 'item');   //向数组中添加
  - session()->push('arr.items', 'item');  //向多维数组中添加
  - session()->get('name');   // 获取单个
  - session()->forget('name');  // 删除单个
  - session()->flush();  // 清空所有
  - session()->pull('name'); //pull 算是“查方法”，但它获取到数据后，会马上删除这个session数据