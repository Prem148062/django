from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def home(request):
    #   เพิ่มที่ setting  'app_general.apps.AppGeneralConfig'
    return render(request,"app_general/home.html")

def about(request):
    return render(request,"app_general/about.html")
