from blog.views import *
from django.urls import path

urlpatterns = [
    path('', asosiy, name="asosiy"),
    path('jurnallar/', jurnallar, name="jurnallar"),
    path('yangiliklar/', yangiliklar, name="yangiliklar"),
    path('jurnal_detel/<int:id>/', jurnal_detel, name="jurnal_detel"),
    path('yangilik_detel/<int:id>/', yangilik_detel, name="yangilik_detel"),
    path('search/', SearchResultList.as_view(), name="search"),
    path('sinov_detel/<int:id>/', sinov_detel, name="sinov_detel"),
]
