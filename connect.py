import requests
from time import sleep

f = open('account.txt', 'r', encoding='utf-8')
lines = f.readlines()
usn = lines[0].strip()
psw = lines[1].strip()
isp = lines[2].strip()
f.close()
url = "http://10.2.5.251:801/eportal/?c=Portal&a=login&login_method=1&user_account=" + usn + "%40" + isp +"&user_password=" + psw
r = requests.get(url)
print(eval(r.content))
sleep(3)
exit()
