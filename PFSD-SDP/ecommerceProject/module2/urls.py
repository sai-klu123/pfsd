from django.urls import path, include

from . import admin
from.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', mainpagecall, name='mainpagecall'),
    path('signup/', signupcall, name='signupcall'),
    path('h1/',navbarcall,name='navbarcall'),
    path('print2/',registerloginfunction,name='registerloginfunction'),
    path('print3/',navbar2call,name='navbar2call'),
    path('login1/',logincall,name='logincall'),
    path('authenticate_user/', authenticate_user, name='authenticate_user'),
    path('about/', aboutcall,name='aboutcall'),
    path('service/',servicecall,name='servicecall'),
    path('team/',teamcall,name='teamcall'),
    path('contactus/',contactcall,name='contactcall'),
    path('contactfunction',feedbackformfunction,name='feedbackformfunction'),
    path('adminPage/',admincall,name='admincall'),
    path('show/', show_user, name='show_user'),
    path('show_users/', show_users, name='show_users'),
    path('remove_user/<str:pk>/', remove_user, name='remove_user'),
    path('',send_welcome_email,name='send_welcome_email'),
    path('',send_removed_user_email,name='send_removed_user_email'),
    path('add/',add_user,name='add_user'),

]
