from PageObjects.product_cen.product_management_cen_bs import productManagementBS


class TestProductManagement:
    def test_productManagement(self, access_web):
        productManagementBS(access_web).productManagementSelect()

