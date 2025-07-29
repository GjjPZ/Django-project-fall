from django.shortcuts import render
def index(request):
    """Домашняя страница приложения Learning Log"""
    return render(request, 'Learning_logs/index.html')

# Create your views here.
