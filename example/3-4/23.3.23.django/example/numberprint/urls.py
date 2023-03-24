from django.urls import path
from . import views

app_name = 'numberprint'
urlpatterns = [
    path('number-print/<int:number>/', views.number_print, name='number_print'),
    path('number-print2/', views.number_print2, name='number_print2'),
]
