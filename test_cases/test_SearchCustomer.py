import time

import pytest

from base_pages.Add_Customer_base_page import Add_Customer
from base_pages.Admin_base_page import Admin_page_login
from base_pages.Search_page_BaseClass import Search_Customer
from utilities.custom_logger import Log_Maker
from utilities.read_properties import Read_Config

class Test_SearchCustomer:

    Admin_login_url = Read_Config.get_Admin_Url()
    Username = Read_Config.get_Username()
    Password = Read_Config.get_Password()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    def test_Search_CustomerByEmail(self, setup):
        self.logger.info("***********Test_SearchCustomer_Started**********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.Admin_login_url)
        self.login_page = Admin_page_login(self.driver)
        self.login_page.Username_ActionMethod(self.Username)
        self.login_page.Password_ActionMethod(self.Password)
        self.login_page.Submit_ActionMethod()
        self.driver.maximize_window()

        self.Adding_Customer = Add_Customer(self.driver)
        self.Adding_Customer.click_CustomerMenu()
        self.Adding_Customer.click_Customer_submenu()

        self.search = Search_Customer(self.driver)
        self.search.Enter_Email("admin@yourstore.com")
        self.search.Click_Searchbutton()
        time.sleep(2)
        is_Email_present = self.search.search_customer_by_email("admin@yourstore.com")
        if is_Email_present == True:
            assert True
            self.logger.info("***********test_Search_CustomerByEmail_is_Passed*********")
            self.driver.close()
        else:
            self.logger.info("***********test_Search_CustomerByEmail_is_Failed*********")
            self.driver.save_screenshot(".\\screenshots\\email.png")
            self.driver.close()
            assert False

    def test_Search_CustomerByName(self, setup):
        self.logger.info("***********Test_SearchCustomer_Started**********")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.Admin_login_url)
        self.login_page = Admin_page_login(self.driver)
        self.login_page.Username_ActionMethod(self.Username)
        self.login_page.Password_ActionMethod(self.Password)
        self.login_page.Submit_ActionMethod()
        self.driver.maximize_window()

        self.Adding_Customer = Add_Customer(self.driver)
        self.Adding_Customer.click_CustomerMenu()
        self.Adding_Customer.click_Customer_submenu()

        self.search = Search_Customer(self.driver)
        self.search.Enter_firstName("James")
        self.search.Enter_LastName("Pan")
        self.search.Click_Searchbutton()
        time.sleep(2)
        is_Name_present = self.search.search_customer_by_name("James Pan")
        if is_Name_present == True:
            assert True
            self.logger.info("***********test_Search_CustomerByName_is_Passed*********")
            self.driver.close()
        else:
            self.logger.info("***********test_Search_CustomerByName_is_Failed*********")
            self.driver.save_screenshot(".\\screenshots\\name.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_Search_CustomerByCompany(self, setup):
        self.logger.info("***********Test_SearchCustomer_Started**********")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.Admin_login_url)
        self.login_page = Admin_page_login(self.driver)
        self.login_page.Username_ActionMethod(self.Username)
        self.login_page.Password_ActionMethod(self.Password)
        self.login_page.Submit_ActionMethod()
        self.driver.maximize_window()

        self.Adding_Customer = Add_Customer(self.driver)
        self.Adding_Customer.click_CustomerMenu()
        self.Adding_Customer.click_Customer_submenu()

        self.search = Search_Customer(self.driver)
        self.search.Enter_CompanyName("Indian Cricket Team")
        self.search.Click_Searchbutton()
        time.sleep(2)
        is_Company_present = self.search.search_customer_by_company("England Cricket Team")
        if is_Company_present == True:
            assert True
            self.logger.info("***********test_Search_CustomerByCompany_is_Passed*********")
            self.driver.close()
        else:
            self.logger.info("***********test_Search_CustomerByCompany_is_Failed*********")
            self.driver.save_screenshot(".\\screenshots\\companyname.png")
            self.driver.close()
            assert False