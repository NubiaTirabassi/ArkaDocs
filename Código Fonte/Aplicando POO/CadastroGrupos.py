class CadastroGrupos:
    def __init__(self):
        def cadastroGrupos(idCadastro, descricaoGrupo):
            cadastro = {
            "id":idCadastro,
            "descricao":descricaoGrupo
        }
            return descricaoGrupo 

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






 