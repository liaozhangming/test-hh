from selenium.webdriver.common.by import By


class productDevlop:
    """
    产品开发元素定位
    """
    # 产品开发菜单
    product_Devlop = (By.XPATH, '/html/body/div[1]/section/section/aside/div/div[1]/div[1]/div/ul/li[4]/ul/li/ul/li[5]')
    # 新增产品开发按钮
    add_product_Devlop = (By.XPATH, '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[1]/button[1]/span')
    # 保存
    save = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div[1]/button/span')
    # 产品编码
    product_code = (By.XPATH,
                    '/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div/div[2]/div/form/div[1]/div/div[1]/div/input')
    # 中文名称
    zh_name = (By.XPATH,
               '/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div/div[2]/div/form/div[3]/div/div[1]/div/input')
    # 英文名称
    en_name = (By.XPATH,
               '/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div/div[2]/div/form/div[5]/div/div[1]/div/input')
    # 产品状态下拉框
    product_status_drop = (By.XPATH,
                           '/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div/div[2]/div/form/div[7]/div/div/div/div/div/input')
    # 产品状态-->正常/html/body/div[2]/div[41]/div/div/div[1]/ul/li[5]/span
    product_status = (By.XPATH, '//span[contains(text(),"正常")]')
    product_status_1 = (By.XPATH, '/html/body/div[2]/div[41]/div/div/div[1]/ul/li[5]')
    # 产品线下拉框
    product_line_drop=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div/div[2]/div/form/div[9]/div/div/div/div/div/input')
    # 产品线-->GA产品线
    product_line =(By.XPATH, '//span[contains(text(),"GA产品线")]')
    product_line_1 = (By.XPATH, '/html/body/div[2]/div[42]/div/div/div[1]/ul/li[2]/span')
    # 市场参考价(USD)
    price = (By.XPATH,
             '/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div/div[2]/div/form/div[11]/div/div[1]/div/input')
    # 申报中文品名下拉框
    item_name_drop = (By.XPATH,
                      '/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div/div[2]/div/form/div[13]/div/div/div/div/div/input')
    # 申报中文品名-->垫片
    item_name = (By.XPATH, '//span[contains(text(),"垫片")]')
    item_name_1 = (By.XPATH, '/html/body/div[2]/div[43]/div/div/div[1]/ul/li[2]')
    # 产品类型下拉框
    product_type_drop = (By.XPATH,
                         '/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div/div[2]/div/form/div[15]/div/div/div/div/div/input')
    # 产品类型-->销售产品
    product_type = (By.XPATH, '//span[contains(text(),"销售商品")]')
    product_type_1 = (By.XPATH, '/html/body/div[2]/div[44]/div/div/div[1]/ul/li[1]/span')
    # 选品照片
    upload_image = (
    By.XPATH, '/html/body/div[1]/section/section/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/ul/div')
    # 开发报告  上传报告
    upload_report=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[2]/div[2]/div[2]/div/div[2]/div/form/div[4]/div[2]/div[1]/div/button/span')
    # 市场规模估算
    scale = (By.XPATH,
             '/html/body/div[1]/section/section/main/div/div/div[2]/div[2]/div[2]/div/div[2]/div/form/div[1]/div/div[1]/div/input')
    # 开发理由
    devlop_reason = (By.XPATH,
                     '/html/body/div[1]/section/section/main/div/div/div[2]/div[2]/div[2]/div/div[2]/div/form/div[3]/div/div[1]/textarea')
    # 采购信息-添加
    purchase_add = (By.XPATH,
                    '/html/body/div[1]/section/section/main/div/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div/div/span/div/button')
    # 采购信息-供应商
    purchase_suppliers = (By.XPATH,
                          '/html/body/div[1]/section/section/main/div/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div/div/div/input')
    # 采购信息 - 供应商编码
    purchase_suppliers_code = (By.XPATH,
                               '/html/body/div[1]/section/section/main/div/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[2]/div/div/div/input')
    # 采购信息 -参考价格
    purchase_price = (By.XPATH,
                      '/html/body/div[1]/section/section/main/div/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[3]/div/div/div/input')
    # 描述信息 -产品描述
    product_description = (By.XPATH,
                           '/html/body/div[1]/section/section/main/div/div/div[2]/div[4]/div/div[2]/div/form/div[1]/div[2]/div/div[2]/div/div[3]/div')
    # 描述信息 -简要描述
    brief_description = (By.XPATH,
                         '/html/body/div[1]/section/section/main/div/div/div[2]/div[4]/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[3]/div')
    # 描述信息 -产品特性
    product_characteristics = (By.XPATH,
                               '/html/body/div[1]/section/section/main/div/div/div[2]/div[4]/div/div[2]/div/form/div[3]/div[2]/div/div[2]/div/div[3]/div')
    # 描述信息 -采购描述
    purchase_description = (By.XPATH,
                            '/html/body/div[1]/section/section/main/div/div/div[2]/div[4]/div/div[2]/div/form/div[4]/div[2]/div/div[2]/div/div[3]/div')
    # 中文名查询条件
    zh_name_input=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[1]/form/div[1]/div[2]/div/div/input')
    # 查询按钮
    select_button=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[1]/form/div[3]/button[1]/span')
    # 详情按钮
    detail=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[9]/div/div/div/button/span')
    # 编辑按钮
    edit=(By.XPATH,'/html/body/div[2]/div[16]/div/div[1]/div/ul/li')
    # 编辑中的英文名
    edit_en_name=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div/div[2]/div/form/div[5]/div/div/div/input')
    # 编辑中的保存
    edit_save=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[1]/button')
    # 提交审核/html/body/div[1]/section/section/main/div/div/div[4]/div/div/footer/button[1]/span
    button_audit=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[1]/button[1]')
    # 提交审核确认
    button_audit_sure=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[3]/div/div/div/div/div/div/div/input')
    # 选择审核人 -龚剑
    audit_person=(By.XPATH, '//span[contains(text(),"龚剑")]')
    # 提交审核 提交
    audit_button=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[3]/div/div/footer/button[1]/span')
    # 选品通过
    select_product=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[1]/button/span')
    # 选品通过  是
    select_product_yes=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[5]/div/div/div/p[2]/label[1]/span[2]')
    # 选品通过 提交
    select_product_sure=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[5]/div/div/footer/button[1]/span')
    # 审核
    audit=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[1]/button')
    # 审核通过
    audit_pass=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[4]/div/div/div/label[2]/span[2]')
    # 审核通过提交
    audit_pass_submit=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[4]/div/div/footer/button[1]/span')
    # 样品照片
    product_image=(By.XPATH,'/html/body/div[1]/section/section/main/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/ul/div')
    # 导入开发产品
    import_product=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[1]/button[2]/span')
    # 上传开发产品
    upload_import_product=(By.XPATH,'/html/body/div[1]/section/section/main/div/div[3]/div/div/div/div/div/div/div/button[1]/span/div/span')
