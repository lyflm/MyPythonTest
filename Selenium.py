from selenium import webdriver
import os

# 对应chrome的用户数据存放路径
profile_dir = r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=" + os.path.abspath(profile_dir))
browser = webdriver.Chrome(chrome_options=chrome_options)

#browser.get("http://www.baidu.com")

browser.get("http://ess.10010.com/essframe")