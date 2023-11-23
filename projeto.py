from tarefa import Tarefa

class Projeto:

    def __init__(self, nome, descricao, status, prioridade, data_entrega, responsavel):
        self.nome = nome
        self.descricao = descricao
        self.status = status
        self.prioridade = prioridade
        self.data_entrega = data_entrega
        self.responsavel = responsavel
        self.tarefas = []
        self.comentarios = []
        
    Status_Disponíveis = ["Não Iniciado", "Em Andamento", "Concluído"]
    prioridades_disponíveis = ["Baixa","Média","Alta"]

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def alterar_status(self, novo_status):
        self.status = novo_status
        
    @staticmethod
    def from_dict(dados):
        nome = dados["nome"]
        descricao = dados["descricao"]
        status = dados["status"]
        prioridade = dados["prioridade"]
        data_entrega = dados["data_entrega"]
        responsavel = dados["responsavel"]
        tarefas = [Tarefa.from_dict(tarefa) for tarefa in dados["tarefas"]]
        return Projeto(nome, descricao, status, prioridade, data_entrega, responsavel, tarefas)

    def to_dict(self):
        return {
            "nome": self.nome,
            "descricao": self.descricao,
            "status": self.status,
            "prioridade": self.prioridade,
            "data_entrega": self.data_entrega,
            "responsavel": self.responsavel,
            "tarefas": [tarefa.to_dict() for tarefa in self.tarefas]
        }
        
    def adicionar_comentario(self, usuario, comentario):
        self.comentarios.append({"usuario": usuario.nome, "comentario": comentario})