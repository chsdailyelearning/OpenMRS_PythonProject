import configparser
config=configparser.RawConfigParser()
config.read("C:\\Users\\chand\\PycharmProjects\\OpenMRS_PythonProject\\Configuration\\config.ini")

class ReadConfig():

    @staticmethod
    def getAppUrl():
        url = config.get("Environmnet details","url")
        return url

    @staticmethod
    def getAppUserName():
        userName = config.get("Environmnet details", "userName")
        return userName

    @staticmethod
    def getAppPassword():
        password = config.get("Environmnet details", "password")
        return password