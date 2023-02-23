import time

from PageLocators.productPage.product_management import productManagement
from base.base import BasePage
from loguru import logger


class productManagementBS(BasePage):
    def productManagementSelect(self):
        self.click(self.productFirst, doc='产品一级菜单')
        self.rightclick(self.messageCenter, doc='消息中心')
        self.click(self.close, doc='关闭其他页面')
        self.click(productManagement.product_Management, doc='成品管理菜单')
        self.click(productManagement.un_improve, doc='待完善tab页')
        self.click(productManagement.select_drop, doc='查询条件下拉框')
        try:
            self.click(productManagement.shop_sku, doc='查询条件->渠道sku')
            logger.critical('用span定位')
        except:
            self.click(productManagement.shop_sku_1, doc='查询条件->渠道sku')
        self.input_text(productManagement.select_input, 'POT-14-006', doc='输入查询条件-> POT-14-006')
        self.click(productManagement.select_button, doc='查询按钮')
        self.click(productManagement.reset, doc='重置按钮')
        self.click(productManagement.select_drop, doc='查询条件下拉框')
        try:
            self.click(productManagement.platform_fnsku, doc='查询条件->平台标签')
            logger.critical('用span定位')
        except:
            self.click(productManagement.platform_fnsku_1, doc='查询条件->平台标签')
        self.input_text(productManagement.select_input, 'X003CEJ1RP', doc='输入查询条件->X003CEJ1RP')
        self.click(productManagement.select_button, doc='查询按钮')
        self.click(productManagement.detail, doc='详情')
        self.click(productManagement.close,doc='关闭')
        self.click(self.productFirst,doc='产品一级菜单')

        logger.info('--------------------成品管理查询执行完毕------------------------------')

        time.sleep(1000)