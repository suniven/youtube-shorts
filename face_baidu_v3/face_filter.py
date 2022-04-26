# 先把没有人脸的封面排除掉 节省时间
# encoding:utf-8

import requests
import os
import shutil
import time


def send_request(img_base64):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    json_data = {
        "image": img_base64,
        "image_type": "BASE64"
    }
    params = json_data
    access_token = '24.0b02f32908f5be9c46348bd3223b3f1d.2592000.1653398339.282335-26063997'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        data = response.json()
        print(data)
        if data["error_code"] == 0:
            result = data["result"]
            if result["face_num"] != 0:
                return True
        elif data["error_code"] == 222202:
            return False
        elif data["error_code"] == 18:
            time.sleep(2)
            return send_request(img_base64)
        else:
            return False


if __name__ == '__main__':
    yt_base64_path = '../cover_img/yt_base64/'
    tt_base64_path = '../cover_img/tt_base64/'

    yt_base64_list = os.listdir(yt_base64_path)
    tt_base64_list = os.listdir(tt_base64_path)
    yt_base64_list.remove("no face")
    tt_base64_list.remove("no face")

    for yt_base64 in yt_base64_list:
        f = open(yt_base64_path + yt_base64, "r", encoding="UTF-8")
        img_base64 = f.read().strip('\n')
        f.close()
        print("Processing {0}...".format(yt_base64))
        have_face = send_request(img_base64)
        if not have_face:
            shutil.move(yt_base64_path + yt_base64, yt_base64_path + 'no face/')

    for tt_base64 in tt_base64_list:
        f = open(tt_base64_path + tt_base64, "r", encoding="UTF-8")
        img_base64 = f.read().strip('\n')
        f.close()
        print("Processing {0}...".format(tt_base64))
        have_face = send_request(img_base64)
        if not have_face:
            shutil.move(tt_base64_path + tt_base64, tt_base64_path + 'no face/')
