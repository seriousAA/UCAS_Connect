### 校园网自动连接 仅限Linux

* * *

(windows端可以自行改一下我的脚本，反正代码就几行，很简单)

##### 使用说明

-   开机之后打开终端，如果没有安装selenium，直接
    
    ```shell
    pip install selenium
    ```
    
    安装selenium
    
-   将auto_connect.py下载下来，放到一个非root权限就可以访问到的地方
    
-   通过以下命令查看chrome版本，(如果没有chrome就去官网安装一个最新版的)

    ```shell    
    google-chrome -version或者chrome -version
    ```
    
    如下图所示
    
    ![查看谷歌浏览器版本](resources/chrome-version.png)
    
-   根据chrome浏览器版本，在[网址1](https://sites.google.com/chromium.org/driver/downloads) 或者[网址2](https://npm.taobao.org/mirrors/chromedriver/) 下载对应版本的ChromeDriver，和auto_connect.py放到同一目录下(不是必须，但最好这样)
    
    像我的Chrome版本如上个图片所示，是92版本的，所以我选择[92.0.4515.107](https://chromedriver.storage.googleapis.com/index.html?path=92.0.4515.107/) 这一版本的ChromeDriver
    
-   对脚本内容进行修改：
    
    -   账号
        
    -   密码
        
    -   ChromeDriver的绝对路径
        
    -   Log输出文件的绝对路径
        
    
    如下图所示：
    
    ![]()
    
-   脚本默认的是每60s检测一次网络连接情况，如果断连就会重新连接，可以在代码里设置检测间隔时间，如下图所示：
    
    ![]()
    
-   最后的操作，是将运行脚本的命令放入到Linux的开机自启动程序中，这样每次开机或者重启，脚本都会自动运行
    
    在/etc/目录下搜索找到rc.local文件，里面的内容应该是与下图类似：
    
    ![]()
    
    在rc.local文件中插入如下命令：
    ```shell 
    nohup python -u {脚本的绝对路径} > {Log输出文件的绝对路径} 2>&1 &
    ```
    
    为了保险起见，可以先在终端运行以下命令测试脚本功能是否正常，然后再修改rc.local文件
    
    ```shell 
    python -u {脚本的绝对路径} > {Log输出文件的绝对路径} 2>&1 &
    ```
    
-   修改完rc.local文件后，重启电脑即可生效。如果后续脚本功能没有达到预期效果，可以查看Log输出文件，查看脚本运行情况
