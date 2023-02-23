from selenium.webdriver.common.by import By


class productCategory:
    '''
    产品库存元素
    '''
    # 产品库存
    product_category = (By.XPATH, '//*[@id="app"]/section/section/aside/div/div[1]/div[1]/div/ul/li[4]/ul/li/ul/li[4]')
    # sku编码查询
    select_text = (By.XPATH, '/html/body/div[1]/section/section/main/div/div[1]/form/div[1]/div[2]/div/div/input')
    # 仓库名称
    warehouse = (By.XPATH, '/html/body/div[1]/section/section/main/div/div[1]/form/div[2]/div/div/div/div/div/input')
    # 深圳自发货订单仓
    sz_warehouse = (By.XPATH, '//span[contains(text(),"深圳自发货订单仓")]')
    # 查询
    select = (By.XPATH, '/html/body/div[1]/section/section/main/div/div[1]/form/div[5]/button[1]/span')
    # sku编码下拉框
    sku_drop = (By.XPATH, '/html/body/div[1]/section/section/main/div/div[1]/form/div[1]/div[1]/div/div/div/div/input')
    # 点击中文名称
    zh_name=(By.XPATH, '/html/body/div[2]/div[11]/div/div/div[1]/ul/li[2]/span')
