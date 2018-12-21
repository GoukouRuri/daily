### 常用的git命令

###### github库使用 ---（gitlab等也类似）
- 初始化一个库

  ``git init``
- ssh方式克隆github远程库 -- 需配置ssh key

  ```git clone git@github.com:GouKouRuri/cms.git```

- 如果是用https方式克隆的，如何转换成ssh呢

  ```git remote -v```   查看remote方式
  
  如果当前是https的，那么可以通过如下命令修改为ssh：
  
  ```git remote set-url origin git@github.com:GoukouRuri/cms.git```
- 配置用户名和邮箱 --- .git/config是git的配置文件

  ```git config --global user.name GoukouRuri```
  
  ```git config --global user.email lovenico2016@gmail.com```
  
- 配置push远程版本

  ```git config --global push.default simple```
  
- 添加远程分支
    
  
- github

  ###### …or create a new repository on the command line
  
  ```
  echo "# cms" >> README.md
  git init
  git add README.md
  git commit -m "first commit"
  git remote add origin https://github.com/GoukouRuri/cms.git
  git push -u origin master
  ```
  
  ###### …or push an existing repository from the command line
  
  ```
  git remote add origin https://github.com/GoukouRuri/cms.git
  git push -u origin master
  
  ```
  
  ###### 如果远程分支与本地分支没有关联
  ```
  git branch --set-upstream-to=origin/master  master
  git push origin master
  git pull origin master
  ```
  
  ###### 如何忽略.idea目录的提交
  ```
  .gitignore 添加.idea/
  git rm -r --cached .idea
  git commit -m "edit"
  git push
  ```
  



