import time

from selenium.webdriver.common.by import By


class productCategories:
    """
    产品模块元素
    """
    # 进入系统默认的消息中心
    messageCenter=(By.XPATH,'/html/body/div[1]/section/header/div/div[2]/div/div/div/div/span')
    # 关闭其他标签页/html/body/div[2]/div[1]/div/div[1]/div/ul/li[2]
    close=(By.XPATH,'/html/body/div[2]/div[1]/div/div[1]/div/ul/li[2]')
    # 产品一级菜单
    productFirst=(By.XPATH, '//span[contains(text(),"产品")]')
    # 产品类目
    product_categories=(By.XPATH, '//*[@id="app"]/section/section/aside/div/div[1]/div[1]/div/ul/li[4]/ul/li/ul/li[1]')
    # 中文名称
    product_ChineseName=(By.XPATH, '/html/body/div[1]/section/section/main/div/div[1]/form/div[1]/div/div/div/input')
    # 查询按钮
    select=(By.XPATH, '/html/body/div[1]/section/section/main/div/div[1]/form/div[4]/button[1]/span')
    # 增加按钮
    add=(By.XPATH, '/html/body/div[1]/section/section/main/div/div[2]/div[1]/button')
    # 增加里面的上级类目
    add_category=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/form/div[1]/div/div/div/div/div/input')
    # MBA产品线/html/body/div[2]/div[22]/div/div/div[1]/ul/li[1]/span
    MBA_category=(By.XPATH,'//span[contains(text(),"MBA产品线")]')
    # 增加中文名称
    add_ZHname=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/form/div[2]/div/div[1]/div/input')
    # 增加英文名称
    add_EHname=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/form/div[3]/div/div[1]/div/input')
    # 增加_备注
    add_remark=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/form/div[4]/div/div/div/input')
    # 增加_确定
    add_sure=(By.XPATH, '/html/body/div[1]/section/section/main/div/div[3]/div/div/footer/button[2]/span')
    # 列表的详情
    list_detail=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[7]/div/div/div/button/span')
    # 详情中的编辑
    detail_edit=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[4]/div/div/footer/button[1]/span')
    # 编辑中的备注
    edit_remark=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/form/div[4]/div/div/div/input')
    # 编辑中的确定
    edit_sure=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/footer/button[2]')