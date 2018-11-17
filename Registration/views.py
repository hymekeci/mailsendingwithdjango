from django.shortcuts import render

# Create your views here.

def RegPage(request):

    return  render(request, 'reg.html')

def create_regis (request):
    return render(request, 'Forms.html', 'form':form)