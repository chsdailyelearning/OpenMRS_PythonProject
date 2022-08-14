import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from Utilities.readProperties import ReadConfig
from pageObjects.loginPage import login
from pageObjects.registerPatientPage import regPatient
from Utilities.excelUtility import excel
from Utilities.randomDataGeneratorUtility import randomUtil


class Test_080_regPatient:
    driverPath = Service("C:\\Users\\chand\\PycharmProjects\\OpenMRS_PythonProject\\Utilities\\chromedriver.exe")
    driver = webdriver.Chrome(service=driverPath)
    url = ReadConfig.getAppUrl()
    userName = ReadConfig.getAppUserName()
    password = ReadConfig.getAppPassword()
    givenName=randomUtil.randomName()
    familyName=randomUtil.randomName()
    phoneNumber=randomUtil.randomPhoneNumber()

    def test_validatePatientRegistration(self):
        try:
            self.driver.get(self.url)
            self.lp = login(self.driver)
            self.lp.setUserName(self.userName)
            self.lp.setPassword(self.password)
            self.lp.clickLocation()
            self.lp.clickLoginBtn()
            self.rp=regPatient(self.driver)
            self.rp.clickRegPatient()
            #self.rp.setGiven(excel.getDataFromExcel(1,1))
            #self.rp.setFamilyName(excel.getDataFromExcel(1,2))
            self.rp.setGiven(self.givenName)
            self.rp.setFamilyName(self.familyName)
            excel.setDataToExcel(1,1,self.givenName)
            excel.setDataToExcel(1,2,self.familyName)
            self.rp.clickNextBtn()
            self.rp.selectGen()
            self.rp.clickNextBtn()
            self.rp.setDay(randomUtil.randomDate())
            self.rp.selectMonth()
            self.rp.setYear(randomUtil.randomYear())
            self.rp.clickNextBtn()
            self.rp.setAddress1()
            self.rp.clickNextBtn()
            self.rp.setPhoneNumber(self.phoneNumber)
            excel.setDataToExcel(1,3,self.phoneNumber)
            self.rp.clickNextBtn()
            self.rp.clickNextBtn()
            self.rp.clickSubmit()
            time.sleep(10)
        except Exception as exceptionMessage:
            print("====>You have not given proper xpath or id or soon<===="+str(exceptionMessage))
        finally:
            self.rp.clickLogoutLink()
