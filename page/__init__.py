""" 以下为计算机配置数据"""
from selenium.webdriver.common.by import By

"""  以下为服务器域名配置 """
url = "http://cal.apple886.com/"

""" 由于数字键有一定的规律，所以暂时先不用定位此键， 用到的时候在考虑此键怎么解决"""
# clac_num = By.CSS_SELECTOR, "#simple{}"

# 加号
add = By.CSS_SELECTOR, "#simpleAdd"
# 等号
Equal = By.CSS_SELECTOR, "#simpleEqual"
# 清屏
clear = By.CSS_SELECTOR, "#simpleClearAllBtn"
#获取结果
result = By.CSS_SELECTOR, "#resultIpt"




