from django.urls import path
from . import views

urlpatterns = [        
    path('createaccount/', views.createaccount, name='createaccount'),
   # path('logout/', views.logoutaccount, name='logoutaccount'),
   # path('login/', views.loginaccount, name='loginaccount'),
]
