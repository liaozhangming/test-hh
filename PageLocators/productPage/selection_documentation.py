from selenium.webdriver.common.by import By


class selectionDocumentation:
    """
    选品建档元素
    """
    # 选品建档菜单
    selection_Documentation = (
        By.XPATH, '/html/body/div[1]/section/section/aside/div/div[1]/div[1]/div/ul/li[4]/ul/li/ul/li[6]')
    # 新增sku明细按钮
    add_skuDetail = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div[1]/div[1]/button[1]/span')
    # 新增中的sku明细
    sku_detail = (
        By.XPATH, '/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/form/div[1]/div/div[1]/div/input')
    edit_sku_detail=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/form/div[1]/div/div/div/input')
    # 新增中的申请原因
    reason = (
        By.XPATH, '/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/form/div[2]/div/div[1]/textarea')
    # 保存
    save = (By.XPATH, '/html/body/div[1]/section/section/main/div/div[3]/div/div/div/footer/button[2]')
    # 列表中详情
    detail = (By.XPATH,
              '/html/body/div[1]/section/section/main/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[10]/div/div/div/button/span')
    # 新建状态详情中编辑
    detail_edit = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[4]/div/div/div/footer/div[1]/button[3]/span')
    # 编辑中的申请原因
    edit_reason=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/form/div[2]/div/div/textarea')
    # 编辑中的保存
    edit_save=(By.XPATH,'//*[@id="app"]/section/section/main/div/div[3]/div/div/div/footer/button[2]')
    # 新建状态下的提交
    submit = (By.XPATH, '/html/body/div[2]/div[17]/div/div[1]/div/ul/li[1]')
    # 查询条件下拉框
    select_drop=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[1]/form/div[2]/div[1]/div/div/div/div/input')
    # 查询件条件   选择sku明细
    select_sku = (By.XPATH, '//span[contains(text(),"SKU明细")]')
    select_sku_1 = (By.XPATH,'/html/body/div[2]/div[13]/div/div/div[1]/ul/li[2]/span')
    # 查询条件输入框
    select_input=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[1]/form/div[2]/div[2]/div/div/input')
    # 查询按钮/html/body/div[1]/section/section/main/div/div[1]/form/div[3]/button[1]
    select_button=(By.XPATH,'//*[@id="app"]/section/section/main/div/div[1]/form/div[3]/button[1]/span')
    # 重置按钮
    reset_button=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[1]/form/div[3]/button[2]/span')
    # 选择数据
    check_box=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div/label/span/span')
    # 批量审核
    bulk_review=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[1]/button[5]/span')
    bulk_review_sure =(By.XPATH,'/html/body/div[7]/div/div/div[3]/button[2]/span')
    # 待完善编辑按钮
    un_improve_edit=(By.XPATH,'/html/body/div[2]/div[17]/div/div[1]/div/ul/li[1]')
    # 开票中文名称
    zh_name=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[4]/div/div/div/div/div[2]/div[2]/div[2]/div/form/div[1]/div/div[1]/div/input')
    # 开票英文名称
    en_name=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[4]/div/div/div/div/div[2]/div[2]/div[2]/div/form/div[2]/div/div[1]/div/input')
    # 材质
    material=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[4]/div/div/div/div/div[2]/div[2]/div[2]/div/form/div[3]/div/div[1]/div/input')
    # 成品海关编码
    code=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[4]/div/div/div/div/div[2]/div[2]/div[2]/div/form/div[4]/div/div[1]/div/input')
    # 用途
    use=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[4]/div/div/div/div/div[2]/div[2]/div[2]/div/form/div[5]/div/div[1]/div/input')
    # 物流属性
    attribute=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[4]/div/div/div/div/div[2]/div[2]/div[2]/div/form/div[6]/div/div[1]/div/input')
    # 待完善编辑保存
    un_improve_edit_save=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[4]/div/div/div/footer/div[1]/button[2]')
    # 待完善提交按钮
    un_improve_button=(By.XPATH,'/html/body/div[2]/div[17]/div/div[1]/div/ul/li[2]')
    # 上传图片按钮
    upload_image=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[4]/div/div/div/div/div[1]/div[2]/div/div[1]/ul/div')
