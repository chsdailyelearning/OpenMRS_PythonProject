from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageObjects.loginPage import login
from Utilities.readProperties import ReadConfig

class Test_001_login:
    driverPath = Service("C:\\Users\\chand\\PycharmProjects\\OpenMRS_PythonProject\\Utilities\\chromedriver.exe")
    driver = webdriver.Chrome(service=driverPath)
    url = ReadConfig.getAppUrl()
    userName = ReadConfig.getAppUserName()
    password = ReadConfig.getAppPassword()

    def test_loginPage(self):
        self.driver.get(self.url)
        self.driver.save_screenshot("C:\\Users\\chand\\PycharmProjects\\OpenMRS_PythonProject\\Screenshots\\loginPage.png")

    def test_loginCheck(self):
        self.driver.get(self.url)
        self.lp = login(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLocation()
        self.lp.clickLoginBtn()
        self.driver.save_screenshot("C:\\Users\\chand\\PycharmProjects\\OpenMRS_PythonProject\\Screenshots\\logincheck.png")
        self.lp.clickLogoutLink()
