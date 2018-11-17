from django.shortcuts import render

# Create your views here.

def SendPage(request):
    return render(request, 'send.html')