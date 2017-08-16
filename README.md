本程序采用Phantomjs + Selenium" 这个python，来实现计算所自动联网程序。

只是简单实现了功能，水平有限，还望见谅。

接下来，介绍如运行程序：

login.py 是登录的主程序，主要实现读取user.conf用户信息文件，
然后采用Phantomjs+Selenium，建立一个无GUI的浏览器，实现模拟点击登录操作。

以上需要安装python2.7，最新的Selenium包，并且下载对应操作系统的PhamtomJS程序到根目录下面。

ps： 所里登录验证方式改了，采用了两步认证，以及两级加密的方式，直接用之前版本实现的方式，困难比较大。

接下来，介绍如何py2exe。
运行setup.py, 就会在当前目录下面生成dist文件夹，然后在dist里面找到library.zip, 
将js文件夹下面的两个js文件拷贝到library.zip里面的selenium/webdriver/remote 下面。
运行login.exe程序，就可以实现自动联网，目前实现的是每个一个小时自动联网一次。


其他更加方面的功能，由于时间关系还没有实现

ubuntu 简单安装方式：
1) sudo apt-get install python-pip
2) sudo pip install selenium
3) sudo apt-get install phantomjs
亲测可行
