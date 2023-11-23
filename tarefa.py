class Tarefa:

    def __init__(self, descricao, status, prioridade=None, data_entrega=None, responsavel=None):
        self.descricao = descricao
        self.status = status
        self.prioridade = prioridade
        self.data_entrega = data_entrega
        self.responsavel = responsavel
        
    status_tarefa_disponiveis = ["Iniciado", "Em Andamento", "Finalizado"]

    def set_prioridade(self, prioridade):
        self.prioridade = prioridade

    def set_data_entrega(self, data_entrega):
        self.data_entrega = data_entrega

    def set_responsavel(self, responsavel):
        self.responsavel = responsavel

    def alterar_status(self, novo_status):
        self.status = novo_status
        
    @staticmethod
    def from_dict(dados):
        descricao = dados["descricao"]
        status = dados["status"]
        return Tarefa(descricao, status)

    def to_dict(self):
        return {
            "descricao": self.descricao,
            "status": self.status
        }