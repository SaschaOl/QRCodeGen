from django.urls import path
from .views import show_auth, show_reg

urlpatterns = [
    path("auth/", show_auth, name = "auth"),
    path("reg/", show_reg, name = "reg")
]