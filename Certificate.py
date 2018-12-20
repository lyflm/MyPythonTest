import requests
from requests.packages import urllib3

#以下会显示错误，因为需要证书验证
#response = requests.get('https://www.12306.cn')
#print(response.status_code)

#解决证书问题，我们有两种方法
#方法一，我们可以通过设置verify=False来忽略证书验证
#以上解决了证书验证问题，但是仍然是有警告抛出：
# InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised.

response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)

#方法二，手动传入证书，如果有的话
#response = requests.get('https://www.12306.cn',cert=('/path/server.vrt','/path/key'))
# ess = requests.get('http://ess.10010.com/essframe')
# print(ess.status_code)
# print(ess.headers)