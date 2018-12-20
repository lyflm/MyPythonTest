from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://weibo.com/?c=spr_sinamkt_buy_hyww_weibo_t112")

time.sleep(3)
# 浏览器全屏显示
#driver.maximize_window()

#通过用户名密码登陆
driver.find_element_by_id("loginname").send_keys("15637793562")
driver.find_element_by_name("password").send_keys("Fl523571")

#勾选保存密码
#driver.find_element_by_id("login_form_savestate").click()
time.sleep(3)

#点击登陆按钮
driver.find_element_by_css_selector("a[action-type=\"btn_submit\"]").click()

#获取cookie信息并打印
cookie= driver.get_cookies()
print (cookie)

time.sleep(2)
driver.close()

