import os

cmd = "get_domain_info.rb -d fbwhores.net"
result = os.popen(cmd)
result = result.read()
print(result)
print(type(result))
if "ServerNotFound" in result:
    print("nnn")

lines = result.splitlines()
for line in lines:
    if "Registrant" in line:
        item_name = line.split(':')[0]
        print("len: ",line.split(':'))
        if item_name == 'Registry Registrant ID':
            try:
                print("--")
                b = line.split(':')[1].strip('\n')
                if b:
                    print(b[1:])
            except:
                print("No ID")
        if item_name == 'Registrant Name':
            try:
                b = line.split(':')[1].strip('\n')
                print(b[1:])
            except:
                print("No ID")
