#!/usr/bin/env python# -*- coding: utf-8 -*-

## ak: gc2yTI4vZm8GRMoyj4q0qHCQ
## sk: hG5S58KMjtK2h6izWPWRVTqpGmkD4Xqj
## at: 24.0b02f32908f5be9c46348bd3223b3f1d.2592000.1653398339.282335-26063997

import os
import time
import copy
import requests
import json
import log
from baidubce import bce_base_client
from baidubce.auth import bce_credentials
from baidubce.auth import bce_v1_signer
from baidubce.http import bce_http_client
from baidubce.http import handler
from baidubce.http import http_methods
from baidubce import bce_client_configuration


def send_request(f, img1_base64, img2_base64, img1_name, img2_name):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
    json_data = [
        {
            "image": img1_base64,
            "image_type": "BASE64",
            "face_type": "LIVE",
            "quality_control": "NONE"
        },
        {
            "image": img2_base64,
            "image_type": "BASE64",
            "face_type": "IDCARD",
            "quality_control": "NONE"
        }
    ]
    params = json_data
    access_token = '24.0b02f32908f5be9c46348bd3223b3f1d.2592000.1653398339.282335-26063997'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, json=params, headers=headers)
    if response:
        print(response.json())
        data = response.json()
        if data["error_code"] == 0:
            result = data["result"]
            score = result["score"]
            if score>=80:
                f.write("{0}\t{1}\t{2}\n".format(img1_name, img2_name, score))  # img1 img2 score
        elif data["error_code"] == 18:  # qps limit * sleep and try again
            time.sleep(2)
            send_request(f, img1_base64, img2_base64, img1_name, img2_name)


if __name__ == '__main__':
    # yt_base64_path = '../cover_img/test/yt_base64/'
    # tt_base64_path = '../cover_img/test/tt_base64/'
    yt_base64_path = '../cover_img/yt_base64/01/'
    tt_base64_path = '../cover_img/tt_base64/'

    yt_base64_file_list = os.listdir(yt_base64_path)
    tt_base64_file_list = os.listdir(tt_base64_path)

    for yt_base64_file in yt_base64_file_list:
        f1 = open(yt_base64_path + yt_base64_file, "r", encoding="UTF-8")
        yt_base64 = f1.read()
        yt_base64.strip('\n')
        f1.close()
        for tt_base64_file in tt_base64_file_list:
            f_log = open("../log/01.txt", "a", encoding="UTF-8")
            f2 = open(tt_base64_path + tt_base64_file, "r", encoding="UTF-8")
            tt_base64 = f2.read()
            tt_base64.strip('\n')
            f2.close()
            yt_base64_file_name = yt_base64_file.replace(".txt", "")
            tt_base64_file_name = tt_base64_file.replace(".txt", "")
            print("Comparing {0} and {1}...".format(yt_base64_file_name, tt_base64_file_name))
            send_request(f_log, yt_base64, tt_base64, yt_base64_file_name, tt_base64_file_name)
            # time.sleep(1.5)
            f_log.close()

# class ApiCenterClient(bce_base_client.BceBaseClient):
#
#     def __init__(self, config=None):
#         self.service_id = 'apiexplorer'
#         self.region_supported = True
#         self.config = copy.deepcopy(bce_client_configuration.DEFAULT_CONFIG)
#
#         if config is not None:
#             self.config.merge_non_none_values(config)
#
#     def _merge_config(self, config=None):
#         if config is None:
#             return self.config
#         else:
#             new_config = copy.copy(self.config)
#             new_config.merge_non_none_values(config)
#             return new_config
#
#     def _send_request(self, http_method, path,
#                       body=None, headers=None, params=None,
#                       config=None, body_parser=None):
#         config = self._merge_config(config)
#         if body_parser is None:
#             body_parser = handler.parse_json
#
#         return bce_http_client.send_request(
#             config, bce_v1_signer.sign, [handler.parse_error, body_parser],
#             http_method, path, body, headers, params)
#
#     def demo(self):
#         path = b'/rest/2.0/face/v3/match'
#         headers = {}
#         headers[b'Content-Type'] = 'application/json;charset=UTF-8'
#
#         params = {}
#
#         params['access_token'] = '24.0b02f32908f5be9c46348bd3223b3f1d.2592000.1653398339.282335-26063997'
#
#         body = '[{\"image\":\"https:\/\/baidu-ai.bj.bcebos.com\/face\/faces.jpg\",\"image_type\":\"URL\"},\n{\"image\":\"https:\/\/baidu-ai.bj.bcebos.com\/face\/faces.jpg\",\"image_type\":\"URL\"}]'
#         return self._send_request(http_methods.POST, path, body, headers, params)
#
#
# if __name__ == '__main__':
#     endpoint = 'https://aip.baidubce.com'
#     ak = ''
#     sk = ''
#     config = bce_client_configuration.BceClientConfiguration(credentials=bce_credentials.BceCredentials(ak, sk),
#                                                              endpoint=endpoint)
#     client = ApiCenterClient(config)
#     res = client.demo()
#     print(res.__dict__['raw_data'])
