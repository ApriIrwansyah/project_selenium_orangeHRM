# file utilitas ini digunakan untuk membaca data dari file config.ini ?
# 5
import configparser
import sys
import os
sys.path.append("../")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))


config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

# membuat class
class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url     = config.get('admin login info', 'pageUrl')
        return url
    
    @staticmethod
    def get_username():
        username     = config.get('admin login info', 'username')
        return username
    
    @staticmethod
    def get_password():
        password     = config.get('admin login info', 'password')
        return password
    
    @staticmethod
    def get_invalid_username():
        invalid_username     = config.get('admin login info', 'invalid_username')
        return invalid_username
    
    @staticmethod
    def get_invalid_password():
        invalid_password     = config.get('admin login info', 'invalid_password')
        return invalid_password
# 5