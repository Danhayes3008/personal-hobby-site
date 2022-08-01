from django.shortcuts import render

# Create your views here.
def Electronics(request):
    return render(request, 'Electronics.html')