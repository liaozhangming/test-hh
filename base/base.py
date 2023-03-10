import sys

import allure
from loguru import logger
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import calendar as cal

# import win32gui
# import win32con
import time, datetime
from selenium.webdriver.common.keys import Keys


# 任何一个步骤都会做到  捕获异常、日志输出、失败截图
class BasePage:
    ''' 包含了PageObjects当中，用到所有的selenium底层方法。
    还可以包含通用的一些元素操作，如alert,iframe,windows...
    还可以自己额外封装一些web相关的断言
    实现日志记录、实现失败截图 '''
    # 公共定位  左上角消息中心
    messageCenter = (By.XPATH, '/html/body/div[1]/section/header/div/div[2]/div/div/div/div/span')
    # 公共定位  消息中心右键后关闭当前页面
    close = (By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/div/ul/li[2]')
    # 公共定位  产品一级菜单
    productFirst = (By.XPATH, '//span[contains(text(),"产品")]')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素可见
    def wait_elevisible(self, loc, timeout=120, frequency=0.5, doc=""):
        """
        :param loc:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        start_time = time.time()
        try:

            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
        except:
            logger.exception("等待{}元素可见超时".format(loc))
            self.screen("等待{}元素可见超时".format(loc))
            raise
        else:
            end_time = time.time()
            duration = end_time - start_time
            logger.info("等待{}元素可见,耗时{}".format(loc, duration))

    # 查找元素
    def is_element_exsits(self, loc, doc=""):
        """
        :param loc:
        :param doc:
        :return:
        """
        try:
            ele = self.driver.find_element(*loc)
        except:
            logger.exception("等待 {} 元素存在，失败！".format(loc))

            return False
        else:
            logger.info("查找{}的元素{}成功。".format(doc, loc))
            return True

    # 查找元素
    def get_element(self, loc, doc=""):
        """
        :param loc:
        :param doc:
        :return:
        """
        try:
            ele = self.driver.find_element(*loc)
        except:
            logger.exception("等待 {} 元素存在，失败！".format(loc))

            raise
        else:
            logger.info("查找{}的元素{}成功。".format(doc, loc))
            return ele

        # 查找元素是否显示

    def get_element_isDisplay(self, loc, doc=""):
        """
        :param loc:
        :param doc:
        :return:
        """
        try:
            self.get_element_text(loc, doc="", timeout=2)
        except:
            logger.exception("页面{}元素不存在！".format(loc))

            return False
        else:
            logger.info("页面{}元素存在！".format(doc, loc))
            return True

    # 输入框输入文本
    def input_text(self, loc, value, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param value:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            ele.send_keys(value)
        except:
            logger.exception("向{}元素输入{}失败".format(loc, value))

            raise
        else:
            logger.info("向{}元素输入{}成功".format(loc, value))

    # 清除输入框中的文本
    def clear_text(self, loc, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param value:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            ele.clear()
        except:
            logger.exception("清除{}内容失败".format(loc))

            raise
        else:
            logger.info("清除{}内容成功".format(loc))

    # 点击
    def click(self, loc, timeout=8, frequency=0.5, doc=""):
        """
        :param loc:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        time.sleep(0.5)
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            ele.click()
        except:
            logger.exception("向{}元素点击失败".format(loc))
            self.screen(doc)
            raise
        else:
            logger.info("向{}元素点击成功".format(loc))

    # 点击
    def click_by_js(self, loc, timeout=8, frequency=0.5, doc=""):
        """
        :param loc:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        time.sleep(0.5)
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            self.driver.execute_script("(arguments[0]).click()", ele)
        except:
            logger.exception("向{}元素点击失败".format(loc))

            raise
        else:
            logger.info("向{}元素点击成功".format(loc))

    # 获取元素文本值
    def get_element_text(self, loc, timeout=8, frequency=0.5, doc=""):
        """
        :param loc:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            text = ele.text
        except:
            logger.exception("获取{}元素文本值失败".format(loc))

            raise
        else:
            logger.info("获取{}元素文本值成功".format(loc))
            return text

    # 获取元素属性
    def get_element_attribute(self, loc, attr, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param attr:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            value = ele.get_attribute(attr)
        except:
            logger.exception("获取{}元素属性值失败".format(loc))

            raise
        else:
            logger.info("获取{}元素属性值成功".format(loc))
            return value

    # 查找多个元素
    def get_elements(self, loc, doc=""):
        """
        :param loc:
        :param doc:
        :return:
        """
        try:
            ele = self.driver.find_elements(*loc)
        except:
            logger.exception("等待 {} 元素存在，失败！".format(loc))

            raise
        else:
            logger.info("查找{}的元素{}成功。".format(doc, loc))
            return ele

    # 获取列表数据长度
    def get_list_length(self, loc, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_elements(loc, doc)
        try:
            value = len(ele)
        except:
            logger.exception("获取{}元素属性值失败".format(loc))

            raise
        else:
            logger.info("获取{}元素属性值成功".format(loc))
            return value

    # 切换窗口
    def switch_window(self, doc=""):
        try:
            # 获取所有的window列表
            windows = self.driver.window_handles
            # 切换到最新窗口
            self.driver.switch_to.window(windows[-1])
        except:
            logger.exception("切换窗口失败")

            raise
        else:
            logger.info("切换窗口成功")

    # 获取当前日期
    def get_date(self):
        return time.strftime("%Y-%m-%d", time.localtime(time.time()))

    # 获取元素默认值
    def get_default_value(self, loc, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            default_value = ele.get_attribute('value')
        except:
            logger.exception("获取{}元素文本值失败".format(loc))

            raise
        else:
            logger.info("获取{}元素文本值成功".format(loc))
            return default_value

    # 输入框输入文本形式上传文件
    def input_text_uploadfile(self, loc, value, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param value:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        ele = self.get_element(loc, doc)
        try:
            ele.send_keys(value)
        except:
            logger.exception("向{}元素输入{}失败".format(loc, value))

            raise
        else:
            logger.info("向{}元素输入{}成功".format(loc, value))

    # 滑动页面到底部
    def slide_to_bottom(self):
        """滑动页面到底部"""
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(1)

    # 滑动页面到顶部
    def slide_to_top(self):
        """滑动页面到顶部"""
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)
        time.sleep(1)

    def screen(self, doc):
        png = self.driver.get_screenshot_as_png()
        allure.attach(png, doc, allure.attachment_type.PNG)

    def move_to(self, loc, timeout=8, frequency=0.5, doc=""):
        ActionChains(self.driver).move_to_element(self.get_element(loc)).perform()

    def wait_time(self, time_):
        self.driver.implicitly_wait(time_)

    '''
      右键点击
      '''

    def rightclick(self, loc, timeout=8, frequency=0.5, doc=""):
        time.sleep(0.5)
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            ActionChains(self.driver).context_click(ele).perform()
        except:
            logger.exception("向{}元素右键点击失败".format(loc))
            self.screen(doc)
            raise
        else:
            logger.info("向{}元素右键点击成功".format(loc))

    '''
      回到消息中心页面，且关闭其他页面
      '''

    def back_to_messagecenter(self, loc1, loc2, timeout=8, frequency=0.5, doc=""):
        self.wait_elevisible(loc1, timeout, frequency, doc)
        self.rightclick(loc1)
        self.wait_elevisible(loc2, timeout, frequency, doc)
        self.click(loc2)

    """ 
    封装当前项目的绝对路径
    """

    def file_path(self, filePath):
        path = sys.path[0]
        filepath_final = path + '\\' + filePath
        return filepath_final

    def refresh(self):
        self.driver.refresh()
