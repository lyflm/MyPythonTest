import requests

#使用session用于模拟以下操作是基于同一个浏览器访问(模拟会话)
s = requests.session()
s.get('http://httpbin.org/cookies/set/number/123456')
response = s.get('http://httpbin.org/cookies')

#输出cookies信息
print(type(response))
print(response.text)

#状态码
print(type(response.status_code))
print(response.status_code)
