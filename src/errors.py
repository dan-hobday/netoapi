import requests


def check_http_errors(response: requests.Response) -> bool:
    """Handles any http errors, else returns True"""

    try:
        response.raise_for_status()

    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return True


def check_api_errors(response: dict) -> bool:
    """Handles any api errors, else returns True"""

    if response["Ack"] == "Error":
        err = ValueError(f"The API responded with an error: {response['Messages']}")
        raise SystemExit(err)

    return True
