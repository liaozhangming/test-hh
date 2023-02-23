from PageObjects.product_cen.product_category_cen_bs import ProductCategoryBS


class TestProductCategory:
    def test_ProductCategory(self, access_web):
        ProductCategoryBS(access_web).productCategory()
