from day07.P02.base import base
from selenium.webdriver.common.by import By
from day07.P02 import page

class PageCalc(base.Base):
    # 点击数字方法
    def page_click_number(self, num):
        for n in str(num):
            loc = By.CSS_SELECTOR, "#simple{}".format(n)
            self.base_click(loc)
    # 点击+号
    def page_click_add(self):
        self.base_click(page.add)
    # 点击=号
    def page_click_equal(self):
        self.base_click(page.Equal)
    # 获取结果方法
    def page_get_data(self):
       return self.base_get_data(page.result)
    # 点击清屏
    def page_click_clear(self):
        self.base_click(page.clear)

    # 截图
    def page_get_image(self):
        self.base_screenshot()

    # 组装加法业务方法
    def page_add_calc(self, num1, num2):
        self.page_click_number(num1)
        self.page_click_add()
        self.page_click_number(num2)
        self.page_click_equal()

