import requests
from .api_call import NetoAPICall
from .api_session import create_session


def validate_response(response: requests.Response) -> bool:
    """Handles any response errors, else returns True"""

    # Check for http errors
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    # Check for errors from the API
    json = response.json()
    if json["Ack"] == "Error":
        err = ValueError(f"The API responded with an error: {json['Messages']}")
        raise SystemExit(err)

    return True


class NetoAPIClient:
    """Neto API client for making API calls"""

    def __init__(self, endpoint: str, username: str, key: str) -> None:
        self.endpoint = endpoint
        self.session = create_session(username, key)

    def execute_api_call(self, apicall: NetoAPICall) -> dict:
        """Execute an api call and return the JSON response"""

        if not isinstance(apicall, NetoAPICall):
            err = f"'{type(apicall)}' object is not type <class 'netoapi.NetoAPICall'>'"
            raise TypeError(err)

        self.session.headers["NETOAPI_ACTION"] = apicall.action

        response = self.session.post(
            self.endpoint,
            json=apicall.payload,
        )
        validate_response(response)

        # Reset headers
        self.session.headers["NETOAPI_ACTION"] = None

        return response.json()
