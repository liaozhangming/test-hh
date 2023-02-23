import time

import pytest

from PageObjects.colleague_cen.colleague_cen_bs import ColleagueBS


class TestColleague:
    # @pytest.mark.dependency(depends=['test_00_login'])
    def test_colleague(self, access_web):
        ColleagueBS(access_web).colleague_select_edit()
        ColleagueBS(access_web).colleague_add()
        ColleagueBS(access_web).colleague_team()
