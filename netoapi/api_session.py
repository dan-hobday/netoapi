from typing import Any
from abc import ABC, abstractmethod

import requests


class NetoAPISession(ABC):
    """Abstract interface for API connection sessions"""

    @abstractmethod
    def auth_session():
        pass

    @abstractmethod
    def send_request():
        pass


class RequestsAPISession(NetoAPISession, requests.Session):
    """A HTTP session which sub-classes requests.Session"""

    def __init__(self) -> None:
        super().__init__()

    def auth_session(self, username: str, key: str) -> None:
        """Sets the authentication headers to be sent with API requests.
        These headers persist between requests."""
        self.headers = {
            "NETOAPI_USERNAME": username,
            "NETOAPI_KEY": key,
            "Accept": "application/json",
        }

    def send_request(self, **kwargs) -> requests.Response:
        """Sends the HTTP post request to the API. The 'NETOAPI_ACTION'
        header is appended to the session headers but does not persist
        between requests."""
        return self.post(**kwargs)


def get_api_session():
    return RequestsAPISession()
