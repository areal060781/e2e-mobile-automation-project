import requests


class ZS4JResponseException(Exception):
    """
    Class to represent unsuccessful ZS4J API operations
    """

    def __init__(self, message):
        self.message = message


def check_zs4j_api_response(response: requests.models.Response, expected_status_code: int = 201) -> None:
    """
    Checking response from ZS4J API

    :param response: requests response object
    :type response: requests.models.Response

    :param expected_status_code: expected response status code, 201 by default
    :type expected_status_code: int

    :raise ZS4JResponseException: raised if actual response status code doesn't match to expected

    :return: None
    :rtype: None
    """
    try:
        assert response.status_code == expected_status_code
    except AssertionError:
        raise ZS4JResponseException(f"Response status code: {response.status_code}, response message: {response.text}")

    return None
