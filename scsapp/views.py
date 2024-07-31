from django.shortcuts import render

def home(request):
    return render(request,"scsapp/home.html")

def aboutus(request):
    return render(request,"scsapp/aboutus.html")

def gallery(request):
    return render(request,"scsapp/gallery.html")

def contactus(request):
    return render(request,"scsapp/contactus.html")

def services(request):
    return render(request,"scsapp/services.html")
