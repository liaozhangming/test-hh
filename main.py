import os

import pytest

if __name__ == '__main__':
    # pytest.main()

    pytest.main(['-vs','--alluredir', './Outputs/allure-report/results', '--clean-alluredir'])
    # pytest.main(['-vs','./TestCases/test_01message/test_01message.py', '--alluredir', './Outputs/allure-report/results', '--clean-alluredir'])
    # pytest.main(['-m','pp1','--lf','--alluredir', './Outputs/allure-report/results', '--clean-alluredir'])
    os.system(r"allure generate ./Outputs/allure-report/results -o ./Outputs/allure-report/report --clean")

