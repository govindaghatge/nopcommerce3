import pytest
from selenium.webdriver.common.by import By

from base_pages.Admin_base_page import Admin_page_login
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

class Test_Login_page:
    Admin_Page_Url = Read_Config.get_Admin_Url()
    username = Read_Config.get_Username()
    password = Read_Config.get_Password()
    Invalid_Username = Read_Config.get_Invalid_username()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    def test_title_verification(self, setup):
        self.logger.info("*************Test_01_Admin_login*******************")
        self.logger.info("*************Test_Title_Verification started*******************")
        self.driver = setup
        self.driver.get(self.Admin_Page_Url)

        Actual_title = self.driver.title

        if Actual_title == "Your store. Login":
            self.logger.info("*************Title matched*******************")
            assert True
            self.driver.close()

        else:
            self.logger.info("*************Title Does not matched*******************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Valid_login(self, setup):
        self.logger.info("*************Test_Valid_login started*******************")
        self.driver = setup
        self.driver.get(self.Admin_Page_Url)
        self.login_page = Admin_page_login(self.driver)
        self.login_page.Username_ActionMethod(self.username)
        self.login_page.Password_ActionMethod(self.password)
        self.login_page.Submit_ActionMethod()

        act_txt = self.driver.find_element(By.XPATH, "//div [@class = 'content-header'] //h1").text

        if act_txt == "Dashboard":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\valid_login.png")
            self.driver.close()
            assert False


    def test_InValid_login(self, setup):
        self.logger.info("*************Test_InValid_login started*******************")
        self.driver = setup
        self.driver.get(self.Admin_Page_Url)
        self.login_page = Admin_page_login(self.driver)
        self.login_page.Username_ActionMethod(self.Invalid_Username)
        self.login_page.Password_ActionMethod(self.password)
        self.login_page.Submit_ActionMethod()

        act_txt = self.driver.find_element(By.XPATH, "//li").text

        if act_txt == "Np No customer account found":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\Invalid_Login.png")
            self.driver.close()
            assert False