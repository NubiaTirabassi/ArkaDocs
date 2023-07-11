class CadastroDocumentos:
    def __init__(self):
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
        
        