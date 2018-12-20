import xlwt
import re
from selenium import webdriver

def GetData(url):
    # driver = webdriver.Chrome()
    driver = webdriver.PhantomJS()
    driver.get(url)
    data = driver.page_source
    res = []
    lists = []

    res.append(re.findall('<h3 class="tab-title">.*?>(.*?)</a>', data, re.S))

    # 找到大的分类
    partten = re.compile('<ul class="interval01-list"(.*?)</ul>', re.S)
    parts = re.findall(partten, data)

    # append 接受一个参数，这个参数可以是任何数据类型，并且简单地追加到 list 的尾部。
    # 找到所有的款式
    for part in parts:
        partten = re.compile('<li(.*?)</li>', re.S)
        a = re.findall(partten, part)
        for b, c in enumerate(a):
            lists.append(c)

    for i in lists:
        partten = re.compile('<div class="interval01-list-cars-infor">.*?>.*?>(.*?)<+'
                             '.*?<span>(.*?)</span>.*?<span>(.*?)</span>'
                             '.*?<div class="interval01-list-guidance">.*?</a>\s+?(.*?)\s+?'
                             '.*?carkind.*?<.*?>(.*?)</', re.S)
        res.extend(re.findall(partten, i))
    return res


URL = 'https://www.autohome.com.cn/'
row = 0
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('cars')

for n in range(16, 512):
    res = GetData(URL + str(n))
    if len(res[0]):
        print(res)
        for car in res:
            for col, item in enumerate(car):
                worksheet.write(row, col, item)
            row += 1

workbook.save('Cars.xls')
print("over")
