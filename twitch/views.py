from django.shortcuts import render

# Create your views here.
def Twitch(request):
    return render(request, 'Twitch.html')