from django.shortcuts import render

def Home(request):
    return render(request,"home.html")

def Campeones(request):
    return render(request,"campeones.html")