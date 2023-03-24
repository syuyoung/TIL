from django.urls import path
from . import views


app_name = 'calculate'
urlpatterns = [
    path('<int:number1>/<int:number2>/', views.calculate, name='calculate'),
    path('calculate2/', views.caculate2, name='caculate2'),
]
