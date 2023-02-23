from selenium.webdriver.common.by import By

class productManagement:
    """
    成品管理元素定位
    """
    # 成品管理菜单
    product_Management=(By.XPATH,'/html/body/div[1]/section/section/aside/div/div[1]/div[1]/div/ul/li[4]/ul/li/ul/li[7]')
    # 待完善tab页
    un_improve=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[1]/div/div[1]/div/div/div/div[4]')
    #  查询条件下拉框
    select_drop=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[1]/form/div[5]/div[1]/div/div/div/div/input')
    # 查询条件 渠道 sku
    shop_sku=(By.XPATH,'//span[contains(text(),"渠道SKU")]')
    shop_sku_1=(By.XPATH,'/html/body/div[2]/div[8]/div/div/div[1]/ul/li[6]/span')
    # 平台标签
    platform_fnsku=(By.XPATH,'//span[contains(text(),"平台标签")]')
    platform_fnsku_1=(By.XPATH,'/html/body/div[2]/div[8]/div/div/div[1]/ul/li[3]/span')
    # 查询条件输入框
    select_input=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[1]/form/div[5]/div[2]/div/div/input')
    # 查询按钮
    select_button=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[1]/form/div[6]/button[1]')
    # 重置
    reset=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[1]/form/div[6]/button[2]/span')
    # 详情
    detail=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[2]/td/div/div/div[1]/div[2]/div/div[1]/div/table/tbody/tr/td[28]/div/button/span')
    # 详情中的关闭按钮
    close=(By.XPATH,'/html/body/div[5]/div/div/footer/div/button/span')
