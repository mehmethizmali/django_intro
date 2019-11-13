from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #views altındaki post_list metodunun yoluna bakar
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]