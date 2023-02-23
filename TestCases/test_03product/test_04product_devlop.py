from PageObjects.product_cen.product_devlop_cen_BS import ProductDevlopBS


class TestProductDevlop:
    def test_productDevlop(self, access_web):
        ProductDevlopBS(access_web).productDevlopAdd()
        ProductDevlopBS(access_web).productDevlopEdit()
        ProductDevlopBS(access_web).productDevlopImport()