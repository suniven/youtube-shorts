# 对图片进行base64编码，解码，解码为numpy，opencv，matplot照片
# USAGE
# python base64_2_jpg.py

import base64
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt


# 将字符串写入文字
#  name 图片名
#  base64_data 图片二进制编码后string流
def write2txt(name, base64_data):
    # 写入_base64.txt
    print(name)
    print(name, len(base64_data))
    basef = open(name + '_base64.txt', 'w')
    data = 'data:image/jpg;base64,%s' % base64_data
    # print(data)
    basef.write(base64_data)
    basef.close()


# 编码图像为base64字符串
def encode_base64(file):
    with open(file, 'rb') as f:
        img_data = f.read()
        base64_data = base64.b64encode(img_data)
        # print(type(base64_data))
        # print(base64_data)
        # 如果想要在浏览器上访问base64格式图片，需要在前面加上：data:image/jpeg;base64,
        base64_str = str(base64_data, 'utf-8')
        # print(base64_str)
        # print(len(base64_data))
        write2txt(file.replace(".jpg", ""), base64_str)
        return base64_data


# 解码base64字符串为图像，并保存
def decode_base64(base64_data):
    with open('./images/base64.jpg', 'wb') as file:
        img = base64.b64decode(base64_data)
        file.write(img)


# 解码base64字符串为numpy图像、opencv、matplot图像

# 解码base64字符串为numpy图像
def decode_base64_np_img(base64_data):
    img = base64.b64decode(base64_data)
    img_array = np.fromstring(img, np.uint8)  # 转换np序列
    print('numpy: ', img_array.shape)
    cv2.imshow("img", img_array)
    cv2.waitKey(0)


# 解码base64字符串为opencv图像
def decode_base64_cv_img(base64_data):
    img = base64.b64decode(base64_data)
    img_array = np.fromstring(img, np.uint8)  # 转换np序列
    img_raw = cv2.imdecode(img_array, cv2.IMREAD_COLOR)  # 转换Opencv格式BGR
    img_gray = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)  # 转换灰度图

    print('opencv bgr: ', img_raw.shape)
    print('opencv gray: ', img_gray.shape)

    cv2.imshow("img bgr", img_raw)
    cv2.imshow("img gray", img_gray)
    cv2.waitKey(0)


# 解码base64字符串为matplot图像
def decode_base64_matplot_img(base64_data):
    img = base64.b64decode(base64_data)
    img_array = np.fromstring(img, np.uint8)  # 转换np序列
    img_raw = cv2.imdecode(img_array, cv2.IMREAD_COLOR)  # 转换Opencv格式BGR
    img_matplot = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)  # BGR转RGB

    img_gray = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)  # 转换灰度图
    imggray_matplot = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)  # 灰度图转RGB
    plt.figure()
    plt.title("Matplot RGB Origin Image")
    plt.axis("off")
    plt.imshow(img_matplot)

    plt.figure()
    plt.title("Matplot Gray Origin Image")
    plt.axis("off")
    plt.imshow(imggray_matplot)
    plt.show()


if __name__ == '__main__':
    # img_path = './images/1622175322109_0.025711.jpg'
    # base64_data = encode_base64(img_path)
    # decode_base64(base64_data)
    #
    # decode_base64_np_img(base64_data)
    # decode_base64_cv_img(base64_data)
    # decode_base64_matplot_img(base64_data)

    # test_image_path = '../cover_img/test/'
    # test_img_list = os.listdir(test_image_path)
    # for img in test_img_list:
    #     encode_base64(test_image_path + img)

    # tt_image_path = '../cover_img/tt/'
    yt_image_path = '../cover_img/yt/'

    # tt_img_list = os.listdir(tt_image_path)
    yt_img_list = os.listdir(yt_image_path)

    # for img in tt_img_list:
    #     encode_base64(tt_image_path + img)

    for img in yt_img_list:
        encode_base64(yt_image_path + img)
