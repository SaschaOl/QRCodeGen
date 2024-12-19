from django.urls import path
from .views import show_qrcodegen, show_qrcodeview

urlpatterns = [
    path("qrcodegen/", show_qrcodegen, name = "qrcodegen"),
    path("qrcodeview/", show_qrcodeview, name = "qrcodeview")
]