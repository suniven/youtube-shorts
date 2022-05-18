if __name__ == '__main__':
    f = open('./url_in_offers.txt', 'r', encoding='UTF8')
    offers = f.readlines()
    f.close()

    f = open('./url_in_comments.txt', 'r', encoding='UTF8')
    comments = f.readlines()
    f.close()

    comments_list = []
    for comment in comments:
        comment = comment.strip('\n')
        if comment:
            comment = '.'.join(comment.split('.')[-2:])
            # print(comment)
            comments_list.append(comment)

    # offers_list=[]
    for offer in offers:
        offer = offer.strip('\n')
        if offer:
            for comment in comments_list:
                if comment in offer:
                    print("offer: {0}\ncomment: {1}".format(offer, comment))
                    f = open('./compare_url_result.txt', 'w', encoding='UTF8')
                    f.write(offer + '\n')
                    f.close()
