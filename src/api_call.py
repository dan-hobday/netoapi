from dataclasses import dataclass


@dataclass
class NetoAPICall:
    """Definition of NetoAPICall type"""

    action: str
    payload: dict
