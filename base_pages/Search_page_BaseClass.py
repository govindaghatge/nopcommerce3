from selenium.webdriver.common.by import By


class Search_Customer:

    Email_Id = "SearchEmail"
    First_name_Id = "SearchFirstName"
    Last_name_Id = "SearchLastName"
    Company_Id = "SearchCompany"
    Search_Id = "search-customers"

    rows_table_xpath = "//table[@id='customers-grid']/tbody//tr"
    columns_table_xpath = "//table[@id='customers-grid']/tbody//tr/td"

    def __init__(self, driver):
        self.driver = driver

    def Enter_Email(self, Email):
        self.driver.find_element(By.ID, self.Email_Id).send_keys(Email)


    def Enter_firstName(self, FirstName):
        self.driver.find_element(By.ID, self.First_name_Id).send_keys(FirstName)

    def Enter_LastName(self, LastName):
        self.driver.find_element(By.ID, self.Last_name_Id).send_keys(LastName)

    def Enter_CompanyName(self, CompanyName):
        self.driver.find_element(By.ID, self.Company_Id).send_keys(CompanyName)

    def Click_Searchbutton(self):
        self.driver.find_element(By.ID, self.Search_Id).click()

    def get_result_table_row(self):
        return len(self.driver.find_elements(By.XPATH, self.rows_table_xpath))

    def get_results_table_cols(self):
        return len(self.driver.find_elements(By.XPATH, self.rows_table_xpath))

    def search_customer_by_email(self, email):
        email_present_flag = False
        for r in range(1, self.get_result_table_row()+1):
            cus_email = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']/tbody//tr["+str(r)+"]/td[2]").text

            if cus_email == email:
                email_present_flag = True
                break
        return email_present_flag

    def search_customer_by_name(self, FirstName):
        email_present_flag = False
        for r in range(1, self.get_result_table_row()+1):
            cus_email = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']/tbody//tr["+str(r)+"]/td[3]").text

            if cus_email == FirstName:
                email_present_flag = True
                break
        return email_present_flag

    def search_customer_by_company(self, companyname):
        email_present_flag = False
        for r in range(1, self.get_result_table_row()+1):
            cus_email = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']/tbody//tr["+str(r)+"]/td[5]").text

            if cus_email == companyname:
                email_present_flag = True
                break
        return email_present_flag
