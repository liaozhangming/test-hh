import time

import pytest
import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from loguru import logger
from base.sqldeal import sqldeal
from base.base import BasePage
from PageLocators.colleaguePage.colleague_ele import colleagueElement
from config import conf as conf
import allure

date_time = datetime.datetime.now()


# driver=webdriver.Chrome()
class ColleagueBS(BasePage):
    def colleague_select_edit(self):
        allure.dynamic.title('同事_查询编辑同事')
        self.rightclick(self.messageCenter, doc='右键消息中心')
        self.click(self.close, doc='点击关闭其他页面')
        self.click(colleagueElement.colleagueFirstLevel, doc='进入一级同事模块')
        self.click(colleagueElement.colleagueSecondLevel, doc='进入二级同事模块')
        self.input_text(colleagueElement.username, '吴千千', doc='输入查询条件吴千千')
        self.click(colleagueElement.find, doc='点击查询')
        self.click(colleagueElement.click_wu, doc='点击吴千千')
        time.sleep(1)
        self.click(colleagueElement.edit, doc='点击编辑')
        time.sleep(1)
        self.clear_text(colleagueElement.remark, doc='清空备注')
        self.input_text(colleagueElement.remark, '自动化测试' + str(date_time), doc='编辑备注字段')
        self.click(colleagueElement.save, doc='点击保存')
        logger.critical('同事编辑执行完毕-----------------------')

    def colleague_add(self):
        allure.dynamic.title('同事_增加同事查询')
        # self.click(colleagueElement.colleagueFirstLevel, doc='进入一级同事模块')
        sqldeal(sql='delete from user where name="自动化测试"')
        self.click(colleagueElement.colleagueSecondLevel, doc='进入二级同事模块')
        self.click(colleagueElement.add, doc='点击新增')
        self.input_text(colleagueElement.add_username, '自动化测试', doc='输入姓名')
        self.input_text(colleagueElement.add_IDcard, '512222200001021234', doc='输入身份证号码')
        self.click(colleagueElement.isMarry, doc='点击婚姻状态')
        self.click(colleagueElement.unMarry, doc='点击未婚')
        self.input_text(colleagueElement.phone, '13123456789', doc='输入手机号码')
        self.input_text(colleagueElement.wechatId, '13123456789', doc='输入微信ID')
        self.click(colleagueElement.company, doc='点击公司名称')
        self.click(colleagueElement.companyName, doc='点击具体公司名称-深圳市益佰勤科技有限公司')
        self.click(colleagueElement.depart, doc='点击部门名称')
        self.click(colleagueElement.departName, doc='点击具体部门名称-IT研发部')
        self.click(colleagueElement.job, doc='点击岗位名称')
        self.click(colleagueElement.jobName, doc='点击具体岗位名称-超级管理岗')
        self.click(colleagueElement.add_save, doc='点击保存')
        self.click(colleagueElement.reset, doc='重置查询条件')
        self.input_text(colleagueElement.username, '自动化测试', doc='输入查询条件自动化测试')
        self.click(colleagueElement.find, doc='点击查询')
        self.click(colleagueElement.stg, doc='点击三条杠')
        self.move_to(colleagueElement.detail, doc='移动到详情')
        self.click(colleagueElement.buchong, doc='点击补充')
        self.input_text(colleagueElement.qq, '9999999', doc='输入qq')
        self.click(colleagueElement.sure, doc='点击确定')
        logger.critical('同事增加执行完毕-----------------------')
    def colleague_team(self):
        allure.dynamic.title('同事_团队')
        self.click(colleagueElement.colleagueFirstLevel, doc='进入一级同事模块')
        self.click(colleagueElement.team, doc='点击团队')
        self.click(colleagueElement.team_detail, doc='点击GA独立团-Amazon1的详情')
        self.click(colleagueElement.team_cancel, doc='点击详情中的取消')
        self.click(colleagueElement.team_svg, doc='点击小三角')
        self.move_to(colleagueElement.team_sec_detail, doc='移动到详情')
        self.click(colleagueElement.team_edit, doc='点击编辑')
        self.click(colleagueElement.team_add, doc='点击添加')
        self.click(colleagueElement.team_save, doc='点击保存')
        self.move_to(colleagueElement.team_sec_detail, doc='移动到详情')
        self.click(colleagueElement.team_edit, doc='点击编辑')
        self.click(colleagueElement.team_delete, doc='点击删除')
        self.click(colleagueElement.team_sure, doc='点击确认')
        self.click(colleagueElement.team_save, doc='点击保存')
        self.click(colleagueElement.colleagueFirstLevel_1,doc='收缩同事菜单')
        logger.critical('---------------------同事_团队执行完毕-----------------------------')

