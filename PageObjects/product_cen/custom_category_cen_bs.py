import time

from loguru import logger
from base.base import BasePage
from base.sqldeal import sqldeal
from PageLocators.productPage.custom_category import customCategory


class customCategoryBS(BasePage):
    def custom_category_add(self):
        sqldeal(sql='delete from sys_declaration where name="自动化测试"')
        self.click(self.productFirst, doc='产品一级菜单')
        self.rightclick(self.messageCenter, doc='消息中心')
        self.click(self.close, doc='关闭其他页面')
        self.click(customCategory.custom_Category, doc='点击报关类目菜单')
        self.click(customCategory.add, doc='点击增加')
        self.input_text(customCategory.zh_name, '自动化测试', doc='输入报关中文名称自动化测试')
        self.input_text(customCategory.en_name, 'autotest', doc='输入域报关英文名字autotest')
        self.input_text(customCategory.product_material, '塑料', doc='输入产品材质塑料')
        self.input_text(customCategory.en_product_material, 'suliao', doc='输入英文产品材质suliao')
        self.input_text(customCategory.HS_code, '8467919000', doc='输入海关编码8467919000')
        self.input_text(customCategory.price, '0.5', doc='输入报关价格0.5')
        self.input_text(customCategory.declaration_elements, '聚乙烯', doc='输入申报要素聚乙烯')
        self.click(customCategory.attention, doc='点击注意事项带电')
        self.input_text(customCategory.zh_use, '自动化测试', doc='输入用途中文说明自动化测试')
        self.input_text(customCategory.en_use, 'autotest', doc='输入用途英文说明autotest')
        self.input_text(customCategory.remark, '自动化测试', doc='输入备注自动化测试')
        self.click(customCategory.save,doc='点击保存')
        logger.critical('------------------报关类目新增执行完毕---------------------')

    def custom_category_select(self):
        self.input_text(customCategory.custom_name,'自动化测试',doc='输入查询条件自动化测试')
        self.click(customCategory.select,doc='点击查询')
        self.click(customCategory.detail,doc='点击详情')
        self.click(customCategory.close,doc='点击详情中的关闭')
        self.move_to(customCategory.detail,doc='移动到详情使得编辑按钮出现')
        self.click(customCategory.edit,doc='点击编辑')
        self.input_text(customCategory.remark,'编辑编辑',doc='在备注中输入编辑编辑')
        self.click(customCategory.edit_save,doc='点击编辑中的保存')
        self.click(self.productFirst, doc='产品一级菜单')
        logger.critical('------------------报关类目查询执行完毕---------------------')

