from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('create_lawsuit',views.create_lawsuit),
    path('delete_lawsuit/<int:id_lawsuit>',views.delete_lawsuit),
    path('lawsuit_detail/<int:id_lawsuit>',views.lawsuit_detail),
    path('lawsuit_detail/re_make_lawsuitpdf/<int:id_lawsuit>',views.re_make_lawsuitpdf),
]