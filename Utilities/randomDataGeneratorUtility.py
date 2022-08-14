import random
import string


class randomUtil():

    @staticmethod
    def randomName():
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(5))
        return name

    @staticmethod
    def randomDate():
        date = random.randint(1, 30)
        return date

    @staticmethod
    def randomMonth():
        month = random.randint(1, 12)
        return month

    @staticmethod
    def randomYear():
        year = random.randint(1995, 2021)
        return year

    @staticmethod
    def randomPhoneNumber():
        phoneNumber = random.randint(1111111111, 9999999999)
        return phoneNumber