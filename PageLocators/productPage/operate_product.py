from selenium.webdriver.common.by import By


class operateProduct:

    # 运营产品菜单
    operate_roduct = (By.XPATH, '//*[@id="app"]/section/section/aside/div/div[1]/div[1]/div/ul/li[4]/ul/li/ul/li[2]')
    # 导入运营产品
    import_operateProduct = (By.XPATH, '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[1]/button[1]/span')
    # 上传文件框
    upload = (
    By.XPATH, '/html/body/div[1]/section/section/main/div/div[5]/div/div/div/div/div/div/div/button[1]/span/div/span')
    # sku输入框
    SKU=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[1]/form/div[2]/div/div/div/input')
    # 查询
    select=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[1]/form/div[5]/button[1]/span')
    # 详情/html/body/div[1]/section/section/main/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[9]/div/div/div/button/span
    detail=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[10]/div/div/div/button/span')
    # 详情中的编辑
    detail_edit=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[1]/button')
    # 编辑中的市场参考价
    price=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div[2]/div/div/form/div[9]/div/div[1]/div/input')
    # 产品负责人下拉框
    product_owner_drop=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div[2]/div/div/form/div[20]/div/div/div/div/div/input')
    # 产品负责人/html/body/div[2]/div[18]/div/div/div[1]/ul/li[1]
    product_owner=(By.XPATH,'/html/body/div[2]/div[20]/div/div/div[1]/ul/li[1]/span')
    # 样品照片
    upload_image=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/ul/div')
    # 保存
    edit_save=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[1]/button')
    # 手动设置授权团队/html/body/div[2]/div[13]/div/div[1]/div/ul/li[3]
    set_team=(By.XPATH,'/html/body/div[2]/div[13]/div/div[1]/div/ul/li[3]')
    # 选择GA独立团ebay
    GA_ebay=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[4]/div/div/div/div/div[1]/div/div[1]/div/div/div/div[4]/div[1]/label/span/span')
    # 设置团队界面确定按钮
    set_team_sure=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[4]/div/div/footer/span/button[2]')
    # 授权销售
    set_seller=(By.XPATH,'/html/body/div[2]/div[13]/div/div[1]/div/ul/li[2]')
    # 授权销售团队下拉框
    set_seller_team_drop=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div/div/div/div/div/input')
    # 团队 -选择GA-独立团吴千千组
    set_seller_team=(By.XPATH,'/html/body/div[2]/div[15]/div/div/div[1]/ul/li[1]/span')
    # 员工下拉框
    set_sellers_drop=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[2]/div/div/div/div/div/input')
    # 员工- 选择吴千千
    set_sellers=(By.XPATH,'/html/body/div[2]/div[16]/div/div/div[1]/ul/li[1]')
    # 状态下拉框
    status_drop=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[3]/div/div/div/div/div/input')
    # 状态选择启用
    status=(By.XPATH,'/html/body/div[2]/div[17]/div/div/div[1]/ul/li[2]')
    # 授权销售信息 -添加按钮
    set_sellers_add=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[4]/div/button[2]')
    # 授权销售信息  确定按钮
    set_sellers_sure=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/footer/button[2]/span')