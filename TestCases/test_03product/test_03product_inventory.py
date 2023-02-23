import allure

from PageObjects.product_cen.product_inventory_cen_bs import ProductCategoryBS

@allure.feature('产品库存')
class TestProductCategory:
    @allure.story('产品库存查询')
    def test_ProductCategory(self, access_web):
        ProductCategoryBS(access_web).productCategorySelect()
