#...
#autor: Waldinei Santos Gonçalves, Luana Nunes da Silva, Rafael de Oliveira Silva, Núbia Gonçalves dos Santos
#data: 09/04/2023
#finalidade: Sistema de Gerenciamento de Arquivos - GED
#versão: 0.0
#...






from CadastroUsuarios import CadastroUsuarios
from CadastroGrupos import CadastroGrupos
from CadastroDocumentos import CadastroDocumentos

cadUsu1 = CadastroUsuarios ()
novoCadGrupo=input("Gostaria de cadastrar um Novo Grupo  ? Diigite S para Sim e N para Não: ")
if novoCadGrupo=="S":
    cadGrupo1 = CadastroGrupos ()

novoCadDoc=input("Gostaria de cadastrar um novo Documento ? Diigite S para Sim e N para Não: ")
if novoCadDoc == "S":
        cadDoc1=CadastroDocumentos()
       
        
print("Cadastros Concluídos. Finalizando o Programa.")






