from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^graficos/acumulado$', views.Acumulado.as_view(), name='acumulado'),
    url(r'^graficos/diario$', views.Diario.as_view(), name='diario'),
]
