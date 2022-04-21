import re

if __name__ == '__main__':
    f1 = open("./land_page.txt", encoding='UTF-8')
    f2 = open("./land_page_domain.txt", "w+", encoding='UTF-8')
    lines = f1.readlines()
    domains = []
    for line in lines:
        line = re.findall(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', line)[0] + '\n'
        domains.append(line)
    domains = list(set(domains))  # 去重
    for index, domain in enumerate(domains):
        sub = domain.split('.')
        domains[index] = sub[-2] + '.' + sub[-1]
    domains = list(set(domains))  # 去重
    domains = sorted(domains)
    for domain in domains:
        f2.write(domain)
    f1.close()
    f2.close()
