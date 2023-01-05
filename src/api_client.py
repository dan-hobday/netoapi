from .api_call import NetoAPICall
from .api_session import create_session
from .errors import check_api_errors, check_http_errors


class NetoAPIClient:
    """Neto API client for making API calls"""

    def __init__(self, endpoint: str, username: str, key: str) -> None:
        self.session = create_session(endpoint, username, key)

    def execute_api_call(self, apicall: NetoAPICall) -> dict:
        """Execute an api call and return the JSON response"""

        if not isinstance(apicall, NetoAPICall):
            err = f"'{type(apicall)}' object is not type <class 'netoapi.NetoAPICall'>'"
            raise TypeError(err)

        self.session.headers["NETOAPI_ACTION"] = apicall.action

        response = self.session.post(
            self.session.endpoint,
            json=apicall.payload,
        )

        # Reset headers
        self.session.headers["NETOAPI_ACTION"] = None

        assert check_http_errors(response) and check_api_errors(response.json())

        return response.json()
