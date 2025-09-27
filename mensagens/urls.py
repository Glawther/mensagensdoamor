from django.urls import path
from . import views

urlpatterns = [
    # A rota vazia ('') vai chamar a função 'home_mensagem_secreta'
    path('', views.home_mensagem_secreta, name='home'),
    path('reagir/<int:mensagem_id>/', views.reagir_mensagem, name='reagir'), 
    path('criar-admin-temp/', views.criar_admin_temp, name='criar_admin_temp'), 
]