# 注意代理模式最好设置成全局，否则可能有503或者隐私设置错误

import time
import requests
import os


def get_yt_cover(vid):
    img_path = './cover_img/yt/' + vid + '.jpg'
    img_url = 'http://i.ytimg.com/vi/' + vid + '/hq2.jpg'

    try:
        print("Getting cover {0}...".format(vid))
        r = requests.get(img_url, timeout=2)
        r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
    except requests.RequestException as e:
        print("Error: ", e)
    else:
        with open(img_path, 'wb') as f:
            f.write(r.content)


if __name__ == '__main__':
    f = open("./yt_vid.txt", "r", encoding="UTF-8")
    vid_list = f.readlines()

    exist_list = os.listdir("./cover_img/yt/")

    for vid in vid_list:
        vid=vid.strip('\n')
        if vid + '.jpg' not in exist_list:
            get_yt_cover(vid)
    f.close()
