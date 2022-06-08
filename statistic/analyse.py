if __name__ == '__main__':
    f = open("../txt files/domain_in_comments.txt", "r", encoding="UTF8")
    domains = f.readlines()
    f.close()
    for i in range(len(domains)):
        domains[i] = domains[i].strip()
        if not domains[i]:
            domains.remove(domains[i])
    domains = list(set(domains))
    print("len: ", len(domains))
    print(domains[:])
