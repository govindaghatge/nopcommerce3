import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Add_Customer:

    Customer_Menu = "//a [@href='#']//p[contains(text(),'Customers')]"
    Customer_Sub_Menu = "//li [@class='nav-item']//p[contains(text(),'Customers')]"
    Add_New_btn = "//a [@class='btn btn-primary']"
    Email_Id = "Email"
    Password_Id = "Password"
    First_Name_Id = "FirstName"
    Last_Name_Id = "LastName"
    Gender_Id = "Gender_Male"
    DateOfBirth_Id = "DateOfBirth"
    Company_name_Id = "Company"
    Is_Tax_Exempt_Id = "IsTaxExempt"
    Newsletter = "//div [@role='listbox']"
    Customer_Administrators = "//li[contains(text(),'Administrators')]"
    Customer_Forum_Moderators = "//li[contains(text(),'Forum Moderators')]"
    Customer_Registered = "//li[contains(text(),'Registered')]"
    Customer_Guests = "//li[contains(text(),'Guests')]"
    Customer_Vendors = "//li[contains(text(),'Vendors')]"
    Manager_of_Vendor_Id = "VendorId"
    Admin_comment = "AdminComment"
    save_btn = "//button [@name='save']"

    def __init__(self, driver):
        self.driver = driver


    def click_CustomerMenu(self):
        self.driver.find_element(By.XPATH, self.Customer_Menu).click()

    def click_Customer_submenu(self):
        self.driver.find_element(By.XPATH, self.Customer_Sub_Menu).click()

    def click_Add_New_Btn(self):
        self.driver.find_element(By.XPATH, self.Add_New_btn).click()

    def Enter_Email(self, email):
        self.driver.find_element(By.ID, self.Email_Id).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(By.ID, self.Password_Id).send_keys(password)

    def Enter_First_Name(self, Firstname):
        self.driver.find_element(By.ID, self.First_Name_Id).send_keys(Firstname)

    def Enter_Last_Name(self, Lastname):
        self.driver.find_element(By.ID, self.Last_Name_Id).send_keys(Lastname)

    def Enter_Gender(self, Gender):
        self.driver.find_element(By.ID, self.Gender_Id).send_keys(Gender)

    def Enter_DateOfBirth(self, DateOfBirth):
        self.driver.find_element(By.ID, self.DateOfBirth_Id).send_keys(DateOfBirth)

    def Enter_Company_name(self, CompanyName):
        self.driver.find_element(By.ID, self.Company_name_Id).send_keys(CompanyName)

    def Select_Is_Tax_Exempt(self):
        self.driver.find_element(By.ID, self.Is_Tax_Exempt_Id).click()
        time.sleep(3)

    def Select_newsletter(self, value):
        element = self.driver.find_elements(By.XPATH, self.Newsletter)
        newsletter_field = element[0]
        newsletter_field.click()
        time.sleep(3)
        if value == "Your store name":
            self.driver.find_element(By.XPATH, "//li[contains(text(), 'Your store name')]").click()

        elif value == "Test store 2":
            self.driver.find_element(By.XPATH, "//li[contains(text(), 'Test store 2')]").click()
        else:
            self.driver.find_element(By.XPATH, "//li[contains(text(), 'Your store name')]").click()

    def Select_customer_role(self, role):
        elements = self.driver.find_elements(By.XPATH, self.Newsletter)
        cursole_field = elements[1]
        cursole_field.click()
        time.sleep(3)
        if role == "Guests":
            self.driver.find_element(By.XPATH, self.Customer_Registered).click()
            time.sleep(3)
            cursole_field.click()
            self.driver.find_element(By.XPATH, self.Customer_Guests).click()
        elif role == "Administrators":
            self.driver.find_element(By.XPATH, self.Customer_Administrators).click()
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.Customer_Forum_Moderators).click()
        elif role == "Customer Registered":
            pass
        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.Customer_Vendors).click()
        else:
            self.driver.find_element(By.XPATH, self.Customer_Administrators).click()

    def Select_Manager_Vendor(self, value):
            drp_down = Select(self.driver.find_element(By.ID, self.Manager_of_Vendor_Id))
            drp_down.select_by_visible_text(value)

    def Enter_Admin_Comments(self, admincomment):
            self.driver.find_element(By.ID, self.Admin_comment).send_keys(admincomment)

    def click_Save(self):
            self.driver.find_element(By.XPATH, self.save_btn).click()