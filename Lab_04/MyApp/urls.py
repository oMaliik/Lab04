from django.urls import path
from . import views

urlpatterns = [
    path("", views.default, name="default"),
    path("<int:number>", views.anyNumber, name="anyNumber"),
    path("taxrate/", views.taxRate, name="taxRate"),
    
]