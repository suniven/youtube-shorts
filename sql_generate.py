if __name__ == '__main__':
    prefix = 'SELECT count(*) from site where '
    f = open("./url_in_comments.txt", "r", encoding="UTF8")
    domains = f.readlines()
    f.close()
    for i in range(len(domains)):
        domains[i] = domains[i].strip('\n')
        if domains[i]:
            domains[i] = "land_page like " + "'%" + domains[i] + "%'"
    sql = prefix + ' or '.join(domains)
    print(sql)
