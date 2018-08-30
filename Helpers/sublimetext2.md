### 安装package controll

***
  - View-控制台输入下面的命令---最好翻墙

     ```
     import urllib2,os,hashlib; h = '7183a2d3e96f11eeadd761d777e62404' + 'e330c659d4bb41d3bdf022e94cab3cd0'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); os.makedirs( ipp ) if not os.path.exists(ipp) else None; urllib2.install_opener( urllib2.build_opener( urllib2.ProxyHandler()) ); by = urllib2.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); open( os.path.join( ipp, pf), 'wb' ).write(by) if dh == h else None; print('Error validating download (got %s instead of %s), please try manual install' % (dh, h) if dh != h else 'Please restart Sublime Text to finish installation')
     ```
  - prefrence->package controll->install package

    - emmet 代码补全
    - theme-itg.flt  主题包
    - git  git版本控制包
    - SidebarEnhancements 侧边栏(打开，查找，复制和粘贴，等等)
    - GitGutter  这是一个小巧有用的插件,它会告诉你自上次git commit以来已经改变的行。一个指示器显示在行号的旁边。
    - Colorpicker  使用一个取色器改变颜色
    - Alignment 代码对齐(Ctrl+ Alt + A)
    - MoveBySymbols 跳转标记 (Ctrl + R)
    - File Switching 文件切换 (Ctrl + P)
    - 函数跳转 http://xlbd.me/1528/
    - svn   TortoiseSVN  
    
  - editToRight 分屏/ alt+shit+1恢复
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    