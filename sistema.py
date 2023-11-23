import json
import os
from usuario import Usuario
from projeto import Projeto
from tarefa import Tarefa

class SistemaGerenciamentoProjetos:
    def __init__(self):
        self.usuarios = []
        self.projetos = []
        


    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)

    def salvar_dados(self, nome_arquivo):
        dados = {
            "usuarios": [usuario.to_dict() for usuario in self.usuarios],
            "projetos": [projeto.to_dict() for projeto in self.projetos]
        }

        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)

    def carregar_dados(self, nome_arquivo):
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r') as arquivo:
                dados = json.load(arquivo)
                self.usuarios = [Usuario.from_dict(usuario) for usuario in dados["usuarios"]]
                self.projetos = [Projeto.from_dict(projeto) for projeto in dados["projetos"]]

    def listar_usuarios(self):
        return self.usuarios
    
    def listar_projetos(self):
        print("Projetos Disponíveis:")
        for i, projeto in enumerate(self.projetos, start=1):
            print(f"{i}. {projeto.nome} - Responsável: {projeto.responsavel}")
            print(f"   Descrição do Projeto: {projeto.descricao}")
            print(f"   Status do Projeto: {projeto.status}")
            print(f"   Prioridade do Projeto: {projeto.prioridade}")
            print("   Tarefas:")
            for j, tarefa in enumerate(projeto.tarefas, start=1):
                print(f"    {j}. Descrição da Tarefa: {tarefa.descricao}")
                print(f"       Status da Tarefa: {tarefa.status}")
                print("   Comentários: ")
                for comentario in projeto.comentarios:
                    print(f"      {comentario['usuario']}: {comentario['comentario']}")
            print("   ___________________________________")
        return self.projetos
        
    def adicionar_tarefa_a_projeto(self, projeto):
        descricao_tarefa = input("Descrição da tarefa: ")

        # Listar status de tarefa e permitir que o usuário escolha pelo número
        print("Status de Tarefa Disponíveis:")
        for i, status in enumerate(Tarefa.status_tarefa_disponiveis, start=1):
            print(f"{i}. {status}")
        numero_status_tarefa = input("Status da tarefa: ")

        try:
            numero_status_tarefa = int(numero_status_tarefa)
            if 1 <= numero_status_tarefa <= len(Tarefa.status_tarefa_disponiveis):
                status_tarefa = Tarefa.status_tarefa_disponiveis[numero_status_tarefa - 1]

                tarefa = Tarefa(descricao_tarefa, status_tarefa)
                projeto.adicionar_tarefa(tarefa)

                print("Tarefa adicionada ao projeto com sucesso!")
            else:
                print("Status de tarefa inválido.")
        except ValueError:
            print("Número inválido")
            
    def selecionar_projeto(self, numero_selecionado):
        try:
            numero_selecionado = int(numero_selecionado)
            if 1 <= numero_selecionado <= len(self.projetos):
                return self.projetos[numero_selecionado - 1]
            else:
                return None
        except ValueError:
            return None
            
    def selecionar_tarefa(self, projeto, numero_selecionado):
        try:
            numero_selecionado = int(numero_selecionado)
            if 1 <= numero_selecionado <= len(projeto.tarefas):
                return projeto.tarefas[numero_selecionado - 1]
            else:
                return None
        except ValueError:
            return None
        
    def salvar_dados(self, nome_arquivo):
        dados = {
            "usuarios": [usuario.to_dict() for usuario in self.usuarios],
            "projetos": [projeto.to_dict() for projeto in self.projetos]
        }

        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)

    def carregar_dados(self, nome_arquivo):
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r') as arquivo:
                dados = json.load(arquivo)
                self.usuarios = [Usuario.from_dict(usuario) for usuario in dados["usuarios"]]
                self.projetos = [Projeto.from_dict(projeto) for projeto in dados["projetos"]]
                
    def efetuar_login(self, nome_usuario, senha):
        for usuario in self.usuarios:
            if usuario.nome == nome_usuario and usuario.senha == senha:
                return usuario  # Retorna a instância completa do Usuario
        return None
    
    def realizar_login(self, nome_usuario, senha):
        for usuario in self.usuarios:
            if usuario.nome == nome_usuario and usuario.senha == senha:
                return usuario
        return None
    
    def adicionar_comentario_a_projeto(self, projeto, usuario, comentario):
        projeto.adicionar_comentario(usuario, comentario)