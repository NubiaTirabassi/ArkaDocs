class CadastroUsuarios:
    def __init__(self):

        def cadastrarUsuario(idUsuario, login, email, senha, tipoUsuario, statusUsuario, listaUsuarios):
            novoUsuario = {
                "idUsuario": idUsuario,
                "login": login,
                "email": email,
                "senha": senha,
                "tipo": tipoUsuario,
                "status": statusUsuario
            }
            listaUsuarios.append(novoUsuario)

        def imprimir(listaUsuarios):
            for u in listaUsuarios:
                print(u)

        listaUsuarios = []

        # comando de repetição enquanto uma condição for verdadeira.

        while True:

            print("-------CADASTRO DE USUÁRIOS--------")
            print("\n")
            idUsuario = int(input("Digite o ID do usuário: "))
            login = input("Digite o login do usuário: ")
            email = input("Digite o e-mail do usuário: ")
            senha = input("Digite a senha do usuário: ")
            tipoUsuario = input("Digite o tipo do usuário (A-Administrador e U-Usuário): ")
            statusUsuario = input("Digite o status do usuário (A-Ativo, B-Bloqueado): ")
            
            cadastrarUsuario(idUsuario, login, email, senha, tipoUsuario, statusUsuario, listaUsuarios)
            # break oferece a possibilidade de sair de um loop quando uma condição externa é acionada (if) - 
            # será utilizado quando a resposta for "N"
            comando = input("Deseja cadastrar novo usuário? Diigite S para Sim e N para Não: ")
            if comando.upper() == "N":
                break
        
        print("\n")
        print("Cadastro realizado com sucesso !")
        print("\n")
        print("-------LISTA DE USUÁRIOS CADASTRADOS--------")
        for pessoa in listaUsuarios:
            print("Login: ",pessoa["login"])
        print("\n")
        print("====================================================================")