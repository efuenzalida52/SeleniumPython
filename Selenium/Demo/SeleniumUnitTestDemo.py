# https://stackoverflow.com/questions/1322575/what-numbers-can-you-pass-as-verbosity-in-running-python-unit-test-suites
import HtmlTestRunner
import unittest
from selenium import webdriver

class MyTestCase(unittest.TestCase):

    # setUpself(self): would run after every test/method same w/ teardown
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search01(self):
        self.driver.get('http://google.com')
        self.driver.find_element_by_name('q').send_keys('automation step by step')
        self.driver.find_element_by_name('btnK').click()
        x = self.driver.title
        print(x)
        # msg will only appear if test fails
        self.assertEqual(x, 'automation step by step - Google Search', msg='error!')

    def test_search02(self):
        self.driver.get('http://google.com')
        self.driver.find_element_by_name('q').send_keys('Elizabeth Fuenzalida')
        self.driver.find_element_by_name('btnK').click()
        x = self.driver.title
        print(x)
        # msg will only appear if test fails
        # this test should fail
        # self.assertEqual(x, 'automation step by step - Google Search', msg='error!')
        self.assertEqual(x, 'Elizabeth Fuenzalida - Google Search')

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/elizabeth.fuenzalida/PycharmProjects/Selenium/Reports'), verbosity=2)
# in command line add ing the flag -v or --verbose would also work
