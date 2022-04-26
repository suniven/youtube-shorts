import json

if __name__ == '__main__':
    result_file = './search result/result-20220426.txt'
    result_filter_file = './search result/result-90.txt'
    f = open(result_file, "r", encoding="UTF-8")
    results = f.readlines()
    f.close()
    for result in results:
        result = result.strip('\n')
        yt_img_id = result.split('\t')[0]
        json_data = json.loads(result.split('\t')[1])
        user_list = json_data["user_list"]
        print(user_list)
        tt_user_id = user_list[0]["user_id"]
        score = user_list[0]["score"]
        if score >= 90:
            print("{0} {1} {2}".format(yt_img_id, tt_user_id, score))
            f = open(result_filter_file, "a", encoding="UTF-8")
            f.write(yt_img_id + '\t' + tt_user_id + '\t' + str(score) + '\n')
            f.close()
