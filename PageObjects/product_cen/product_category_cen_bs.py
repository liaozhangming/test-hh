import datetime
import time
from loguru import logger
import allure

from base.base import BasePage
from base.sqldeal import sqldeal
from PageLocators.productPage.product_category import productCategories

t = (datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")


@allure.feature('产品类目')
class ProductCategoryBS(BasePage):

    def productCategory(self):
        allure.dynamic.title('产品类目增加查询编辑')
        self.rightclick(self.messageCenter, doc='右键消息中心')
        self.click(self.close, doc='点击关闭其他页面')
        logger.info('执行删除sql，初始化数据')
        sqldeal(sql='delete from sys_category where name_zh="自动化测试"')
        # 这里右键消息中心 后续补上
        # self.rightclick(productCategories.messageCenter,doc='右键消息中心')
        # self.click(productCategories.close,doc='点击关闭其他页面')
        self.click(productCategories.productFirst, doc='点击产品一级菜单')
        self.click(productCategories.product_categories, doc='点击产品类目')
        self.click(productCategories.add, doc='点击增加')
        self.click(productCategories.add_category, doc='点击上级类目')
        time.sleep(1)
        self.click(productCategories.MBA_category, doc='点击MBA产品线')
        self.input_text(productCategories.add_ZHname, '自动化测试', doc='输入中文名称')
        self.input_text(productCategories.add_EHname, 'autotest', doc='输入英文名称')
        self.input_text(productCategories.add_remark, '自动化测试增加', doc='输入备注')
        self.click(productCategories.add_sure, doc='点击确定')
        self.input_text(productCategories.product_ChineseName, '自动化测试', doc='输入查询条件自动化测试')
        self.click(productCategories.select, doc='点击查询')
        self.click(productCategories.list_detail, doc='点击详情')
        self.click(productCategories.detail_edit, doc='点击详情中的编辑')
        self.clear_text(productCategories.edit_remark, doc='清除编辑中的备注')
        self.input_text(productCategories.edit_remark, '自动化测试' + t, doc='清除编辑中的备注')
        self.click(productCategories.edit_sure, doc='点击编辑中的确定')
        self.click(self.productFirst, doc='产品一级菜单')
        logger.critical('-----------产品类目执行完成---------------')
