from django.urls import path
from apps.api.views import SearchInfo
urlpatterns = [
    path("profile-card/", SearchInfo.as_view(), name="get-cars",)
]
