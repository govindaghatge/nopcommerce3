from selenium.webdriver.common.by import By


class Admin_page_login:

    Admin_Username_Id = "Email"
    Admin_Password_Id = "Password"
    Submit_button_Id = "//button [@type= 'submit']"

    def __init__(self, driver):
        self.driver = driver

    def Username_ActionMethod(self, username):
        self.driver.find_element(By.ID, self.Admin_Username_Id).clear()
        self.driver.find_element(By.ID, self.Admin_Username_Id).send_keys(username)

    def Password_ActionMethod(self, password):
        self.driver.find_element(By.ID, self.Admin_Password_Id).clear()
        self.driver.find_element(By.ID, self.Admin_Password_Id).send_keys(password)

    def Submit_ActionMethod(self):
        self.driver.find_element(By.XPATH, self.Submit_button_Id).click()