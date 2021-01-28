from django.shortcuts import render,HttpResponse
from home.models import Password
import string,random


def home(requests):
    
    return render(requests,'home.html')

def all(requests):
    if requests.method=="POST":
        title = requests.POST.get('title')
        website = requests.POST.get('website')
        user = requests.POST.get('user')
        myRange=requests.POST.get('myRange')
        ran_w=string.ascii_letters+string.digits
        wpass=[]
        for u in range(int(myRange)):
            wpass.append(random.choice(ran_w))
        wpass=''.join(wpass)
        p={'wpass':wpass}
        password = Password(title=title, website=website, user=user,myRange=myRange,wpass=wpass)
        password.save()

    return render(requests,'all.html',p)


def login(requests):

    return render(requests,'login.html')