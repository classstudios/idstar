

from aip import AipImageClassify #加载百度识别库

import os


import PIL #加载pillow处理图片库
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


import re #加载网络爬虫库
import requests

word = input("输入你想下载图片大类（10张）: ")
url ="https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="+word #需要通过网络爬虫请求的链接
headers = {'user-agent': '"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'} 
 
html = requests.get(url,headers).text  #头文件标识了，我使用某种浏览器来访问，避免被防爬虫机制屏蔽
pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
pic_url=pic_url[0:11]  #所有链接数组中的前10项
i =1
pathn="待识别图片/"
try:                     #
    os.makedirs(pathn)   #相对路径，在脚本所在目录下创建 待识别图片文件目录
except Exception as e:   #异常处理，打印出错原因，打印事件

      print(e)  

for each in pic_url:
    print(each)
    try:
        pic= requests.get(each, timeout=10)
    except requests.exceptions.ConnectionError:
        print( '【错误】当前图片无法下载')
        continue
    string =pathn+"/"+word+str(i) + '.jpg'
    fp = open(string,'wb')
    fp.write(pic.content)
    fp.close()
    i+=1


font = ImageFont.truetype("C:\Windows\Fonts\msyhbd.ttc", 50)#设置所使用的字体

APP_ID = '15836728'
API_KEY = 'KE9KUEv8eVnFl4QURxGte5Pg'
SECRET_KEY = 'DBeRG73N9oNUQsqYC4U6dH8HbDcyV2jZ'
百度识图 = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
options = {}  
options["baike_num"] = 1

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

for i,filename in enumerate(os.listdir("./待识别图片")):  #遍历该目录下所有的图片
  if filename.endswith('.jpg'):

          图片路径="待识别图片//"+str(filename)
          #print(图片路径)
          try:
                result=百度识图.advancedGeneral(get_file_content(图片路径))
                resultbaike=百度识图.advancedGeneral(get_file_content(图片路径),options)#百度百科介绍
                des=resultbaike["result"][0]["baike_info"]['description']
                name=result['result'][0]['keyword']
                kind=result['result'][0]['root']
                  
                #print(name)

                im1 = Image.open(图片路径)

                path="识别结果/"+kind

                #创建目录，注意如何处理异常
                try:
                    os.makedirs(path)

                except Exception as e:

                      print(e)   
                #画图
                draw = ImageDraw.Draw(im1)
                draw.text((0, 0), str(name), (255, 0, 255), font=font)    #设置文字位置/内容/颜色/字体


                #print(result)

                draw = ImageDraw.Draw(im1)#Just draw it!



                #另存图片
                im1.save("识别结果//"+str(kind)+"/"+str(name)+".jpg")

                des_name = str(name)+ '.txt'
                f = open("识别结果//"+str(kind)+"/"+des_name,'w')
                f.write(str(des))
                f.close()

          except Exception as e:

                print(e)  
    


   
  
 

   
  
