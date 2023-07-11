#...
#autor: Waldinei Santos Gonçalves, Rafael de Oliveira Silva, Núbia Gonçalves dos Santos
#data: 09/06/2023
#finalidade: Sistema de Gerenciamento de Arquivos - GED
#versão: 0.0
#...

import mysql.connector


### Autenticar Usuario
def autenticarUsuario():
    opcao = int(input("Escolha uma opção: 1 - Cadastrar; 2 - Login; 3 - Sair: "))
    while ("*"):
        match opcao:
            case 1:
                coneccaoBanco = mysql.connector.connect(
                        host="localhost", user="projeto_integrador", password="123456",
                        database="arkadocs")
                cursorBanco = coneccaoBanco.cursor()

                print("Opcao escolhida foi: 1 - Cadastrar Usuario:")
                nome = input("Digite o Nome: ")
                login = input("Digite o Login: ")
                senha = input("Digite a Senha: ")
                email = input("Digite o Email: ")
                tipo = "U"
                status = "A"
                SQL =  "insert into usuarios(nomeUsuario, loginUsuario, senhaUsuario, " \
                       "emailUsuario, tipoUsuario, statusUsuario)values( % s, %s, %s, %s, %s, %s)"

                pacoteDados = (nome, login, senha, email, tipo, status)
                cursorBanco.execute(SQL, pacoteDados)
                print("Usuario Cadatrado! Registros Alterados: ",
                cursorBanco.rowcount)
                coneccaoBanco.commit()
                cursorBanco.close()
                coneccaoBanco.close()
                return True, login
            case 2:
                coneccaoBanco = mysql.connector.connect(
                    host="localhost", user="projeto_integrador", password="123456",
                    database="arkadocs")
                cursorBanco = coneccaoBanco.cursor()
                print("Opcao escolhida foi: 2 - Login:")
                login = input("Digite o Login: ")
                senha = input("Digite a senha: ")
                SQL = "select * from usuarios where loginUsuario=%s and senhaUsuario=%s"
                pacoteDados = (login, senha)
                cursorBanco.execute(SQL, pacoteDados)
                validaLogin = cursorBanco.fetchone()
                cursorBanco.close()
                coneccaoBanco.close()
                if (validaLogin):
                    return True, login
                else:
                 print("Falha Autenticação login/senha.\nTente novamente.")
                return False, "vazio"
            case 3:
                print("Usuario pediu para sair!")
                return False,"vazio"

### Listar Todos Grupos

def listarTodosGrupos():
    coneccaoBanco = mysql.connector.connect(
        host="localhost",
        user="projeto_integrador",
        password="123456",
        database="arkadocs")
    cursorBanco = coneccaoBanco.cursor()
    SQL = "select * from grupos"
    cursorBanco.execute(SQL)
    consultaBanco = cursorBanco.fetchall()

    print("Dados dos Grupos:")
    for grupo in consultaBanco:
        print("Id: ", grupo[0], " - Descricao: ", grupo[1])
    cursorBanco.close()
    coneccaoBanco.close()

### Listar Meus Grupos

def listarMeusGrupos(loginUsuario):
    coneccaoBanco = mysql.connector.connect(
        host="localhost",
        user="projeto_integrador",
        password="123456",
        database="arkadocs")
    cursorBanco = coneccaoBanco.cursor()
    SQL = "select idusuario, loginusuario from usuarios where loginusuario = %s"

    pacoteDados = (loginUsuario,)
    cursorBanco.execute(SQL, pacoteDados)
    consultaBanco = cursorBanco.fetchone()
    idUsuario = consultaBanco[0]

    SQL = "select usuarios.nomeUsuario, grupos.idgrupo, grupos.decricao from usuarios, pertence, " \
          "grupos where usuarios.idusuario = %s and usuarios.idusuario = pertence.idusuario and " \
          "pertence.idgrupo = grupos.idgrupo"
    pacoteDados = (idUsuario,)
    cursorBanco.execute(SQL, pacoteDados)
    consultaBanco = cursorBanco.fetchall()
    print("Dados dos Grupos a que Pertenço:")
    for registro in consultaBanco:
        print("idGrupo: ", registro[1], "Nome Grupo: ", registro[2])
    cursorBanco.close()
    coneccaoBanco.close()

### Cadastrar Grupo

def cadastrarGrupo():
    coneccaoBanco = mysql.connector.connect(
        host="localhost",
        user="projeto_integrador",
        password="123456",
        database="arkadocs")
    cursorBanco = coneccaoBanco.cursor()

    nomeNovoGrupo = input("Informe Nome/Descricao Novo Grupo: ")
    SQL = "insert into grupos(decricao) values (%s)"
    pacoteDados = (nomeNovoGrupo,)
    cursorBanco.execute(SQL, pacoteDados)

    print("Grupo Cadastrado! Registros Alterados: ", cursorBanco.rowcount)
    coneccaoBanco.commit()
    cursorBanco.close()
    coneccaoBanco.close()
    return True

### Entrar Grupo

def entrarGrupo(loginUsuario, entrarGrupo):
    coneccaoBanco = mysql.connector.connect(
        host="localhost",
        user="projeto_integrador",
        password="123456",
        database="arkadocs")
    cursorBanco = coneccaoBanco.cursor()

    SQL = "select idusuario, loginusuario from " \
          "usuarios where loginusuario = %s"
    pacoteDados = (loginUsuario,)
    cursorBanco.execute(SQL, pacoteDados)
    consultaBanco = cursorBanco.fetchone()
    idUsuario = consultaBanco[0]

    SQL = "insert into pertence(idusuario, idgrupo) values (%s,%s)"
    pacoteDados = (idUsuario, entrarGrupo)
    cursorBanco.execute(SQL, pacoteDados)

    print("Já entrou no Grupo! Registros Alterados: ", cursorBanco.rowcount)

    coneccaoBanco.commit()
    cursorBanco.close()
    coneccaoBanco.close()
    return True

### Sair Grupo

def sairGrupo(loginUsuario, sairGrupo):
    coneccaoBanco = mysql.connector.connect(
        host="localhost",
        user="projeto_integrador",
        password="123456",
        database="arkadocs")
    cursorBanco = coneccaoBanco.cursor()

    SQL = "select idusuario, loginusuario " \
          "from usuarios where loginusuario =%s"
    pacoteDados = (loginUsuario,)
    cursorBanco.execute(SQL, pacoteDados)
    consultaBanco = cursorBanco.fetchone()
    idUsuario = consultaBanco[0]

    SQL = "delete from pertence where idusuario=%s and idgrupo=%s"
    pacoteDados = (idUsuario, sairGrupo)
    cursorBanco.execute(SQL, pacoteDados)
    return True

### Cadastrar Usuario

def cadastraUsuario(nome, login, senha, email):
    coneccaoBanco = mysql.connector.connect(
        host="localhost",
        user="projeto_integrador",
        password="123456",
        database="arkadocs")
    cursorBanco = coneccaoBanco.cursor()

    tipo = "U"
    status = "A"

    SQL = "insert into usuarios(nomeUsuario, loginUsuario, senhaUsuario, " \
          "emailUsuario, tipoUsuario, statusUsuario) values(%s, %s, %s, %s, %s, %s) "
    pacoteDados = (nome, login, senha, email, tipo, status)
    cursorBanco.execute(SQL, pacoteDados)

    print("Numero Registros Alterados: ", cursorBanco.rowcount)

    cursorBanco.close()
    coneccaoBanco.close()

### Bloquear Usuario

def bloquearUsuario(idBloqueio):
    coneccaoBanco = mysql.connector.connect(
    host = "localhost",
    user = "projeto_integrador",
    password = "123456",
    database = "arkadocs")
    cursorBanco = coneccaoBanco.cursor()

    novoStatus = "B"
    SQL = "update usuarios set statusUsuario = %s where idUsuario=%s"

    pacoteDados = (novoStatus, idBloqueio)
    cursorBanco.execute(SQL, pacoteDados)
    coneccaoBanco.commit()

    print("Numero Registros Afetados: ", cursorBanco.rowcount)

    cursorBanco.close()
    coneccaoBanco.close()

### Loop Infinito

validaLogin = False
continuar = "s"
validaLogin, loginUsuario = autenticarUsuario()
while (continuar == "s" and validaLogin == True):
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("Login do Usuário:", loginUsuario)
    print("\n\n")
    print("Deseja Alterar: Grupos ou Documentos?")
    menu = int(input("1 - Grupos; 2 - Documentos:"))
    match (menu):
        case 1:
            print("\nOpcao escolhida: Grupos")
            print("1 - Listar Todos; 2 - Listar Meus Grupos; 3 - Cadastrar Grupo;")
            print("4 - Entrar em Grupo; 5 - Sair de Grupo;")
            modificarGrupo = int(input("Escolha uma Opcao: "))
    match (modificarGrupo):
        case 1:
            listarTodosGrupos()
        case 2:
            listarMeusGrupos(loginUsuario)
        case 3:
            cadastrarGrupo()
        case 4:
            print("Qual o Id do Grupo que deseja ENTRAR?")
            entrar = int(input("Digite o Id do Grupo: "))
            entrarGrupo = (loginUsuario, entrar)
        case 5:
            print("Qual o Id do Grupo que deseja SAIR?")
            sair = int(input("Digite o Id do Grupo: "))
            sairGrupo = (loginUsuario, sair)
            continuar = input("Deseja Continuar no Sistema? [S/N]")