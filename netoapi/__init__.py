#     _   __     __        ___    ____  ____
#    / | / /__  / /_____  /   |  / __ \/  _/
#   /  |/ / _ \/ __/ __ \/ /| | / /_/ // /
#  / /|  /  __/ /_/ /_/ / ___ |/ ____// /
# /_/ |_/\___/\__/\____/_/  |_/_/   /___/

"""
NetoAPI Library
----------------------

A Python3 API Client for the Neto (Maropost) Ecommerce platform

Basic Get usage:

    >>> api = netoapi.NetoAPIClient(
    >>>     endpoint,
    >>>     username,
    >>>     apikey
    >>> )
    >>> payload = {
    >>>     "Filter": {
    >>>         "SKU": "LSD",
    >>>         "OutputSelector": [
    >>>             "Name",
    >>>             "RRP"
    >>>         ] 
    >>>     }
    >>> }
    >>> response = api.execute_api_call("GetItem", payload)
    >>> print(response)
    {
      'Item': [{'RRP': '150.00', 'InventoryID': '31673', 'Name': 'Luke Skywalker Doll', 'SKU': 'LSD'}],
      'CurrentTime': '2021-02-06 10:49:40',
      'Ack': 'Success'
    }
"""

import sys

if sys.version_info < (3, 7):
    raise Warning(
        f"NetoAPI supports Python3.7 or greater. You are on V{sys.version_info.major}.{sys.version_info.minor}"
    )

import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())

import errors

try:
    import requests
except:
    raise errors.DependencyNotFoundError(
        "NetoAPI requires the requests library. Use: pip install requests"
    ) from None

from .api_client import NetoAPIClient

__all__ = [NetoAPIClient, errors]
