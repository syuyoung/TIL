from django.urls import path
from articles import views


urlpatterns = [
    path('', views.article),
    path('<article_pk>/', views.article_detail),
]
