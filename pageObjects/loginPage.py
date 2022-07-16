from selenium import webdriver
from selenium.webdriver.common.by import By


class login:
    textbox_username_id="username"
    textbox_password_xpath="//input[@type='password']"
    button_location_id="Isolation Ward"
    button_login_id="loginButton"
    link_logout_xpath="//div[@id='navbarSupportedContent']/ul[1]/li[3]/a"


    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,userName):
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(userName)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def clickLocation(self):
        self.driver.find_element(By.ID,self.button_location_id).click()

    def clickLoginBtn(self):
        self.driver.find_element(By.ID,self.button_login_id).click()

    def clickLogoutLink(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()

