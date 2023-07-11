#...
#autor: Waldinei Santos Gonçalves, Luana Nunes da Silva, Rafael de Oliveira Silva, Núbia Gonçalves dos Santos
#data: 09/04/2023
#finalidade: Sistema de Gerenciamento de Arquivos - GED
#versão: 0.0
#...

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

def cadastroGrupos(idCadastro, descricaoGrupo):
        cadastro = {
        "id":idCadastro,
        "descricao":descricaoGrupo
    }
        return descricaoGrupo 

#Chamando o programa de Cadastro de Grupos

novoCadGrupo=input("Gostaria de cadastrar um Novo Grupo  ? Diigite S para Sim e N para Não: ")
if novoCadGrupo=="S":
    while True:
        print("-------CADASTRO DE GRUPOS DE USUÁRIO--------")
        print("\n")
        numGrupo=input("Id do Grupo: ")
        infoGrupo=input("Descriçao do Grupo: ")
        cadastroGrupos(numGrupo,infoGrupo)
        print("\n")
        novoCad= input("Gostaria de cadastrar um novo grupo? Diigite S para Sim e N para Não: ")
        if novoCad.upper() == "N":
            break

    print("\n")
    print("Grupo cadastrado com sucesso !!")
    print("\n")
    print("-------GRUPO CADASTRADO--------")
    print ("Descriçao do Grupo: ",infoGrupo)
    print("\n")
    print("====================================================================")
 
#Chaamando o programa de Cadastro de Documento 

novoCadDoc=input("Gostaria de cadastrar um novo Documento ? Diigite S para Sim e N para Não: ")
if novoCadDoc == "S":    

    def cadastroDocumentos(idDocumento, nome, nomeArmazenamento, idGrupo):
            cadastroDoc={
            "id":idDocumento,
            "nomeDocumento":nome,
            "nomeArm":nomeArmazenamento,
            "grupo":idGrupo
        }
            return nome, nomeArmazenamento
   
    while True:
        print("-------CADASTRO DE DOCUMENTO--------")
        print("\n")
        infoDocumento=input("Id do Documento: ")
        nomeDocumento=input("Nome do Documento: ")
        nomeArm=input("Nome de Armazenamento: ")
        infoGrupo=input("Grupo: ")
        cadastroDocumentos(infoDocumento,nomeDocumento,nomeArm,infoGrupo)
        print("\n")
        novoCad= input("Gostaria de cadastrar um novo Documento ? Diigite S para Sim e N para Não: ")
        if novoCad.upper() == "N":
            break


    print("\n")
    print("Documento cadastrado com sucesso !!")
    print("\n")
    print("-------DOCUMENTO CADASTRADO--------")
    print("Descrição do Documento: ",nomeDocumento)
    print("Nome de Armazenamento do Documento: ",nomeArm)
    print("\n")
    print("====================================================================")
    
print("Cadastros Concluídos. Finalizando o Programa.")