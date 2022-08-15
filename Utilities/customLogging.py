import logging

class LogGen:

    @staticmethod
    def log():
        logger = logging.getLogger()
        logFile = logging.FileHandler("C:\\Users\\chand\\PycharmProjects\\OpenMRS_PythonProject\\Logs\\CustomReport.log")
        format=logging.Formatter('%(asctime)s %(message)s')
        logFile.setFormatter(format)
        logger.addHandler(logFile)
        logger.setLevel(logging.INFO)
        return logger