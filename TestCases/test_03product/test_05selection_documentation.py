import allure

from PageObjects.product_cen.selection_documentation_cen_bs import SelectionDocumentationBS


@allure.feature('选品建档')
class TestSelectionDocumentation:
    def test_SelectionDocumentation(self, access_web):
        SelectionDocumentationBS(access_web).selectionDocumentationAdd()
        SelectionDocumentationBS(access_web).selectionDocumentationEdit()
        SelectionDocumentationBS(access_web).selectionDocumentationSubmit()
