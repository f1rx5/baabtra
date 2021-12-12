from django.urls import path,include
from . import views
urlpatterns=[
    path('home/',views.fnhome,name='home'),
    path('courses/',views.fncourses,name='courses'),
    path('contact/',views.fncontact,name='contact'),
]