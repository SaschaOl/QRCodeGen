from django.shortcuts import render

# Create your views here.
def show_subsription_app(request):
    return render(request, "SubscriptionApp/subscription.html")
