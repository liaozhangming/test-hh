from PageObjects.product_cen.custom_category_cen_bs import customCategoryBS


class TestCustomCategory:
    def test_CustomCategory(self, access_web):
        customCategoryBS(access_web).custom_category_add()
        customCategoryBS(access_web).custom_category_select()
