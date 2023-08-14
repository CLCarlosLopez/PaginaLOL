from django.shortcuts import render
from .models import Campeones

def Home(request):
    return render(request,"home.html")

def Campeones_list(request):
    campeones = Campeones.objects.all()
    return render(request,"campeones.html",{"campeones":campeones})

def campeon_detail(request,campeon_id):
    campeon = Campeones.objects.get(pk=campeon_id)
    return render(request,"campeon_detail.html",{"campeon":campeon})