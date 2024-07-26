from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='pagina_inicial'),
    path('lista_topicos/', views.lista_topicos, name='lista_topicos')
]
