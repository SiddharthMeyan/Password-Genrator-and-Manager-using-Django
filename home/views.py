from django.shortcuts import render,HttpResponse
from home.models import Password



def home(requests):
    
    return render(requests,'home.html')

def all(requests):
    if requests.method=="POST":
        title = requests.POST.get('title')
        website = requests.POST.get('website')
        user = requests.POST.get('user')
        myRange=requests.POST.get('myRange')
        password = Password(title=title, website=website, user=user,myRange=myRange)
        password.save()
    return render(requests,'all.html')