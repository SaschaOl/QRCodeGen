from django.shortcuts import render

# Create your views here.
def show_auth(request):
    return render(request, "UserApp/auth.html")

def show_reg(request):
    return render(request, "UserApp/reg.html")