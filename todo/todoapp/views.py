from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from todoapp.models import Task,Course
from todoapp.form import EmpRegister,CourseForm
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
def home(request):

    #return HttpResponse("Hello Home Page")
    #return redirect("/contact")

    #passing data as dictionary to home.html 
    d={'id':1,'name':'Itvedant','rno':35}
    return render(request,'home.html',d)

def contact(request):

    data="hello,This is Contact Page"
    #return HttpResponse(data)
    return render(request,'contact.html')


def product(request):
    d="<h1><b>Hello</b> this is product page</h1>"
    #return HttpResponse(d)
    return render(request,'product.html')


"""
Retriving request parameter in the views function 
"""
def edit(request,rid):
    '''
        data="Id to be edited is:"+rid
        return HttpResponse(data)
    '''

    if request.method=='POST':
        ut=request.POST['t']
        udet=request.POST['det']
        udt=request.POST['dt']
        #print(ut)
        #print(udet)
        #print(udt)
        x=Task.objects.filter(id=rid)
        x.update(title=ut,details=udet,date=udt)
        return redirect('/')

    else:
        content={}
        content['data']=Task.objects.filter(id=rid)
        return render(request,'editform.html',content)

def delete(request,rid):
        #data="Id to be deleted is:"+rid
        #return HttpResponse(data)
        '''
        #Hard Delete
        x=Task.objects.get(id=rid)
        x.delete()
        return redirect('/')
        '''
        x=Task.objects.filter(id=rid)
        x.update(is_deleted='Y')
        return redirect('/')

'''
check evenodd and result in template
'''
def evenodd(request,n):
    r=int(n)%2
    d={'res':r}
    return render(request,'home.html',d)

'''
Template looping
'''
def loop(request):
    d={
        'l':[10,20,30,40,50,60]
    }
    return render(request,'home.html',d)

def about(request):
    return render(request,'about.html')


def index(request):

    content={}
    #content['data']=Task.objects.all()
    #print(content['data'])
    content['data']=Task.objects.filter(is_deleted='N')

    return render(request,'index.html',content)


def create_task(request):
    #return HttpResponse('In create a task function')
    
    if request.method=='POST':
        #retrive and Store in database
        t=request.POST['t']
        det=request.POST['det']
        dt=request.POST['dt']
        #print(t)
        #print(det)
        #print(dt)
        #return HttpResponse('retrive and Store in database')
        t1=Task.objects.create(title=t,details=det,date=dt,is_deleted='N')
        #print(t1)
        t1.save()
        return redirect('/')
    else:
        #show blank form
        return render(request,'create_task.html')

def cdashboard(request):
    content={}
    
    #content['data']=Course.objects.all()
    #content['data']=Course.cobj.all() #changing default manager name
    #content['data']=Course.ccustomobj.all() #custom class object
    
    #content['data']=Course.ccustomobj.sortfeeshightolowdev()
    #content['data']=Course.ccustomobj.sortfeeshightolowds()

    #content['data']=Course.ccustomobj.sortfeeslowtohighdev()
    content['data']=Course.ccustomobj.sortfeeslowtohighds()

    #content['data']=Course.objects.filter(ccat='Developement')
    #content['data']=Course.objects.filter(ccat='Data Science')
    #>=django: coloumname__gt=value or member__gt=value
    #content['data']=Course.objects.filter(cprice__gt=20000)
    #content['data']=Course.objects.filter(cprice__gte=20000)
    #<=django: coloumname__lt=value or member__lt=value
    #content['data']=Course.objects.filter(cprice__lt=20000)
    #content['data']=Course.objects.filter(cprice__lte=20000)
    '''
    Q.1) category is data science and cprice is>=20000
    '''
    #content['data']=Course.objects.filter(ccat='Data Science',cprice__gte=20000)
    '''
    Q()
    classname=Q
    Q(): Query object encapsulate or wrapped sql expression that can be used as Python object.
    '''
    #Q1=Q(ccat='Data Science')
    #Q2=Q(cprice__gte=20000)
    #content['data']=Course.objects.filter(Q1&Q2)

    #Q1=Q(cdur=40)
    #Q2=Q(cdur=50)
    #Q3=Q(cdur=20)
    #content['data']=Course.objects.filter(Q1|Q2|Q3) # | is a or operator
    '''
    sorting:
    order_by(data member or coloumnname) its by default in ascending order
    order_by(-data member or -coloumnname)

    '''
    #content['data']=Course.objects.order_by('cdur') # for ascending oredr
    #content['data']=Course.objects.order_by('-cdur') # for Decending order
    #content['data']=Course.objects.order_by('cprice')
    #content['data']=Course.objects.order_by('-cprice')
    
    # filter & sorting together
    #content['data']=Course.objects.order_by('cprice').filter(ccat='Data Science')

    return render(request,'dashboard.html',content)

def lowtohigh(request):
    content={}
    content['data']=Course.objects.order_by('cprice')
    #content['data']=Course.ccustomobj.sortfeeslowtohighdev()
    #content['data']=Course.ccustomobj.sortfeeslowtohighds()
    
    return render(request,'dashboard.html',content)

def hightolow(request):
    content={}
    content['data']=Course.objects.order_by('-cprice')
    #content['data']=Course.ccustomobj.sortfeeshightolowdev()
    #content['data']=Course.ccustomobj.sortfeeshightolowds()
    
    return render(request,'dashboard.html',content)


def showform(request):
    
    fobj=EmpRegister() #create object of form class
    content={}
    content['form']=fobj
    return render(request,'empregister.html',content)


def showmodelform(request):

    mfobj=CourseForm() #Creating Modelform Object
    content={}
    content['form']=mfobj
    return render(request,'createcourse.html',content)



class MyView(View):

    def get(self,request):

        return HttpResponse("Hello from MyView with GET Request")

    def post(self,request):
        return HttpResponse("Hello from MyView with POST Request")


'''
def register(request):

    if request.method=='POST':
        uname=request.POST['username']
        pass1=request.POST['password1']
        #print(uname)
        #print(pass1)
        u1=User(username=uname,password=pass1,is_staff=True,is_active=True)
        u1.save()
        return redirect('/register')
    
    else:
        fm=UserCreationForm()
        return render(request,'signup.html',{'form':fm})
'''
def register(request):

    if request.method=='POST':
        fm=UserCreationForm(request.POST)
        #print(fm)
        print(fm.is_valid())
        
        if fm.is_valid():
            fm.save()
        
        return redirect('/register')
    
    else:
        fm=UserCreationForm()
        return render(request,'signup.html',{'form':fm})




