import requests

#输出cookies信息
baidu = requests.get('http://www.baidu.com')
print(type(baidu.cookies))
print(baidu.cookies)
for key,value in baidu.cookies.items():
    print(key+"="+value)