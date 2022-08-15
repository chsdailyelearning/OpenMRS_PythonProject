from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class regPatient:

    link_registerPatient_id="referenceapplication-registrationapp-registerPatient-homepageLink-referenceapplication-registrationapp-registerPatient-homepageLink-extension"
    tb_given_xpath="//fieldset[@id='demographics-name']/div[1]/p[1]/input"
    tb_familyName_name="familyName"
    btn_next_id="next-button"
    select_gender_id="gender-field"
    tb_day_id="birthdateDay-field"
    select_month_id="birthdateMonth-field"
    tb_year_id="birthdateYear-field"
    tb_address1_id="address1"
    tb_phoneNumber_name="phoneNumber"
    btn_submit_id="submi"
    link_logout_xpath="//div[@id='navbarSupportedContent']/ul/li[3]/a/i"

    def __init__(self, driver):
        self.driver = driver

    def clickRegPatient(self):
        self.driver.find_element(By.ID, self.link_registerPatient_id).click()

    def setGiven(self,givenName):
        self.driver.find_element(By.XPATH,self.tb_given_xpath).send_keys(givenName)

    def setFamilyName(self,FamilyName):
        self.driver.find_element(By.NAME,self.tb_familyName_name).send_keys(FamilyName)

    def clickNextBtn(self):
        self.driver.find_element(By.ID,self.btn_next_id).click()

    def selectGen(self):
        gender= Select(self.driver.find_element(By.ID,self.select_gender_id)).select_by_value("M")

    def setDay(self,date):
        self.driver.find_element(By.ID, self.tb_day_id).send_keys(date)

    def selectMonth(self):
        month= Select(self.driver.find_element(By.ID,self.select_month_id)).select_by_value("1")

    def setYear(self,year):
        self.driver.find_element(By.ID,self.tb_year_id).send_keys(year)

    def setAddress1(self):
        self.driver.find_element(By.ID,self.tb_address1_id).send_keys("44 Mangalore - 571212")

    def setPhoneNumber(self,phone):
        self.driver.find_element(By.NAME,self.tb_phoneNumber_name).send_keys(phone)

    def clickSubmit(self):
        self.driver.find_element(By.ID,self.btn_submit_id).click()

    def clickLogoutLink(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()
