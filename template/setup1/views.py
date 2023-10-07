from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def servies(request):
    return render(request, 'serviec.html')