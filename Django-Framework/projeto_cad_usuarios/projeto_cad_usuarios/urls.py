
# Configuração de URL para o projeto projeto_cad_usuários

from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, viwe responsável, nome de referência
    # usuarios.com
    path('',views.home,name='home'),  # url que o usuário tem que inserir
    # usuarios.com/usuarios
    path('usuarios/',views.usuarios,name= 'listagem_usuarios')
]
