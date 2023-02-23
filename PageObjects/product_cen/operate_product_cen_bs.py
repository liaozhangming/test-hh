import os.path
import sys
import time
import allure
from pywinauto import Desktop
from loguru import logger
from base.base import BasePage
from base.sqldeal import sqldeal
from PageLocators.productPage.operate_product import operateProduct
@allure.feature('运营产品')
class OperateProductBS(BasePage):
    def uploadOperateProduct(self):
        allure.dynamic.title('运营产品导入运营产品')
        logger.info('初始化数据 执行删除sql----')
        sqldeal(sql='DELETE from sys_product where sku="AUTO_001"')
        self.click(self.productFirst, doc='产品一级菜单')
        self.rightclick(self.messageCenter,doc='消息中心')
        self.click(self.close,doc='关闭其他页面')
        self.click(operateProduct.operate_roduct,doc='点击运营产品菜单')
        self.click(operateProduct.import_operateProduct,doc='点击导入运营产品')
        self.click(operateProduct.upload,doc='点击上传文件')
        app = Desktop()
        dialog = app['打开']  # 根据名字找到弹出窗口
        dialog["Edit"].type_keys(self.file_path('uploadfile\excel\运营产品模板V2.xlsx'))  # 在输入框中输入值
        time.sleep(1)
        dialog["Button"].click()
        time.sleep(1.5)
        self.input_text(operateProduct.SKU,'AUTO_001',doc='输入sku -> AUTO_001')
        self.click(operateProduct.select,doc='点击查询')
        logger.critical('-----------------导入运营产品并查询成功-----------------')

    # 编辑运营产品
    def operateProductEdit(self):
        allure.dynamic.title('运营产品_编辑')
        self.click(operateProduct.detail,doc='运营产品详情')
        self.click(operateProduct.detail_edit,doc='详情中的编辑')
        self.click(operateProduct.product_owner_drop, doc='产品负责人下拉框')
        self.click(operateProduct.product_owner, doc='产品负责人')
        self.input_text(operateProduct.price, '2', doc='市场参考价')
        self.click(operateProduct.upload_image, doc='上传样品照片')
        app = Desktop()
        dialog = app['打开']  # 根据名字找到弹出窗口
        dialog["Edit"].type_keys(self.file_path('uploadfile\image\\testimage.png'))  # 在输入框中输入值
        time.sleep(1)
        dialog["Button"].click()
        time.sleep(1.5)
        self.click(operateProduct.edit_save,doc='编辑保存')
        logger.critical('-----------------运营产品编辑保存成功-----------------')


    # 设置授权团队
    def operateProductSetTeam(self):
        self.click(operateProduct.operate_roduct,doc='重新点击运营产品回到运营产品界面')
        self.move_to(operateProduct.detail,doc='移动到详情使得设置手动授权团队按钮出现')
        self.click(operateProduct.set_team,doc='设置手动授权团队')
        self.click(operateProduct.GA_ebay,doc='选择团队GA独立团-ebay')
        self.click(operateProduct.set_team_sure,doc='选择好团队之后点击确定')
        time.sleep(1)
        self.move_to(operateProduct.detail,doc='移动到详情使得授权销售信息出现')
        self.click(operateProduct.set_seller,doc='授权销售信息')
        self.click(operateProduct.set_seller_team_drop,doc='团队下拉框')
        self.click(operateProduct.set_seller_team,doc='选择ga独立团-ebay-千千组')
        self.click(operateProduct.set_sellers_drop,doc='员工下拉框')
        self.click(operateProduct.set_sellers,doc='选择吴千千')
        self.click(operateProduct.status_drop,doc='状态下拉框')
        self.click(operateProduct.status,doc='状态-激活')
        self.click(operateProduct.set_sellers_sure,doc='确定按钮')
        self.click(self.productFirst, doc='产品一级菜单')
        logger.critical('运营产品授权团队执行完毕-------------------')
