from.import views
from django.urls import path

urlpatterns=[
   
    path('rent/', views.rent, name='rent'),
    path('form/<str:id>/', views.fri, name='form'),
    path('register/<str:id>/', views.reg, name='register'),
    
]