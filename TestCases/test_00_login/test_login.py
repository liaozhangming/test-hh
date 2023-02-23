import os

import pytest

from TestCases.conftest import refresh
from  PageObjects.login_cen.login_cen_bs import  LoginBS as  lb

class TestLogin:
    # @pytest.mark.smoke
    # @pytest.mark.run(order=1)
    # 登录
    # @pytest.mark.parametrize()
    def test_login(self,access_web):
        lb(access_web).login()
        # assert  1==2











