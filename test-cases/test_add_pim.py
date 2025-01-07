import sys
import os
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from base_pages.login_admin_page import login_admin_page
from base_pages.add_pim_page import Add_Pim
from utilities.custom_logger import LogMaker

from time import sleep

# pytest -s -x -v test-cases/test_add_pim.py
# pytest -s -x -v test-cases/test_add_pim.py --test-browser chrome ## 7
# pytest -s -x -v test-cases/test_add_pim.py --test-browser chrome -n 3 ## 8
# pytest -s -v test-cases/test_add_pim.py --html=reports/test_admin_login2.html --self-contained-html -n 4 ## perintah untuk laopran html
# pytest -s -v test-cases/test_add_pim.py --junitxml=reports/test_admin_login.xml ## perintah untuk laporan xml

class Test_Add_Pim:
    
    
    pageUrl         = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username        = "Admin"
    password        = "admin123"
    
    
    def test_add_employee(self, setup: WebDriver):
        try:
            self.driver     = setup
            self.driver.get(self.pageUrl)
            self.driver.maximize_window()
            # Inisiasikan Object Halaman
            self.login_page = login_admin_page(self.driver)
            self.add_admin  = Add_Pim(self.driver)
            sleep(2)
            # Form Login
            self.login_page.enter_username("Admin")
            self.login_page.enter_password("admin123")
            self.login_page.click_login()
            sleep(2)

            # Excetute object add pim
            self.add_admin.get_menu_PIM()
            self.add_admin.btn_add_employee()
            # search_employee.employee_new("Sisia", "lucia", "masia", "0010")
        except:
            pass
       
        
        



