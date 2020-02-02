# 图像识别明星或动物
using python identifying stars or animals

## Python应用百度AI图像识别1.0

****1、准备工作：安装百度AI为python开发的API SDK模块****

在系统命令控制行下使用命令在线安装
```
pip install baidu-aip 
```

****2、准备工作：建立工作环境****

以"regstar"在桌面建立一个文件夹，并以"regstar1.0"为名建python脚本放在该文件夹内。用IDLE编辑该脚本：
```python
from aip import AipImageClassify #调用百度AI的API包
```

****3、加入百度AI注册信息****


登陆并注册百度AI：[百度AI传送门](http://ai.baidu.com/?track=cp:aipinzhuan%7Cpf:pc%7Cpp:AIpingtai%7Cpu:title%7Cci:%7Ckw:10005792)
在注册获得百度AI的APPID和APIKey后
在脚本中定义一个百度AI图像识别功能的SDK函数对象：

```python
APP_ID = 'your app id'
API_KEY = 'your app key'
SECRET_KEY = 'your secret key'
百度图像识别 = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
```

****4、之后我们要定义如何读取文件的方法****


```python
def get_file_content(图片路径):   #定义一个读取本地图片文件的函数
    with open(图片路径, 'rb') as fp:
        return fp.read()
```

****5、找到路径需要解析图片的路径和文件名****

```python
图片路径 = "文件夹名\\1.jpg"  #如果脚本和图片在同一级目录不用加\\“和前面的内容”
```

****6、使用百度图像识别中的动物识别分析该图****

```python
result=百度图像识别.animalDetect(get_file_content(图片路径))
```

> 百度AI图像识别参考文档：https://ai.baidu.com/docs#/ImageClassify-Python-SDK/top
