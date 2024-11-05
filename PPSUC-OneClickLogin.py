import requests
from random import randrange
from urllib.parse import quote
f=open('账号密码.txt','r+')
data={
    'callback':'dr1730552179698',
    'DDDDD':f.readline()[:-1],
    'upass':f.readline()[:-1],
    '0MKKey':'123456',
    'R1':'0',
    'R3':'0',
    'R6':'0',
    'para':'00',
    'v6ip':'',
    '_':str(randrange(1000000000000,9999999999999))}
header={
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'DNT':'1',
    'Host':'192.168.8.123',
    'Referer':'http://192.168.8.123/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
url = 'http://192.168.8.123/drcom/login?callback=dr1730552179698&DDDDD='+quote(data['DDDDD'])+'&upass='+quote(data['upass'])+'&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&_=1370215579896'
response = requests.post(url,data=data,headers=header).status_code
if response == 200:
    print('已连接（Code:200）')
else:
    print('连接失败（Code:{}）'.format(response))
    input('请按回车键（Enter）结束。')
