class ZS4JConfigurationException(Exception):
    """
    Class to represent ZS4J configuration exceptions
    """

    def __init__(self, message):
        self.message = message
