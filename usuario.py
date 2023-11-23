# Classe Usuario
class Usuario:
    Niveis_Permissao = {
        'Administrador': 1,
        'Assistente': 2,
        'User': 3
    }

    def __init__(self, nome_usuario, funcao, senha):
        self.nome = nome_usuario
        self.funcao = funcao
        self.senha = senha
        self.projetos = []
        self.nivel_permissao = self.definir_nivel_permissao()

    def definir_nivel_permissao(self):
        return Usuario.Niveis_Permissao.get(self.funcao, 0)
    
    def verificar_permissao(self, opcao):
        try:
            opcao_int = int(opcao)
        except ValueError:
            return False  # Se não for possível converter para inteiro, retorna False

        if self.nivel_permissao is not None:
            if self.funcao == 'Administrador':
                return True  # Administrador tem acesso a todas as opções
            elif self.funcao == 'Assistente' and opcao_int in [4, 5, 6, 7, 8, 9, 0]:
                return True
            elif self.funcao == 'User' and opcao_int in [1, 4, 5, 9, 0]:
                return True
        return False

    @staticmethod
    def login(sistema):
        nome_usuario = input("Nome do Usuário: ")
        senha = input("Senha: ")

        usuario_logado = sistema.efetuar_login(nome_usuario, senha)

        if usuario_logado:
            return usuario_logado
        else:
            print("Login falhou. Verifique o nome de usuário e senha.")
            return None

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)

    @staticmethod
    def listar_usuarios(usuarios):
        print("\nLista de Usuários:")
        for usuario in usuarios:
            print(f"Nome: {usuario.nome} - Função: {usuario.funcao}")

    @staticmethod
    def from_dict(dados):
        nome = dados["nome"]
        funcao = dados["funcao"]
        usuario = Usuario(nome, funcao)
        return usuario

    def to_dict(self):
        return {
            "nome": self.nome,
            "funcao": self.funcao
        }

    @staticmethod
    def listar_funcoes_usuario():
        funcoes = {
            1: "Administrador",
            2: "Assistente",
            3: "User"
        }
        return funcoes