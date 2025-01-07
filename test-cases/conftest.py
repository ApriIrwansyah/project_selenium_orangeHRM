# 5
import pytest
from selenium import webdriver
# 5
# 9
from pytest_metadata.plugin import metadata_key

# # 5
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver
# # 5

# 7
# pada tahap ini kita akan modifikasi untuk bisa memanggil berbagai browser
def pytest_addoption(parser):
    # print(parser.option_string_actions.keys()) # Log semua argumen yang ada
    parser.addoption("--test-browser", action="store", default="chrome", help="Specify the browser: chrome or firefox or edge")
# 7
# 7
@pytest.fixture
def browser(request):
    return request.config.getoption("--test-browser")
# 7
# 7
@pytest.fixture
def setup(browser):
    global driver
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError("browser tidak di support")
    return driver
# 7

# 9
# =======================for pytest html reports==========================================
#  hook for adding environment info in html report / pengait untuk menambahkan info lingkungan dalam laporan html
def pytest_configure(config):
    config.stash[metadata_key]['Project Name']  = "Ecommerce Project, orangeHRM"
    config.stash[metadata_key]['Test Module Name'] = "Test Module Admin Login"
    config.stash[metadata_key]['Tester Name']   = "Apri Irwansyah"
    config.stash[metadata_key]['Base URL']      = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# hook for delete/modify environment info in html report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)