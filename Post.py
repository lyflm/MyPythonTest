import requests

#post发送
data = {'name':'fl','age':'22'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
response = requests.post("http://httpbin.org/post",data=data,headers=headers)
print(response.text)