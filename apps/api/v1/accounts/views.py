from django.db import transaction

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.accounts.models import Account
from apps.api.v1.accounts.serializers import AccountSerializer


class AccountListCreate(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
