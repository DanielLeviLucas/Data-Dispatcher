import json

from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from apps.accounts.models import Account
from apps.domain.broadcast_data import broadcast_data


@method_decorator(csrf_exempt, name="dispatch")
class DataHandlerView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {"message": "Invalid Data"}, status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)

        app_secret_token = self.request.headers.get("Cl-X-Token")
        if not app_secret_token:
            return JsonResponse(
                {"message": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED
            )

        account = Account.objects.filter(app_secret_token=app_secret_token)
        if not account:
            return JsonResponse(
                {"message": "No matching account found"}, status=status.HTTP_400_BAD_REQUEST
            )

        response = broadcast_data(account[0], data)
        return  response
