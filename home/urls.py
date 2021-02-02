from django.urls import path,include
from home import views



urlpatterns = [
    path('',views.home,name='home'),
    path('all',views.all,name='all'),
    #path('home',views.home,name='home'),
                        ####from boiler plate
                        ####visit github to know more!
    path('register/', views.registerPage,name='registerPage'),
    path('login/', views.loginPage,name='loginPage'),
    path('logout/', views.logoutPage,name='logoutPage'),
]
