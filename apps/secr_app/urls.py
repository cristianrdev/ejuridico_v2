from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('create_lawsuit',views.create_lawsuit),
    path('delete_lawsuit/<int:id_lawsuit>',views.delete_lawsuit),
]