from django.http import JsonResponse
from rest_framework import status
import requests


def broadcast_data(account, data):
    for destination in account.destinations.all():
        try:
            response = send_data(destination, data)
            print(response.status_code)
            response.raise_for_status()
        except requests.RequestException as err:
            return JsonResponse({'error': str(err)}, status=response.status_code)
        except HttpMethodNotImplemented as err:
            return JsonResponse({'error': str(err)}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return JsonResponse({"message": "Data broadcasted successfully to destinations"}, status=status.HTTP_200_OK)


def send_data(destination, data):
    url = destination.url.rstrip("/")
    headers = destination.headers
    http_method = destination.http_method.upper()

    if http_method == 'GET':
        response = requests.get(url, params={"data": data}, headers=headers)
    elif http_method == 'POST':
        response = requests.post(url, json=data, headers=headers)
    elif http_method == 'PUT':
        response = requests.put(url, json=data, headers=headers)
    else:
        raise HttpMethodNotImplemented(http_method)
    return response


class HttpMethodNotImplemented(Exception):
    def __init__(self, method):
        self.method = method
        super().__init__(f"HTTP method '{method}' is not implemented.")
