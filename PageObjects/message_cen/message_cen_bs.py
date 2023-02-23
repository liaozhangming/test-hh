import datetime
import time
from loguru import logger
import allure

from base.base import BasePage
from PageLocators.messagePage.message_ele import messageElement

t = (datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")

@allure.story('消息查询')
class MessageBS(BasePage):

    def messageSelect(self):
        allure.dynamic.title('消息查询')
        self.click(messageElement.system_notice, doc='点击系统公告')
        self.input_text(messageElement.message_doc, 'ybq越来越好', doc='输入消息内容')
        self.click(messageElement.message_select, doc='点击查询')
        # time.sleep(1)

    @allure.story('消息接收设置')
    def messageReceiveSet(self):
        allure.dynamic.title('消息接收设置')
        self.click(messageElement.message_receive_set, doc='点击消息接收设置')
        self.input_text(messageElement.message_receive_doc, '亮子', doc='输入消息内容亮子')
        self.click(messageElement.message_receive_select, doc='点击查询')
        self.click(messageElement.message_receive_email, doc='双击行政公告的邮件第一次')
        time.sleep(0.5)
        self.click(messageElement.message_receive_email, doc='双击行政公告的邮件第二次')

    @allure.story('消息发布')
    def messagePublish(self):
        allure.dynamic.title('过滤查询-新增-存为草稿-编辑')
        self.click(messageElement.message_publish, doc='点击消息发布')
        self.click(messageElement.message_publish_news, doc='点击发公告')
        self.click(messageElement.message_type, doc='点击消息类型')
        self.click(messageElement.system_publish, doc='点击系统')
        self.input_text(messageElement.send_time, t, doc='输入发送时间')
        self.click(messageElement.send_range, doc='点击选择发送范围')
        self.click(messageElement.all_select, doc='点击全选')
        self.input_text(messageElement.title, 'ybq越来越好 来来来来', doc='输入标题')
        time.sleep(0.5)
        self.click(messageElement.mark, doc='标记为重要')
        self.input_text(messageElement.content, 'ybq越来越好了哦', doc='输入正文')
        self.click(messageElement.save_draft, doc='点击存为草稿')
        self.click(messageElement.edit, doc='点击编辑')
        self.click(messageElement.send, doc='点击发送')
        self.click(messageElement.withdraw, doc='点击撤回')
        self.click(messageElement.sure, doc='点击确认')

    @allure.story('消息发布')
    def messageDel(self):
        allure.dynamic.title('存为草稿_查询_删除')
        self.click(messageElement.message_publish, doc='点击消息发布')
        self.click(messageElement.message_publish_news, doc='点击发公告')
        self.click(messageElement.message_type, doc='点击消息类型')
        self.click(messageElement.system_publish, doc='点击系统')
        self.input_text(messageElement.send_time, t, doc='输入发送时间')
        self.click(messageElement.send_range, doc='点击选择发送范围')
        self.click(messageElement.all_select, doc='点击全选')
        self.input_text(messageElement.title, '自动化删除', doc='输入标题')
        time.sleep(0.5)
        self.click(messageElement.mark, doc='标记为重要')
        self.input_text(messageElement.content, '自动化删除', doc='输入正文')
        self.click(messageElement.save_draft, doc='点击存为草稿')
        self.input_text(messageElement.message_title, '自动化删除', doc='输入查询条件消息标题')
        self.click(messageElement.message_select, doc='点击查询')
        self.move_to(messageElement.message_edit, doc='移动到编辑按钮使得删除按钮出现')
        self.click(messageElement.message_del, doc='点击删除按钮')
        self.click(messageElement.message_sure, doc='点击确认')
        logger.info('----消息模块执行完毕---------------------')

