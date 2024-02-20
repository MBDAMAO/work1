import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置日期和货币代号
date = "20211231"
currency = "USD"

# 创建文件用于存储结果
result_file = open("result.txt", "w")

# 启动浏览器
driver = webdriver.Chrome()

try:
    # 打开中国银行外汇牌价网站
    driver.get("https://www.boc.cn/sourcedb/whpj/")

    # 输入日期
    date_input = driver.find_element(By.NAME, "erectDate")
    date_input.send_keys(date)

    # 输入货币代号
    currency_input = driver.find_element(By.NAME, "pjname")
    currency_input.send_keys(currency)

    # 点击查询按钮
    query_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='查询']")))
    query_button.click()

    # 等待1秒让数据加载
    time.sleep(1)

    # 获取现汇卖出价
    sell_price = driver.find_element(By.XPATH, "//table[@class='bocha']/tbody/tr/td[contains(text(), '现汇卖出价')]/following-sibling::td[1]").text

    # 将结果写入文件，并打印在控制台
    result_file.write(sell_price)
    print(sell_price)

except Exception as e:
    print("An error occurred:", e)

finally:
    # 关闭浏览器和文件
    driver.quit()
    result_file.close()
