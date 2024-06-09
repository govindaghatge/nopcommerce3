import random
import string
import time

from selenium.webdriver.common.by import By

from base_pages.Add_Customer_base_page import Add_Customer
from base_pages.Admin_base_page import Admin_page_login
from utilities.custom_logger import Log_Maker
from utilities.read_properties import Read_Config


class Test_Add_New_Customer:

    Admin_login_url = Read_Config.get_Admin_Url()
    Username = Read_Config.get_Username()
    Password = Read_Config.get_Password()
    logger = Log_Maker.log_gen()


    def test_Add_New_Customer(self, setup):
        self.logger.info("***********Test_Add_Customer_Started**********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.Admin_login_url)
        self.login_page = Admin_page_login(self.driver)
        self.login_page.Username_ActionMethod(self.Username)
        self.login_page.Password_ActionMethod(self.Password)
        self.login_page.Submit_ActionMethod()
        self.driver.maximize_window()

        self.logger.info("***********Login_Completed**********")
        self.logger.info("***********Adding_Customer_Started**********")
        self.Adding_Customer = Add_Customer(self.driver)
        self.Adding_Customer.click_CustomerMenu()
        self.Adding_Customer.click_Customer_submenu()
        self.Adding_Customer.click_Add_New_Btn()

        self.logger.info("***********Test_Providing_UserInfo**********")
        email = generate_random_email()
        self.Adding_Customer.Enter_Email(email)

        self.Adding_Customer.Enter_Password("Test@123")
        self.Adding_Customer.Enter_First_Name("test")
        self.Adding_Customer.Enter_Last_Name("tester")
        self.Adding_Customer.Enter_Gender("Male")
        self.Adding_Customer.Enter_DateOfBirth("10/04/2022")
        self.Adding_Customer.Enter_Company_name("nopcommerce")
        self.Adding_Customer.Select_Is_Tax_Exempt()
        self.Adding_Customer.Select_newsletter("Test store 2")
        self.Adding_Customer.Select_customer_role("Guests")
        self.Adding_Customer.Select_Manager_Vendor("Vendor 1")

        self.logger.info("********Providing_Comment********")

        self.Adding_Customer.Enter_Admin_Comments("Test Admin Comment")
        self.Adding_Customer.click_Save()
        time.sleep(3)

        message = self.driver.find_element(By.CSS_SELECTOR, ".alert alert-success alert-dismissable").text

        if message == "The new customer has been added successfully":
            assert True
            self.logger.info("********Test_Add_Customer_Passed********")
            self.driver.close()
        else:
            self.logger.info("********Test_Add_Customer_Failed********")
            self.driver.save_screenshot(".\\Screenshots\\test_Add_new_customer.png")
            self.driver.close()
            assert False


def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'example.com'])
    return f'{username}@{domain}'
