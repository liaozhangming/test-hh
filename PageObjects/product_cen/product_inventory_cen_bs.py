import time

from loguru import logger

from PageLocators.productPage.product_inventory import productCategory
from base.base import BasePage
import allure


class ProductCategoryBS(BasePage):

    def productCategorySelect(self):
        allure.dynamic.title('产品库存查询')
        self.rightclick(self.messageCenter, doc='消息中心')
        self.click(self.close, doc='关闭其他页面')
        self.click(self.productFirst, doc='产品一级菜单')
        self.click(productCategory.product_category, doc='点击库存菜单')
        self.input_text(productCategory.select_text, 'GA826', doc='输入sku编码GA826')
        self.click(productCategory.warehouse, doc='点击仓库名称')
        self.click(productCategory.sz_warehouse, doc='点击深圳自发货订单仓')
        self.click(productCategory.select, doc='点击查询')
        self.click(productCategory.sku_drop, doc='点击sku编码下拉框')
        self.click(productCategory.zh_name, doc='点击中文名称')
        self.clear_text(productCategory.select_text,doc='清除文本信息')
        self.input_text(productCategory.select_text, '滤清器', doc='输入中文名称滤清器')
        self.click(productCategory.select, doc='点击查询')
        self.click(self.productFirst, doc='产品一级菜单')
        logger.info('-----------执行产品库存查询完毕-------------------------')
