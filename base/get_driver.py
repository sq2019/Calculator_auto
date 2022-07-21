from selenium import webdriver
from day07.P02 import page
from time import sleep
class GetDriver:
    # 如何保证只调用一次，就是把下面的类，设置为类方法

    # 设置类属性
    driver = None

    @classmethod
    # 获取driver

    def get_driver(cls):
        if cls.driver is None:
            # 实例化浏览器
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            # 打开浏览器
            cls.driver.get(page.url)
        return cls.driver  # 保证 永远只返回或调用一个driver



    # 退出driver
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 注意， 此处有一个大坑。 关闭driver之后， 要把driver置空
        cls.driver = None


if __name__ == '__main__':
    # 第一次获取浏览器对象
    print(GetDriver().get_driver())
    GetDriver().quit_driver()




