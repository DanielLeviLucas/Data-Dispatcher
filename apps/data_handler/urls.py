from django.urls import path

from apps.data_handler.views import DataHandlerView

app_name = "data_handler"

urlpatterns = [
    path("", DataHandlerView.as_view(), name="handler"),
]
