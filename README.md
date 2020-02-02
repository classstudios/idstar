# ID-Star or Animal 图像识别明星或动物
using python identifying stars or animals

**Python应用百度AI做图像识别1.0**


*1、准备工作：安装百度AI为python开发的API SDK模块：baidu-aip模块*


在系统的命令控制行下使用  
#pip install baidu-aip 命令在线安装
    

*2、准备工作：建立工作环境*


以”regstar”在桌面建立一个文件夹，并以”regstar1.0”为名建python脚本放在该文件夹内。
#调用百度AI的API包
#from aip import AipImageClassify


*3、加入百度AI注册信息*
登陆并注册百度AI： http://ai.baidu.com/?track=cp:aipinzhuan|pf:pc|pp:AIpingtai|pu:title|ci:|kw:10005792
获得百度AI的APPID和APIKey，在脚本中定义一个百度AI图像识别功能的SDK函数对象，如下：


APP_ID = 'your app id'
API_KEY = 'your app key'
SECRET_KEY = 'your secret key'
百度图像识别 = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)



*4、之后我们要定义如何读取文件的方法*
#定义一个读取本地图片文件的函数
def get_file_content(图片路径): 
    with open(图片路径, 'rb') as fp:
        return fp.read()

5、#找到路径需要解析图片的路径和文件名
图片路径 = "文件夹名\\1.jpg"  #如果脚本和图片在同一级目录不用加\\“和前面的内容”

6、#使用百度图像识别中的动物识别分析该图
result=百度图像识别.animalDetect(get_file_content(图片路径))

百度AI图像识别参考文档：https://ai.baidu.com/docs#/ImageClassify-Python-SDK/top
Python应用百度AI做图像识别2.0的探索——返回值如何处理

修改文件名，分析数据发现：
 
得到的内容很繁多，我们真正需要的是？ 

为何会有多个结果？ Score是什么意思？猜一猜

返回的result是什么数据类型？ 

什么是字典？ http://www.runoob.com/python/python-dictionary.html

键值对key : value
字典： d = {key1 : value1, key2 : value2 }

我们现在想要访问字典内特定的值：

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
 print （"dict['Name']: ", dict['Name']）
以上实例输出结果：
dict['Name']:  Zara

有了上面的例子你有想法了吧。

result[?]
好像还是不对


那咋办？
Result[?][?]

Python应用百度AI做图像识别3.0的基本步骤 应用-----自动化

我要批量化识别路径下所有的图片，我该咋办？ 

循环？ 怎么用？ 如何写？ for 还是 while ?
提示：for  i  ….
       Str(i)+ …..



Python应用百度AI做图像识别4.0的基本步骤 应用-----图片处理

光识别不行，我要把记录保留下来最好在图片上有显示。

加个水印吧。怎么弄？
自学：https://www.cnblogs.com/tk091/p/4331327.html
注意需要安装哪个包？ 试一试
