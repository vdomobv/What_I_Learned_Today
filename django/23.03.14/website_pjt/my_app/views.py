from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, 'my_app/main.html')

def profile(request):
    return render(request, 'my_app/profile.html')
