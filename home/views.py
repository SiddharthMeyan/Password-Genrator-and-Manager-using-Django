from django.shortcuts import render,HttpResponse, redirect
from home.models import Password
import string,random
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required    ####login_required Decorator

def home(requests):
    
    return render(requests,'home.html')

def all(requests):
    if requests.method=="POST":
        title = requests.POST.get('title')
        website = requests.POST.get('website')
        user = requests.POST.get('user')
        myRange=requests.POST.get('myRange') 
        signs='!@#$%&()'
        ran_w=string.ascii_letters+string.digits+signs
        wpass=[]
        
        for u in range(int(myRange)):
            wpass.append(random.choice(ran_w))
        wpass=''.join(wpass)
        p={'wpass':wpass}
        if requests.user.is_authenticated:
            pass_author=requests.user
            password = Password(title=title, website=website, user=user,myRange=myRange,wpass=wpass,pass_author=pass_author)
            password.save()

            return render(requests,'all.html',p)

        else:
            return render(requests,'all.html',p)

@login_required
def view(requests):
    user_post=Password.objects.all()
    context={"user_post":user_post}
    return render(requests,'view.html',context)


def registerPage(request):
    form=CreateUserForm()                         #setting form variable as function CreateUserForm

    if request.method=="POST":
        form=CreateUserForm(request.POST)         #putting value of filled CreateUserForm in form
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)


            return redirect('loginPage')


    context={'form':form}                           #sending for as context
    return render(request,"register.html",context)


#from login/register boiler plate
#visit github to know more
def loginPage(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is incorrect')

    return render(request,"login.html")


def logoutPage(request):
    logout(request)
    return redirect('loginPage')


@login_required
def profilePage(request):
    log_user=request.user
    user_post=Password.objects.filter(pass_author=log_user)
    
    return render(request,'profile.html',{"user_post":user_post})
    