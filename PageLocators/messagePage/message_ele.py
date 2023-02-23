import time

from selenium.webdriver.common.by import By


class messageElement:
    """
    消息模块元素
    """
    # 消息中心_系统公告
    system_notice=(By.XPATH, '//span[contains(text(),"系统公告")]')
    # 消息内容
    message_doc=(By.XPATH, '//form/div/div/div/div/input')
    # 查询
    message_select=(By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div[2]/form/div[3]/button[1]/span')

    # --------------------消息接收设置-------------------------------------------
    # 消息接收设置
    message_receive_set=(By.XPATH, '//*[@id="app"]/section/section/aside/div/div[1]/div[1]/div/ul/li[1]/ul/li/ul/li[2]')
    # 输入查询内容
    message_receive_doc=(By.XPATH, '//form/div[2]/div/div/div/input')
    # 查询
    message_receive_select=(By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div/form/div[3]/button[1]')
    # 行政公告中的邮件
    message_receive_email=(By.XPATH, '//table/tbody/tr[1]/td[5]/div/label/span/span')

    # ------------------消息发布-----------------------
    # allure.dynamic.title('过滤查询-新增-存为草稿-编辑')
    # 消息发布
    message_publish=(By.XPATH, '//*[@id="app"]/section/section/aside/div/div[1]/div[1]/div/ul/li[1]/ul/li/ul/li[3]')
    # 发布公告
    message_publish_news=(By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div[1]/button/span')
    # 消息类型
    message_type=(By.XPATH, '//section/main/div/div/div/div[2]/div/form/div[2]/div/div/div/div/div/input')
    # 系统公告
    system_publish=(By.XPATH, '/html/body/div[2]/div[11]/div/div/div[1]/ul/li[6]')
    # 预约发送时间
    send_time=(By.XPATH, '//section/main/div/div/div/div[2]/div/form/div[3]/div/div/div/input')
    # 选择发送范围
    send_range=(By.XPATH, '//section/main/div/div/div/div[2]/div/form/div[5]/div[2]/div/div[2]/div[2]')
    # 全选
    all_select=(By.XPATH, '//form/div[5]/div[2]/div/div[1]/div/div/footer/span/button[2]/span')
    # 标题
    title=(By.XPATH, '//section/main/div/div/div/div[3]/div/div[1]/form/div[1]/div/div[1]/div/input')
    # 标记为重要
    mark=(By.XPATH, '//form/div[2]/div/label/span[1]/span')
    # 正文文本框
    content=(By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div[3]/div/div[2]/form/div[1]/div[2]/div/div[2]/div/div[3]/div')
    # 存为草稿
    save_draft=(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div[1]/button[2]/span')
    # 编辑
    edit=(By.XPATH, '//table/tbody/tr[1]/td[8]/div/div/div/button/span')
    # 发送
    send=(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div[1]/button[1]')
    # 撤回
    withdraw=(By.XPATH, '//div/table/tbody/tr[1]/td[8]/div/button/span')
    # 确认
    sure=(By.XPATH,'/html/body/div[7]/div/div/div[3]/button[2]/span')
    # 查询条件_消息标题
    message_title=(By.XPATH, '/html/body/div[1]/section/section/main/div/div[1]/div[2]/form/div[1]/div/div/div/input')
    # 消息公告查询
    message_publish_select=(By.XPATH, '/html/body/div[1]/section/section/main/div/div[1]/div[2]/form/div[3]/button[1]/span')
    # 编辑按钮
    message_edit=(By.XPATH,'//div/table/tbody/tr/td[8]/div/div/div/button/span')
    # 删除按钮
    message_del=(By.XPATH, '/html/body/div[2]/div[14]/div/div[1]/div/ul/li')
    message_sure=(By.XPATH, '/html/body/div[7]/div/div/div[3]/button[2]/span')#/html/body/div[5]/div/div/div[3]/button[2]/span