from selenium.webdriver.common.by import By
from selenium import webdriver
import os

# 4
SCREENSHOT_DIR = os.path.join(os.getcwd(), 'screenshot')  # Folder untuk screenshot

class login_admin_page:
    textbox_username_id = "//input[@placeholder='Username']" # "Username" #
    textbox_password_id = "//input[@placeholder='Password']" # "Password" #
    btn_login           = "//button[@type='submit']"
    btn_user            = "//span[@class='oxd-userdropdown-tab']"
    btn_logout          = "//a[normalize-space()='Logout']"
    
    def __init__(self, driver):
        self.driver = driver
        
    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_id).send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_id).send_keys(password)
        
    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login).click()
    
    def click_logout(self):
        self.driver.find_element(By.XPATH, self.btn_user).click()
        self.driver.find_element(By.XPATH, self.btn_logout).click()
        
    def take_screenshot(self,name):
        # Take screenshot
        screenshot_name = f"screenshot_{name}.png"
        screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_name)

        # Membuat Folder jika tidak ditemukan
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        self.driver.save_screenshot(screenshot_path)

        # Verifikasi screenshot di simpan
        assert os.path.exists(screenshot_path), f"Screenshot not saved at {screenshot_path}"
# 4