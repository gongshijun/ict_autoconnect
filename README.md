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
3) sudo apt-get install phantomjs 亲测可行（这样安装phantomjs可能出现无法使用find_element类型的函数）

推荐使用如下方法安装phantomjs
apt install nodejs-legacy # just an alias node/nodejs to make npm install work
apt purge phantomjs       # optionaly
npm install -g phantomjs  # most important part because apt installation failed for me
（以上安装实现，于2018/6/12，在ubuntu 16.04 python2.7 下成功运行）

在ubuntu 16.04下，可能2）和3）中的selenium和phantomjs包无法正常安装，那么你需要按照下面几步手动安装，并修改login.py中的一个函数

+ 安装 selenium

https://pypi.python.org/pypi/selenium/

复制这个whl（selenium-3.6.0-py2.py3-none-any.whl (md5) 	Python Wheel 	2.7 	2017-09-25 	902K）的链接，然后用下面的命令安装就可以了

```
sudo pip install https://pypi.python.org/packages/48/90/29bcfa7ced2836016a400e8216e5a4166a71923b05d452ee7ee9e8775156/selenium-3.6.0-py2.py3-none-any.whl#md5=11022f864bf7075841486a0b30e173a8
```


+ 安装phantomjs

去[官网](http://phantomjs.org/download.html)下载可执行文件，现在把文件放到路径/usr/local/lib下，然后修改权限```sudo chmod -R 777 /usr/local/phantomjs-2.1.1-linux-x86_64/```,最后修改login.py，只需要修改一行即可，

```
#browser = webdriver.PhantomJS()
browser = webdriver.PhantomJS(executable_path='/usr/local/lib/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

```
<a href="https://info.flagcounter.com/Y4Mt"><img src="https://s11.flagcounter.com/count2/Y4Mt/bg_FFFFFF/txt_000000/border_CCCCCC/columns_2/maxflags_10/viewers_0/labels_0/pageviews_0/flags_0/percent_0/" alt="Flag Counter" border="0"></a>
