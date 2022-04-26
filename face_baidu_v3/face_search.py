# encoding:utf-8

import requests
import os
import time
import hashlib
import json

result_file = './search result/result-20220426.txt'


def send_request(img_base64, user_id):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
    json_data = {
        "image": img_base64,
        "image_type": "BASE64",
        "group_id_list": "group_tt",
        "quality_control": "NONE"
    }
    params = json_data
    access_token = '24.0b02f32908f5be9c46348bd3223b3f1d.2592000.1653398339.282335-26063997'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        data = response.json()
        print(response.json())
        if data["error_code"] == 0:
            print("Search Successfully. Saving Result.")
            result = data["result"]
            f = open(result_file, "a", encoding="UTF-8")
            f.write(user_id + '\t' + json.dumps(result) + '\n')
            f.close()
            print("Result Saved.")
        elif data["error_code"] == 18:
            time.sleep(2)
            send_request(img_base64, user_id)


if __name__ == '__main__':
    yt_base64_path = '../cover_img/yt_base64/'
    yt_base64_list = os.listdir(yt_base64_path)
    yt_base64_list.remove('no face')

    for yt_base64_file in yt_base64_list:
        f = open(yt_base64_path + yt_base64_file, "r", encoding='UTF-8')
        yt_base64 = f.read().strip('\n')
        f.close()
        user_id = yt_base64_file[:-11]
        print("Search {0}...".format(user_id))
        send_request(yt_base64, user_id)
