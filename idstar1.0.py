from aip import AipImageClassify#调用百度AI

APP_ID="your id"
APP_KEY="your key"
SECRET_KEY="your secret"
百度图像识别=AipImageClassify(APP_ID,APP_KEY,SECRET_KEY)

def get_file_content(图片路径):
    with open(图片路径,'rb') as fp:
        return fp.read()

图片路径="1.jpg"

result=百度图像识别.animalDetect(get_file_content(图片路径))


print(result["result"][0]["name"])
