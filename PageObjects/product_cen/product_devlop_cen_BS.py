import time
from loguru import logger
import allure
from pywinauto import Desktop

from base.base import BasePage
from base.sqldeal import sqldeal
from PageLocators.productPage.product_devlop import productDevlop


class ProductDevlopBS(BasePage):

    def productDevlopAdd(self):
        sqldeal(sql='delete from sys_product_select where sku="GA9528";')
        sqldeal(sql='DELETE from sys_product where sku="GA9528";')
        self.click(self.productFirst, doc='点击产品一级菜单')
        self.rightclick(self.messageCenter, doc='消息中心')
        self.click(self.close, doc='关闭其他页面')
        self.click(productDevlop.product_Devlop, doc='产品开发菜单')
        self.click(productDevlop.add_product_Devlop, doc='新增产品开发')
        self.input_text(productDevlop.product_code, 'GA9528', doc='输入产品编码GA9528')
        self.input_text(productDevlop.zh_name, '自动化测试', doc='输入中文名字自动化测试')
        self.input_text(productDevlop.en_name, 'autotest', doc='输入英文名字autotest')
        self.click(productDevlop.product_status_drop, doc='产品状态下拉框')
        try:
            self.click(productDevlop.product_status, doc='产品状态-->正常')
            logger.critical('牛逼class-----------------------------------------'
                            '牛逼class-----------------------------------------')
        except:
            self.click(productDevlop.product_status_1, doc='产品状态-->正常')
            logger.critical('牛蛙牛蛙牛蛙-----------------------------------------'
                            '牛蛙牛蛙牛蛙-----------------------------------------')
        self.click(productDevlop.product_line_drop, doc='产品线下拉框')
        try:
            self.click(productDevlop.product_line, doc='产品线-->GA产品线')
        except:
            self.click(productDevlop.product_line_1, doc='产品线-->GA产品线')
            logger.critical('牛蛙牛蛙牛蛙11111-----------------------------------------'
                            '牛蛙牛蛙牛蛙111111-----------------------------------------')
        self.input_text(productDevlop.price, '2', doc='输入市场参考价')
        self.click(productDevlop.item_name_drop, doc='申报中文名')
        try:
            self.click(productDevlop.item_name, doc='申报中文名垫片')
        except:
            self.click(productDevlop.item_name_1, doc='申报中文名垫片')
            logger.critical('牛蛙牛蛙牛蛙22222-----------------------------------------'
                            '牛蛙牛蛙牛蛙2222222-----------------------------------------')
        self.click(productDevlop.product_type_drop, doc='产品类型下拉框')
        try:
            self.click(productDevlop.product_type, doc='产品类型-->销售商品')
        except:
            self.click(productDevlop.product_type_1, doc='产品类型-->销售商品')
            logger.critical('牛蛙牛蛙牛蛙3333-----------------------------------------'
                            '牛蛙牛蛙牛蛙33333-----------------------------------------')
        self.click(productDevlop.upload_image, doc='选品照片上传按钮')
        app = Desktop()
        dialog = app['打开']  # 根据名字找到弹出窗口
        dialog["Edit"].type_keys(self.file_path('uploadfile\image\\testimage.png'))  # 在输入框中输入值
        dialog["Button"].click()
        # dialog["Button"].click()
        time.sleep(1.5)
        self.input_text(productDevlop.scale, '2', doc='输入市场规模')
        self.input_text(productDevlop.devlop_reason, '自动化测试', doc='输入开发理由')
        self.click(productDevlop.upload_report, doc='上传开发报告')
        app = Desktop()
        dialog = app['打开']  # 根据名字找到弹出窗口
        dialog["Edit"].type_keys(self.file_path('uploadfile\image\\testimage.png'))  # 在输入框中输入值
        dialog["Button"].click()
        # dialog["Button"].click()
        time.sleep(1.5)
        self.click(productDevlop.purchase_add, doc='采购信息添加按钮')
        self.input_text(productDevlop.purchase_suppliers, '江南皮革厂', doc='输入采购信息供应商-->江南皮革厂')
        self.input_text(productDevlop.purchase_suppliers_code, 'GA9528', doc='输入采购信息供应商编码-->GA9528')
        self.input_text(productDevlop.purchase_price, '1', doc='输入采购信息参考价格')
        self.input_text(productDevlop.product_description, '产品描述-自动化测试', doc='输入产品描述')
        self.input_text(productDevlop.brief_description, '简要描述-自动化测试', doc='输入简要描述')
        self.input_text(productDevlop.product_characteristics, '产品特性-自动化测试', doc='输入产品特性')
        self.input_text(productDevlop.purchase_description, '采购描述-自动化测试', doc='输入采购描述')
        self.click(productDevlop.save, doc='点击保存')

    # 查询-编辑-保存-详情-审核
    def productDevlopEdit(self):
        self.input_text(productDevlop.zh_name_input, '自动化测试', doc='输入中文名称查询自动化测试')
        self.click(productDevlop.select_button, doc='查询按钮')
        self.move_to(productDevlop.detail, doc='移动到详情')
        self.click(productDevlop.edit, doc='编辑按钮')
        time.sleep(1)
        self.input_text(productDevlop.edit_en_name, '666', doc='输入英文名称')
        self.click(productDevlop.edit_save, doc='编辑中的保存')
        self.click(productDevlop.detail, doc='点击详情')
        self.click(productDevlop.button_audit, doc='提交审核')
        self.click(productDevlop.button_audit_sure, doc='提交审核确认')
        self.click(productDevlop.audit_person, doc='选择第一个审核人')
        self.click(productDevlop.audit_button, doc='提交审核 -提交')
        time.sleep(2)
        self.click(productDevlop.audit, doc='审核按钮')
        self.click(productDevlop.audit_pass, doc='通过')
        self.click(productDevlop.audit_pass_submit, doc='提交审核通过-提交')
        time.sleep(2)
        self.click(productDevlop.product_image, doc='样品图片')
        app = Desktop()
        dialog = app['打开']  # 根据名字找到弹出窗口
        dialog["Edit"].type_keys(self.file_path('uploadfile\image\\testimage.png'))  # 在输入框中输入值
        dialog["Button"].click()
        time.sleep(2)
        self.click(productDevlop.select_product, doc='选品通过按钮')
        self.click(productDevlop.select_product_yes, doc='选品通过 ->是')
        self.click(productDevlop.select_product_sure, doc='选品通过-提交')
        self.rightclick(self.messageCenter, doc='右击消息中心')
        self.click(self.close, doc='关闭其他页')
        logger.critical('----------------产品开发提交审核执行完毕-----------------')

    # 导入产品开发
    def productDevlopImport(self):
        sqldeal(sql='delete from sys_product_select where sku="GA9529";')
        self.click(productDevlop.product_Devlop,doc='产品开发')
        self.click(productDevlop.import_product, doc='导入产品开发')
        self.click(productDevlop.upload_import_product,doc='点击导入框导入')
        app = Desktop()
        dialog = app['打开']  # 根据名字找到弹出窗口
        dialog["Edit"].type_keys(self.file_path('uploadfile\excel\产品开发模板.xlsx'))  # 在输入框中输入值
        time.sleep(1)
        dialog["Button"].click()
        time.sleep(2)
        self.input_text(productDevlop.zh_name_input, '自动化测试导入', doc='输入查询条件自动化测试导入')
        self.click(productDevlop.select_button, doc='点击查询')
        self.click(self.productFirst, doc='产品一级菜单')
        logger.critical('----------------产品开发导入执行完毕-----------------')

