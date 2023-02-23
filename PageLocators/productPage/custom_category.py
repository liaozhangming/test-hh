from selenium.webdriver.common.by import By


class customCategory:
    '''
    产品模块报关类目元素
    '''
    # 报关类目菜单
    custom_Category=(By.XPATH,'//*[@id="app"]/section/section/aside/div/div[1]/div[1]/div/ul/li[4]/ul/li/ul/li[3]')
    # 增加
    add=(By.XPATH,'//*[@id="app"]/section/section/main/div/div[2]/div[1]/div[1]/button')
    # 报关中文名称
    zh_name=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div/input')
    # 报关英文名称
    en_name=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div/form/div[2]/div/div[1]/div/input')
    # 产品材质
    product_material=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div/form/div[3]/div/div[1]/div/input')
    # 产品材质英文说明
    en_product_material=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div/form/div[4]/div/div[1]/div/input')
    # 海关编码
    HS_code=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div/form/div[5]/div/div[1]/div/input')
    # 报关价格
    price=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div/form/div[6]/div/div[1]/div/input')
    # 申报要素
    declaration_elements=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div/form/div[7]/div/div[1]/div/input')
    # 注意事项_带电
    attention=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div/form/div[8]/div/div/label[1]/span[1]/span')
    # 用途中文说明
    zh_use=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div/form/div[9]/div/div/div/input')
    # 用途英文说明
    en_use=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div/form/div[10]/div/div/div/input')
    # 备注
    remark=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div/form/div[11]/div/div/div/input')
    # 保存
    save=(By.XPATH,'//*[@id="app"]/section/section/main/div/div[3]/div/div/footer/span/button[2]/span')

    # 查询条件  报关名称
    custom_name=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[1]/form/div[1]/div/div/div/input')
    # 查询按钮
    select=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[1]/form/div[3]/button[1]/span')
    # 详情
    detail=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[10]/div/div/div/button/span')
    # 详情中的关闭
    close=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/footer/span/button/span')
    # 编辑
    edit=(By.XPATH,'/html/body/div[2]/div[13]/div/div[1]/div/ul/li')
    # 编辑里的保存
    edit_save=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/footer/span/button[2]/span')