from selenium import webdriver
import time

# 启动浏览器
driver = webdriver.Chrome()

# 打开一个网页
#driver.get("https://qimg2.xyy001.com/qnjymp/stable/main/index.html?token=%257EVggIBQZQDwFfVwtWHwYDG1dUDQ1TVAEMDh%252FRkofU%252B7%252BAi6htQwEaUgcOQAAfBB9ZEwlUFQ0QX1gPAQ%253D%253D%257E1%257E#/v5/printList")
# driver.get('http://www.baidu.com')

# 获取当前时间
current_time = driver.execute_script("return new Date().toLocaleString()")

# 修改时间（示例为将当前时间加上一小时）
driver.execute_script("var date = new Date(); date.setHours(date.getHours() + 1);")
# # 打开一个网页
driver.get('http://www.baidu.com')
# 获取修改后的时间

driver.refresh()
modified_time = driver.execute_script("return new Date().toLocaleString()")

# 输出时间
print("当前时间：", current_time)
print("修改后时间：", modified_time)
time.sleep(1)
# 关闭浏览器
# driver.quit()

