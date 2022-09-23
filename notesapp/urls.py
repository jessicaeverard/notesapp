"""notesapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from notes import views as notesViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', notesViews.index, name='index'),
    path('delete/<int:id>', notesViews.delete, name='delete'),
    path('edit/<int:id>', notesViews.edit, name='edit'),
    path('accounts/', include('accounts.urls')),
]

#the href in the template points to the 3rd url here

#reason why the integer needs to be there is because each note object has a unique id so it needs to know which one to delete

#we pass through the integer from the template to this url which does the delete view

#in this view you grab the specific object from the notes model and delete it 