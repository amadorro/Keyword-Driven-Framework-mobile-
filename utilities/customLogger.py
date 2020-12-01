import logging

class LogGen:
    @staticmethod
    def loggen():
        # specify where to generate the logging
        logging.basicConfig(filename="./Logs/automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        # create a variable
        logger = logging.getLogger()
        # set level
        logger.setLevel(logging.INFO)
        return logger
