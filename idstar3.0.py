#百度识图API
from aip import AipImageClassify


#给图片加水印  
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


#设置所使用的字体
font = ImageFont.truetype("C:\Windows\Fonts\msyhbd.ttc", 50)

APP_ID = '15836728'
API_KEY = 'KE9KUEv8eVnFl4QURxGte5Pg'
SECRET_KEY = 'DBeRG73N9oNUQsqYC4U6dH8HbDcyV2jZ'
百度识图 = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
    
for i in range(1,50):  
  图片路径 = "pic//"+str(i)+".jpg"

   
  result=百度识图.advancedGeneral(get_file_content(图片路径))

  if "error" in str(result):
      continue

  print(result['result'][0]['keyword'])
  
  im1 = Image.open(图片路径)

  
  #画图
  draw = ImageDraw.Draw(im1)
  draw.text((0, 0), str(result['result'][0]['keyword']), (255, 0, 255), font=font)    #设置文字位置/内容/颜色/字体


  #print(result)
  
  draw = ImageDraw.Draw(im1)#Just draw it!
  
  #另存图片
  im1.save("result//"+str(i)+".jpg")

   
  
