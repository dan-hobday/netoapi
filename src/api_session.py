import requests
from dataclasses import dataclass, asdict


@dataclass
class NetoAPIHeaders:
    """Definition for API request headers objects"""

    NETOAPI_USERNAME: str
    NETOAPI_KEY: str
    NETOAPI_ACTION: str
    Accept: str


class NetoAPISession(requests.Session):
    """HTTP session - sub-class of requests.Session"""

    def __init__(self) -> None:
        super().__init__()
        pass


def create_session(username: str, key: str) -> NetoAPISession:
    """Returns a session object with the request headers initialised"""

    s = NetoAPISession()
    s.headers.update(
        asdict(
            NetoAPIHeaders(
                NETOAPI_USERNAME=username,
                NETOAPI_KEY=key,
                NETOAPI_ACTION=None,
                Accept="application/json",
            )
        )
    )
    return s
