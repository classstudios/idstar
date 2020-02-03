from aip import AipImageClassify#调用百度AI

APP_ID="15836728"
APP_KEY="KE9KUEv8eVnFl4QURxGte5Pg"
SECRET_KEY="DBeRG73N9oNUQsqYC4U6dH8HbDcyV2jZ"
百度图像识别=AipImageClassify(APP_ID,APP_KEY,SECRET_KEY)

def get_file_content(图片路径):
    with open(图片路径,'rb') as fp:
        return fp.read()

图片路径="1.jpg"

result=百度图像识别.animalDetect(get_file_content(图片路径))


print(result["result"][0]["name"])
