import argparse, requests

parser = argparse.ArgumentParser()

parser.add_argument('--list', action='store', dest='list', required=False, help='Target list.')
parser.add_argument('--url', action='store', dest='url', required=False, help='Target url.')
arguments = parser.parse_args()
targets = []
directories = ['/.git','/.git/HEAD','/.git/config','/.git/description','/.git/hooks','/.git/index','/.git/info','/.git/logs','/.git/objects','/.git/refs/','/.git/packed-refs','/git']

def main(targets):
    for target in targets:
        print("\n[+] Target: " + target + "\n")
        for directorie in directories:
            req = target+directorie
            responseValue = requests.get(req)
            if responseValue.status_code == 200:
                print('[+] Vulnerable: ' + req + ' ' + str(responseValue.status_code))
            else:
                print('\n[-] Not found: ' + req)

if(arguments.url != None and arguments.list == None):
    targets.append(arguments.url)
    main(targets)

elif(arguments.url != None and arguments.list != None):
    print('You are lost?')
    exit()

else:
    try:
        target_list = open(arguments.list, 'r', errors='ignore')
        for target in target_list.read().splitlines():
            targets.append(target)
        main(targets)

    except FileNotFoundError:
        print('[-] File with url not found.')
        exit()