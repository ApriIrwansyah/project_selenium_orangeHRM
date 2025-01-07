# 4
import sys
import os

from selenium.webdriver.chrome.webdriver import WebDriver
sys.path.append("../") # file di dalam folder - diluar folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))) # file di dalam folder

import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_pages.login_admin_page import login_admin_page
# 4
from utilities.read_properties import Read_Config # 5
from utilities.custom_logger import LogMaker # 6
from utilities import excel_utils # 10

# ini untuk memanggil config.ini untuk dikonfugurasikan
from time import sleep
import warnings

# pytest -s -x -v test-cases/test_admin_login_datadriven.py
# pytest -s -x -v test-cases/test_admin_login_datadriven.py --test-browser chrome ## 7
# pytest -s -x -v test-cases/test_admin_login_datadriven.py --test-browser chrome -n 3 ## 8
# pytest -s -v test-cases/test_admin_login_datadriven.py --html=reports/test_admin_login_datadriven.html --self-contained-html -n 4 ## perintah untuk laopran html
# pytest -s -v test-cases/test_admin_login_datadriven.py --junitxml=reports/test_admin_login.xml ## perintah untuk laporan xml

class Test_Admin_login:
    # Data ini kita ambil dari config.ini dan read_properties.py
    
    # 5
    pageUrl     = Read_Config.get_admin_page_url()
    # 6
    logger      = LogMaker.log_gen()
    # 6
    # 10
    path        = ".\\test_data\\Admin_orangeHRM_POM_QTOMATION.xlsx"
    status_list = []
    # 10
    # tidak menggunakan data ini karna akan mengambil data dari excel
    # username    = Read_Config.get_username() 
    # password    = Read_Config.get_password() 
    # invalid_username = Read_Config.get_invalid_username() 
    # invalid_password = Read_Config.get_invalid_password()
    # 5
    # akan mengambil logs
    
    @pytest.mark.regression # 13
    @pytest.mark.sanity # 13
    # Success message 
    # 4
    def test_title_verification(self, setup: WebDriver):
        # 6
        self.logger.info("**********Test 01 - Admin Login**********") # 6 info untuk memberikan kesalahan bug (bug) atau mengatur sebagai info (info) untuk memberikan pesan
        self.logger.info("**********Verifikasi halaman login admin**********")
        # 6
        self.driver = setup # 5
        self.driver.implicitly_wait(10) # 10
        self.driver.get(self.pageUrl)
        act_title = self.driver.title
        exp_title = 'OrangeHRM'
        if act_title == exp_title:
            assert True
            # 6
            self.logger.info("**********Verifikasi Pesan test_title berhasil**********")
            # 6
            # self.admin_v.take_screenshot("test_login_valid")
            self.driver.save_screenshot(".\\screenshot\\test_homepage_valid2.png")
            self.driver.close()
        else:
            # 6
            self.logger.info("**********Verifikasi Pesan test_title tidak berhasil**********")
            # 6
            self.driver.close()
            assert False
    # 4
    
    @pytest.mark.regression # 13
    @pytest.mark.sanity # 13
    # 4
    def test_admin_login_valid(self, setup: WebDriver):
        # 6
        self.logger.info("**********Test_admin_login_valid**********")
        # 6
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.pageUrl)
        self.admin_v = login_admin_page(self.driver)
        sleep(2)
        
        # 10
        self.rows = excel_utils.get_row_count(".\\test_data\\Admin_orangeHRM_POM_QTOMATION.xlsx", "Sheet1")
        print("Num of rows : ", str(self.rows))
        
        for r in range(2, self.rows+1):
            self.username       = excel_utils.read_data(self.path, "Sheet1",r, 1)
            self.password       = excel_utils.read_data(self.path, "Sheet1",r, 2)
            self.exp_login      = excel_utils.read_data(self.path, "Sheet1",r, 3)
            self.admin_v.enter_username(self.username)
            sleep(2)
            self.admin_v.enter_password(self.password)
            self.admin_v.click_login()
            sleep(2)
            act_title = self.driver.title
            exp_title = "OrangeHRM"
            
            if act_title == exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data is passed")
                    self.status_list.append('Pass')
                    self.admin_v.click_logout()
                    # assert False
                elif self.exp_login == "No":
                    self.logger.info("test data is failed")
                    self.status_list.append('Fail')
                    # assert True
            elif act_title != exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data is failed")
                    self.status_list.append('Fail')
                elif self.exp_login == "No":
                    self.logger.info("test data is passes")
                    self.status_list.append('Pass')
                    
        print("Status list is : ", self.status_list)
        
        if 'Fail' in self.status_list:
            self.logger.info("Test Admin data driven test is failed")
            # assert False
        elif 'Pass' in self.status_list:
            self.logger.info("Test Admin data driven test is passes")
            # assert True
        else: 
            pass
        # 10
        # 4
    
    # @pytest.mark.regression # 13
    # @pytest.mark.sanity # 13
    # # 4
    # def test_admin_login_invalid(self, setup: WebDriver):
    #     # 6
    #     self.logger.info("**********Test_admin_login_invalid**********")
    #     # 6
    #     self.driver = setup
    #     self.driver.get(self.pageUrl)
    #     self.admin_v = login_admin_page(self.driver)
    #     sleep(2)
    #     self.admin_v.enter_username(self.invalid_username)
    #     sleep(2)
    #     self.admin_v.enter_password(self.invalid_password)
    #     self.admin_v.click_login()
    #     # act_dashboard_text = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
    #     act_dashboard_text = self.driver.title
    #     if act_dashboard_text == "OrangeHRM":
    #         assert True
    #         print(act_dashboard_text)
    #         self.admin_v.take_screenshot("test_login_invalid")
    #         # 6
    #         self.logger.info("**********Verifikasi Pesan Kesalahan Test_admin_login_invalid**********")
    #         # 6
    #         self.driver.close()
            
    #     else:
    #         self.driver.close()
    #         assert False
    # # 4