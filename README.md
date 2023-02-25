# NetoAPI library V0.0.2
### A Python API client for the <a href="https://www.netohq.com/" target="_blank">Neto</a> (Maropost) Ecommerce platform.
</br>

## Requirements:
* Python 3.7+
* <a href="https://pypi.org/project/requests/">Requests</a>
<br><br>
## To install:
```bash
pip install git+https://github.com/dan-hobday/netoapi
```

## Basic use:
``` python
import netoapi

api = netoapi.NetoAPIClient(
    my_endpoint,
    my_username,
    my_apikey
)
payload = {
    "Filter": {
        "SKU": "LSD",
        "OutputSelector": [
            "Name",
            "RRP"
        ] 
    }
}
response = api.execute_api_call("GetItem", payload)
print(response)
```
``` bash
{
    'Item': [
        {'RRP': '150.00', 'InventoryID': '31673', 'Name': 'Luke Skywalker Doll', 'SKU': 'LSD'}
    ],
    'CurrentTime': '2021-02-06 10:49:40',
    'Ack': 'Success'
}
```

## Method - NetoAPIClient.execute_api_call():
``` python
# Parameters:
action: str """Used in the 'NETOAPI_ACTION' request header"""
payload: dict """Converted to JSON as the request payload"""

# See NETO API documentation for more information on building
# JSON payloads and available 'NETOAPI_ACTION' headers
```

## Custom exceptions:
### Raised if netoapi is imported without the requests library installed:
``` python
netoapi.errors.DependencyNotFoundError
```

### Raised if an error occurs during an API call:
``` python
netoapi.errors.NetoAPIRequestError

# Catch this error to avoid breaking execution
try:
    api.execute_api_call(action, payload)
except NetoAPIRequestError as e:
    # Handle the error
```

## timeout:
### Setting the connection and response timeout property
``` python
# The timeout property will always return a tuple (connection, response)
print(type(api.timeout))
```
``` bash
<class 'tuple'>
```
``` python
# By default the timeout property is set to (5, 5)
# timeout can be set to an integer, a tuple or NoneType

# Set both timeouts to the same value with an integer
api.timeout = 10 # 10 seconds

# Set the timeouts individually with a tuple
api.timeout = (5, 10)

# Set the connection timeout to 5 and wait forever for a response
api.timeout = (5, None)

# Cancel all time limits on connections and requests
api.timeout = None
```

### That's about all there is to it!
</br>

For more info see <a href="https://developers.maropost.com/documentation/engineers/api-documentation" target="_blank">Neto API docs</a>

Written by <a href="https://github.com/dan-hobday" target="_blank">github.com/dan-hobday</a>

### Roadmap:
* -> V0.0.2 - Current release
* -> V1.0.0 - Add the unit tests and documentation. Release on PYPI
* -> V1.1.0 - Map API fields to classes. This will make building payloads easier, less error prone and add support for field constraints.