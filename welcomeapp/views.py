from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

def index(request):
    return HttpResponse('welcome in second app')

def swap(request):
    a,b=10,20
    a,b=b,a
    return HttpResponse("a={0} and b={1}".format(a,b))
class SIView(View):
    
    def get(self,request):
        return render(request,"welcomeapp/si.html")
    def post(self,request):
        p=request.POST.get("txtp")
        r=request.POST.get("txtr")
        t=request.POST.get("txtt")
        res = (float(p)*float(r)*float(t))/100
        return render(request,"welcomeapp/si.html",{"key":res})
class Calc(View):
    result=[]
    def post(self,request):
        try:
         num1 = int(request.POST.get('num1'))
         num2 = int(request.POST.get('num2'))
        
         if request.POST.get('btnsubmit1')!=None:
            num=num1+num2
            self.result.append("+ " + str(num)) 
         elif request.POST.get('btnsubmit2')!=None:
            num=num1-num2
            self.result.append("- " + str(num)) 
         elif request.POST.get('btnsubmit3')!=None:
            num=num1*num2
            self.result.append("* " + str(num)) 
         elif request.POST.get('btnsubmit4')!=None:
             num=num1/num2
             self.result.append("/ " + str(num)) 
         elif request.POST.get('btnsubmit5')!=None:
             if len(self.result)>0:
                self.result.clear()
         return render(request,"factapp/calc.html",{"data1":num1,"data2":num2,"key":self.result})
        except Exception:
            return HttpResponse("enter correct data")
    def get(self,request):
        return render(request,"factapp/calc.html")