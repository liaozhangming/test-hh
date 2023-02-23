from PageObjects.product_cen.operate_product_cen_bs import OperateProductBS


class TestOperateProduct:
    def test_OperateProduct(self, access_web):
        OperateProductBS(access_web).uploadOperateProduct()
        OperateProductBS(access_web).operateProductEdit()
        OperateProductBS(access_web).operateProductSetTeam()