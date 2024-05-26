from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from apps.destinations.models import Destination
from apps.accounts.models import Account
from apps.api.v1.destinations.serializers import DestinationSerializer


class DestinationListCreate(ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        account_id = serializer.validated_data.get("account", {}).get("account_id", None)
        account = get_object_or_404(Account, account_id=account_id)
        instance = serializer.save(account=account)
        headers = self.get_success_headers(serializer.data)
        return Response(self.get_serializer(instance).data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        destination_id = self.request.GET.get("id")
        account_id = self.request.GET.get("account_id")

        if destination_id:
            return Destination.objects.filter(id=destination_id)
        if account_id:
            account = Account.objects.get(account_id=account_id)
            return account.destinations.all()
        return Destination.objects.all()
