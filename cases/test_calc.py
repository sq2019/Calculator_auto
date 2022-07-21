import unittest
from day07.P02.page.page_calc import PageCalc
from parameterized import parameterized
from day07.P02.base.get_driver import GetDriver
from day07.P02.tool.read_json import ReadJson
def get_data():
    datas = ReadJson().read_json()

    arrs = []
    for data in datas.values():
        arrs.append((data['a'], data['b'], data['expect']))

    return arrs



class TestCalc(unittest.TestCase):

    # setUpclass(cls)
    @classmethod
    def setUpClass(cls) -> None:
        # 初始化 计算页面对象
        cls.calc = PageCalc(GetDriver.get_driver())


    # tearDownClass(cls)
    @classmethod
    def tearDownClass(cls) -> None:
        # 关闭driver
        GetDriver().quit_driver()



    # 测试 加法 方法
    @parameterized.expand(get_data())
    def test_add_calc(self, num1, num2, expect):
        # 调用page页面的组合业务方法
        self.calc.page_add_calc(num1, num2)
        data = self.calc.page_get_data()

        # 断言
        try:
            self.assertEqual(str(expect), data)
            # 截图
        except AssertionError:
            self.calc.page_get_image()
            raise
