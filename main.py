from usuario import Usuario
from tarefa import Tarefa
from projeto import Projeto
from sistema import SistemaGerenciamentoProjetos
import json
import os

class Main:
    @staticmethod
    def main():
        sistema = SistemaGerenciamentoProjetos()
        funcoes_usuario = Usuario.listar_funcoes_usuario()
        usuario_logado = None

        # Adicionar usuário administrador por padrão (para facilitar testes)
        administrador_padrao = Usuario("user", "User", "123")
        sistema.adicionar_usuario(administrador_padrao)

        # Efetuar automaticamente o login com o administrador padrão
        usuario_logado = administrador_padrao
        print(f"Bem-vindo, {usuario_logado.nome} ({usuario_logado.funcao})!")

        # Menu de opções
        while True:
            print("\n           Menu Principal")
            print("------------------------------------")
            print("|1. Adicionar Usuário              |")
            print("|2. Adicionar Projeto              |")
            print("|3. Adicionar Tarefa a um Projeto  |")
            print("|4. Listar Usuários                |")
            print("|5. Listar Projetos                |")
            print("|6. Alterar Status de Projeto      |")
            print("|7. Alterar Status de Tarefa       |")
            print("|8. Adicionar Comentários          |")
            print("|9. Login                          |")
            print("|0. Sair                           |")
            print("------------------------------------")
            opcao = input("Escolha uma Opção: ")

            if usuario_logado and isinstance(usuario_logado, Usuario):
                if usuario_logado.funcao == 'Administrador':
                    permissao = True
                elif usuario_logado.funcao == 'Assistente':
                    permissao = opcao in ['4', '5', '6', '7', '8', '9', '0']
                elif usuario_logado.funcao == 'User':
                    permissao = opcao in ['1','4', '5', '9', '0']

                if not permissao:
                    print("Você não tem permissão para executar esta opção.")
                    continue

                if opcao == '1':
                    # Restante do código para a opção 1
                    nome = input("Nome do Usuário: ")
                    senha = input("Senha: ")  # Adicionando senha
                    for numero, funcao in funcoes_usuario.items():
                        print(f"{numero}. {funcao}")

                    while True:
                        numero_funcao = input("Função: ")
                        try:
                            numero_funcao = int(numero_funcao)
                            if numero_funcao in funcoes_usuario:
                                funcao = funcoes_usuario[numero_funcao]
                                usuario = Usuario(nome, funcao, senha)
                                sistema.adicionar_usuario(usuario)
                                print("------------------------------------")
                                print("Usuário adicionado com sucesso!")
                                input("Pressione Enter para continuar...")
                                os.system('cls')
                                break
                            else:
                                print("Função inválida.")
                        except ValueError:
                            print("Número inválido.")

                elif opcao == '2':
                    # Restante do código para a opção 2
                    nome_projeto = input("Nome do projeto: ")
                    descricao = input("Descrição do projeto: ")

                    # Listar status de projeto e permitir que o usuário escolha pelo número
                    print("Status de Projeto Disponíveis:")
                    for i, status in enumerate(Projeto.Status_Disponíveis, start=1):
                        print(f"{i}. {status}")

                    while True:
                        numero_status_projeto = input("Status do Projeto: ")
                        try:
                            numero_status_projeto = int(numero_status_projeto)
                            if 1 <= numero_status_projeto <= len(Projeto.Status_Disponíveis):
                                status_projeto = Projeto.Status_Disponíveis[numero_status_projeto - 1]
                                break
                            else:
                                print("Status de projeto inválido.")
                        except ValueError:
                            print("Número inválido.")

                    # Listar prioridades de projeto e permitir que o usuário escolha pelo número
                    print("Prioridades Disponíveis:")
                    for i, prioridade in enumerate(Projeto.prioridades_disponíveis, start=1):
                        print(f"{i}. {prioridade}")

                    while True:
                        numero_prioridade_projeto = input("Prioridade do projeto: ")
                        try:
                            numero_prioridade_projeto = int(numero_prioridade_projeto)
                            if 1 <= numero_prioridade_projeto <= len(Projeto.prioridades_disponíveis):
                                prioridade_projeto = Projeto.prioridades_disponíveis[numero_prioridade_projeto - 1]
                                break
                            else:
                                print("Prioridade de projeto inválida.")
                        except ValueError:
                            print("Número inválido.")

                    data_entrega_projeto = input("Data de entrega do projeto: ")

                    # Listar os usuários disponíveis
                    usuarios_disponíveis = sistema.listar_usuarios()
                    print("Usuários disponíveis:")
                    for i, user in enumerate(usuarios_disponíveis, start=1):
                        print(f"{i}. {user.nome} - Função: {user.funcao}")

                    while True:
                        numero_usuario = input("Selecione um usuário responsável pelo projeto: ")
                        try:
                            numero_usuario = int(numero_usuario)
                            if 1 <= numero_usuario <= len(usuarios_disponíveis):
                                responsável_usuario = usuarios_disponíveis[numero_usuario - 1]

                                projeto = Projeto(nome_projeto, descricao, status_projeto, prioridade_projeto, data_entrega_projeto, responsável_usuario.nome)
                                sistema.adicionar_projeto(projeto)
                                print("Projeto adicionado com sucesso!")
                                break
                            else:
                                print("Usuário inválido.")
                        except ValueError:
                            print("Número inválido.")

                elif opcao == '3':
                    # Restante do código para a opção 3
                    projetos_disponíveis = sistema.listar_projetos()
                    numero_projeto = input("Selecione um projeto pelo número: ")
                    projeto_selecionado = sistema.selecionar_projeto(numero_projeto)

                    if projeto_selecionado:
                        sistema.adicionar_tarefa_a_projeto(projeto_selecionado)
                    else:
                        print(f"Projeto não encontrado.")

                elif opcao == '4':
                    # Restante do código para a opção 4
                    Usuario.listar_usuarios(sistema.usuarios)

                elif opcao == '5':
                    # Restante do código para a opção 5
                    sistema.listar_projetos()

                elif opcao == '6':
                    # Restante do código para a opção 6
                    projetos_disponíveis = sistema.listar_projetos()
                    numero_projeto = input("Selecione um projeto pelo número: ")
                    projeto_selecionado = sistema.selecionar_projeto(numero_projeto)

                    if projeto_selecionado:
                        print("Status de Projeto Disponíveis:")
                        for i, status in enumerate(Projeto.Status_Disponíveis, start=1):
                            print(f"{i}. {status}")

                        while True:
                            numero_status_projeto = input("Status do Projeto: ")
                            try:
                                numero_status_projeto = int(numero_status_projeto)
                                if 1 <= numero_status_projeto <= len(Projeto.Status_Disponíveis):
                                    status_projeto = Projeto.Status_Disponíveis[numero_status_projeto - 1]

                                    # Verifica permissão antes de alterar o status
                                    if usuario_logado and isinstance(usuario_logado, Usuario):
                                        projeto_selecionado.alterar_status(status_projeto)
                                        print("Status do projeto alterado com sucesso!")
                                    else:
                                        print("Você não tem permissão para alterar o status do projeto.")

                                    break
                                else:
                                    print("Status de projeto inválido.")
                            except ValueError:
                                print("Número inválido.")
                    else:
                        print(f"Projeto não encontrado.")

                elif opcao == '7':
                    # Restante do código para a opção 7
                    projetos_disponíveis = sistema.listar_projetos()
                    numero_projeto = input("Selecione o PROJETO: ")
                    projeto_selecionado = sistema.selecionar_projeto(numero_projeto)

                    if projeto_selecionado:
                        tarefas_disponíveis = projeto_selecionado.tarefas
                        print("Tarefas disponíveis para o projeto:")
                        for i, tarefa in enumerate(tarefas_disponíveis, start=1):
                            print(f"{i}. Descrição da Tarefa: {tarefa.descricao} - Status: {tarefa.status}")

                        while True:
                            numero_tarefa = input("Selecione a TAREFA: ")
                            tarefa_selecionada = sistema.selecionar_tarefa(projeto_selecionado, numero_tarefa)

                            if tarefa_selecionada:
                                print(f"Status atual da Tarefa: {tarefa_selecionada.status}")
                                print("Selecione o novo status da Tarefa:")
                                for i, status in enumerate(Tarefa.status_tarefa_disponiveis, start=1):
                                    print(f"{i}. {status}")

                                while True:
                                    numero_status_tarefa = input("Novo Status da Tarefa: ")
                                    try:
                                        numero_status_tarefa = int(numero_status_tarefa)
                                        if 1 <= numero_status_tarefa <= len(Tarefa.status_tarefa_disponiveis):
                                            novo_status_tarefa = Tarefa.status_tarefa_disponiveis[numero_status_tarefa - 1]

                                            # Verifica permissão antes de alterar o status
                                            if usuario_logado and isinstance(usuario_logado, Usuario):
                                                if usuario_logado.funcao == 'Administrador' or usuario_logado.funcao == 'Assistente':
                                                    tarefa_selecionada.alterar_status(novo_status_tarefa)
                                                print("Status da tarefa alterado com sucesso!")
                                            else:
                                                print("Você não tem permissão para alterar o status da tarefa.")

                                            break
                                        else:
                                            print("Status de tarefa inválido.")
                                    except ValueError:
                                        print("Número inválido.")
                            else:
                                print("Tarefa não encontrada.")
                                break
                            
                elif opcao == '8':
                    # Adicionar Comentário ao Projeto
                    projetos_disponíveis = sistema.listar_projetos()
                    numero_projeto = input("Selecione o PROJETO para adicionar um comentário: ")
                    projeto_selecionado = sistema.selecionar_projeto(numero_projeto)

                    if projeto_selecionado:
                        comentario = input("Digite seu comentário: ")
                        sistema.adicionar_comentario_a_projeto(projeto_selecionado, usuario_logado, comentario)
                        print("Comentário adicionado com sucesso!")
                    else:
                        print(f"Projeto não encontrado.")               

                if opcao == '9':
                    # Efetuar login com o novo usuário
                    novo_usuario_logado = Usuario.login(sistema)
                    if novo_usuario_logado:
                        usuario_logado = novo_usuario_logado
                        print(f"Bem-vindo, {usuario_logado.nome} ({usuario_logado.funcao})!")

                        # Verificação de permissão após o login
                        if not usuario_logado.verificar_permissao(opcao):
                            print("Você não tem permissão para executar esta opção.")
                            usuario_logado = None  # Desloga o usuário se não tiver permissão
                            continue
                    else:
                        print("Login falhou. Verifique o nome de usuário e senha.")
                        continue

                if opcao == '0':
                    print("Finalizando o programa.")
                    break

            else:
                print("Você precisa fazer login para acessar as opções.")
                continue

if __name__ == "__main__":
    Main.main()
