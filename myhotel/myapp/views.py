from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import myapp

def booking(request):
    return render(request,'booking.html')

def index1(request):
    return render(request,'home.html')


def login(request):
    return render(request,'index.html')

def auth(request):
    if request.method== "POST":
        email=request.POST.get('email')
        pwd=request.POST.get('pass')
        if email=="aaa@gmail.com" and pwd=="123":
            return render(request,"booking.html")
    return HttpResponse("err")

def index(request):
    data = myapp.objects.all().values()
    template = loader.get_template('junu_index.html')
    context = {
    'data': data,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    return render(request,'booking.html')

def addrecord(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    mobile=request.POST['mobile']
    num=request.POST['num']
    rtype=request.POST['rtype']
    date=request.POST['date']

    add=myapp(fname=fname,lname=lname, email=email, mobile=mobile, num=num, rtype=rtype, date=date)
    add.save()
    print("added succesfully")
    return render(request,"home.html")

def update(request,emp_id):
    data = myapp.objects.get(emp_id=emp_id)
    template = loader.get_template('update.html')
    context = {
    'data': data,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request,emp_id):
    nm,em=request.POST['name'],request.POST['email']
    data = myapp.objects.get(emp_id=emp_id)
    data.name = nm
    data.email = em
    data.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request,emp_id):
    getdata =myapp.objects.get(emp_id=emp_id)
    getdata.delete()
    return HttpResponseRedirect(reverse('index'))