from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('all',views.all,name='all'),
                        ####from boiler plate
                        ####visit github to know more!
    path('register/', views.registerPage,name='registerPage'),
    path('login/', views.loginPage,name='loginPage'),
    path('logout/', views.logoutPage,name='logoutPage'),
    path('profile/', views.profilePage, name='profilePage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
