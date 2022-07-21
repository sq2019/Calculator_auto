from selenium.webdriver.support.wait import WebDriverWait
import time
# 初始化方法
class Base:
# 初始化方法
    def __init__(self, driver):
        self.driver = driver

# 查找元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        """

        :param loc: 元素定位信息， 格式为：元祖
        :param timeout: 默认超时时间为30s
        :param poll: 访问频率， 默认0.5
        :return: 返回查找到的元素
        """
        # 显式等待
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

# 点击事件
    def base_click(self, loc):
        # 调用查找元素，并引用
        self.base_find_element(loc).click()

# 获取结果值
    def base_get_data(self, loc):
        # 使用get_attribute("") 获取的元素属性值
        return self.base_find_element(loc).get_attribute("value")
# 截图
    def base_screenshot(self):
        self.driver.get_screenshot_as_file('../image/%s.png'%(time.strftime('%Y%m%d_%H%M%S')))