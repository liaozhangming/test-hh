import time

from loguru import logger
from pywinauto import Desktop

from PageLocators.productPage.selection_documentation import selectionDocumentation
from base.base import BasePage
from base.sqldeal import sqldeal
import allure


class SelectionDocumentationBS(BasePage):
    # 选品建档新增
    def selectionDocumentationAdd(self):
        logger.info('--------------------------开始执行删除sql')
        sqldeal(sql='delete from wpm_commodity where sku_detail in("GA008*9528","GA008*9527")')
        self.click(self.productFirst, doc='点击产品一级菜单')
        """下面2行与其他一起跑的时候开启"""
        self.rightclick(self.messageCenter, doc='消息中心')
        self.click(self.close, doc='关闭其他页面')
        self.click(selectionDocumentation.selection_Documentation, doc='点击选品库存')
        self.click(selectionDocumentation.add_skuDetail, doc='点击新增sku明细按钮')
        self.input_text(selectionDocumentation.sku_detail, 'GA008*9527', doc='输入sku明细 GA008*9527')
        self.input_text(selectionDocumentation.reason, '自动化测试', doc='输入申请原因自动化测试')
        self.click(selectionDocumentation.save, doc='点击保存')
        self.click(selectionDocumentation.select_drop, doc='点击查询条件下拉框')
        try:
            self.click(selectionDocumentation.select_sku, doc='点击sku明细查询条件')
            logger.critical('用包含文本定位出来的')
        except:
            self.click(selectionDocumentation.select_sku_1,doc='点击sku明细查询条件')
        self.input_text(selectionDocumentation.select_input, 'GA008*9527', doc='输入查询条件GA008*9527')
        self.click(selectionDocumentation.select_button, doc='点击查询按钮')

    # 新建状态下编辑
    def selectionDocumentationEdit(self):
        self.click(selectionDocumentation.detail, doc='点击详情')
        self.click(selectionDocumentation.detail_edit, doc='点击详情中的编辑')
        self.clear_text(selectionDocumentation.edit_sku_detail, doc='清除sku明细')
        self.clear_text(selectionDocumentation.edit_reason, doc='清除申请原因')
        self.input_text(selectionDocumentation.edit_sku_detail, 'GA008*9528', doc='重新输入sku明细->GA008*9528')
        self.input_text(selectionDocumentation.edit_reason, '自动化测试编辑', doc='重新输入申请原因->自动化测试编辑')
        self.click(selectionDocumentation.edit_save, doc='点击编辑中的保存')
        self.click(selectionDocumentation.reset_button, doc='点击重置按钮')
        self.input_text(selectionDocumentation.select_input, 'GA008*9528', doc='输入查询条件->GA008*9528')
        self.click(selectionDocumentation.select_button, doc='点击查询按钮')
        time.sleep(1)

    def selectionDocumentationSubmit(self):
        self.move_to(selectionDocumentation.detail, doc='移动到详情使得提交按钮出现')
        self.click(selectionDocumentation.submit, doc='点击提交按钮')
        # 将审核人改为亮子
        sqldeal(sql='update wpm_commodity set review_id=257,review_name="亮子" where sku_detail="GA008*9528";')
        self.click(selectionDocumentation.check_box, doc='点击复选框')
        self.click(selectionDocumentation.bulk_review, doc='点击批量审核')
        self.click(selectionDocumentation.bulk_review_sure, doc='点击批量审核确定')
        self.move_to(selectionDocumentation.detail, doc='移动到详情')
        self.click(selectionDocumentation.un_improve_edit, doc='点击待完善状态编辑')
        self.input_text(selectionDocumentation.zh_name, '自动化测试', doc='开票中文名称')
        self.input_text(selectionDocumentation.en_name, 'autotest', doc='开票英文名称')
        self.input_text(selectionDocumentation.material, '材质-塑料', doc='材质')
        self.input_text(selectionDocumentation.code, '100000', doc='成品海关编码')
        self.input_text(selectionDocumentation.use, '自动化测试', doc='用途')
        self.input_text(selectionDocumentation.attribute, '自动化测试-物流属性', doc='物流属性')
        self.click(selectionDocumentation.un_improve_edit_save, doc='待完善编辑中的保存')
        self.move_to(selectionDocumentation.detail, doc='移动到详情')
        self.click(selectionDocumentation.un_improve_button, doc='待完善中的提交')
        self.move_to(selectionDocumentation.detail, doc='移动到详情')
        self.click(selectionDocumentation.un_improve_edit, doc='点击待完善状态编辑')
        self.click(selectionDocumentation.upload_image, doc='待完善编辑上传图片')
        app = Desktop()
        dialog = app['打开']  # 根据名字找到弹出窗口
        dialog["Edit"].type_keys(self.file_path('uploadfile\image\\testimage.png'))  # 在输入框中输入值
        dialog["Button"].click()
        time.sleep(1.5)
        self.click(selectionDocumentation.un_improve_edit_save, doc='待完善上传完图片之后保存')
        self.move_to(selectionDocumentation.detail, doc='移动到详情')
        self.click(selectionDocumentation.un_improve_button, doc='待完善中的提交')
        self.click(self.productFirst, doc='产品一级菜单')
        logger.info('-------选品建档执行完毕----------------')

