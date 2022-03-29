import re
import requests

a = '43,567'
a = re.sub('(,)', '', a)
print(a)

a = 'https://www.youtube.com/shorts/AUXSZtyAnGk'
print(a[-11:])
#
# # 将获取到的图片二进制流写入本地文件
# with open('xxx.jpg', 'wb') as f:
#     # 通过requests发送一个get请求到图片地址，返回的响应就是图片内容
#     r = requests.get('http://i.ytimg.com/vi/eSvIOXueP5U/hq2.jpg')   # 注意不能https
#     f.write(r.content)

URL = 'http://i.ytimg.com/vi/eSvIOXueP5U/hq.jpg'
try:
    r = requests.get(URL, timeout=1)
    r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
except requests.RequestException as e:
    print(e)
else:
    result = r.content
    print(type(result), result, sep='\n')
