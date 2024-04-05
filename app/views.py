from django.shortcuts import render

# Create your views here.
def nanna(request):
    return render(request,'nanna.html')

def a(request):
    return render(request,'a.html')