from django.shortcuts import render
from django.http import HttpResponse
result=[]
def index(request):
    if request.method=="POST":
        n = int(request.POST.get("num"))
        f=1
        for i in range(1,n+1):
            f=f*i
        return render(request,"factapp/factorial.html",{"key":"result is "+str(f)})
    else:
        return render(request,"factapp/factorial.html")

def table(request):
    if request.method=="POST":
        num = int(request.POST.get("txtnum"))
        lst=[]
        if request.POST.get("btnsubmit1")!=None:
           for i in range(1,11):
                lst.append(num*i)
        else:
            for i in range(11,1,-1):
                lst.append(num*i)
        return render(request,"factapp/table.html",{"key":lst})

    else:
        return render(request,"factapp/table.html")
def squarecube(request):
    if request.method=="POST":
        num = int(request.POST.get("txtnum"))
        result=''
        if request.POST.get("btnsquare")!=None:
            result = num*num
        else:
            result = num*num*num
        return render(request,"factapp/square_cube.html",{"data1":num,"key":result})

    else:
        return render(request,"factapp/square_cube.html")

def calc(request):
    global result
    if request.method=="POST":
        try:
         num1 = int(request.POST.get('num1'))
         num2 = int(request.POST.get('num2'))
        
         if request.POST.get('btnsubmit1')!=None:
            num=num1+num2
            result.append("+ " + str(num)) 
         elif request.POST.get('btnsubmit2')!=None:
            num=num1-num2
            result.append("- " + str(num)) 
         elif request.POST.get('btnsubmit3')!=None:
            num=num1*num2
            result.append("* " + str(num)) 
         elif request.POST.get('btnsubmit4')!=None:
             num=num1/num2
             result.append("/ " + str(num)) 
         elif request.POST.get('btnsubmit5')!=None:
             if len(result)>0:
                result.clear()
         return render(request,"factapp/calc.html",{"data1":num1,"data2":num2,"key":result})
        except Exception:
            return HttpResponse("enter correct data")
    else:
        return render(request,"factapp/calc.html")