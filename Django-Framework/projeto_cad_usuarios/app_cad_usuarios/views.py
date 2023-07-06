from django.shortcuts import render

def home(request): # criando uma função
    return render(request,'usuarios/home.html') # criar uma página


def usuarios(request):
    # Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # Exibir todos os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all() # retornando todos os usuários que estão cadastrados no banco de dados
    }
    # Retornar os dados para a página de listagem de usuários
    return render(request,'usuarios/usuarios.html',usuarios)

