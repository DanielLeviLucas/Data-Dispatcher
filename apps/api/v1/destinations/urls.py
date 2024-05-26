from django.urls import path

from apps.api.v1.destinations.views import DestinationListCreate, DestinationUpdateView

app_name = "destinations"

urlpatterns = [
    path("", DestinationListCreate.as_view(), name="list_create"),
    path("<int:pk>/update/", DestinationUpdateView.as_view(), name="update"),
]
