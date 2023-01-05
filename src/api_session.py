import requests


class NetoAPISession(requests.Session):
    """HTTP session - sub-class of requests.Session"""

    def __init__(self, endpoint) -> None:
        super().__init__()
        self.endpoint = endpoint


def create_session(endpoint: str, username: str, key: str) -> NetoAPISession:
    """Returns a session object with the request headers initialised"""

    s = NetoAPISession(endpoint)
    s.headers.update(
        {
            "NETOAPI_USERNAME": username,
            "NETOAPI_KEY": key,
            "NETOAPI_ACTION": None,
            "Accept": "application/json",
        }
    )
    return s
