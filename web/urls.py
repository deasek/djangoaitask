from django.urls import path

from .views import AddTextView, SummaryDetailView

app_name = "web"


urlpatterns = (
    path("", AddTextView.as_view(), name="index"),
    path("<uuid:pk>", SummaryDetailView.as_view(), name="summary-view"),
)
