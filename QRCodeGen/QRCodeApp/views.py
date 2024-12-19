from django.shortcuts import render

# Create your views here.
def show_qrcodegen(request):
    return render(request, "QRCodeApp/qrcodegen.html")

def show_qrcodeview(request):
    return render(request, "QRCodeApp/qrcodeview.html")