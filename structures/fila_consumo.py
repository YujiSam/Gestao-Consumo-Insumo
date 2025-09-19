from typing import Optional  # Para dizer que algo pode ser vazio
from models.registro_consumo import RegistroConsumo  # Importamos o registro

class FilaConsumo:
    """
    FILA DE CONSUMO: Organiza os registros por ordem de chegada (como fila de banco)
    
    PRINCÍPIO: Primeiro que entra é o primeiro que sai (FIFO - First In, First Out)
    Use quando quiser ver os registros na ordem em que aconteceram
    """
    
    def __init__(self):
        self.registros = []  # Lista vazia para guardar os registros
    
    def enfileirar(self, registro: RegistroConsumo):
        """
        COLOCAR NA FILA: Adiciona um novo registro no final da fila
        Como chegar no final de uma fila real
        """
        self.registros.append(registro)
    
    def desenfileirar(self) -> Optional[RegistroConsumo]:
        """
        RETIRAR DA FILA: Remove e retorna o primeiro registro da fila
        Como atender o primeiro da fila
        Retorna None (vazio) se a fila estiver vazia
        """
        if not self.esta_vazia():
            return self.registros.pop(0)  # Remove o primeiro
        return None
    
    def esta_vazia(self) -> bool:
        """VERIFICAR SE FILA ESTÁ VAZIA: Retorna True se não tiver registros"""
        return len(self.registros) == 0
    
    def tamanho(self) -> int:
        """CONTAR REGISTROS: Retorna quantos registros tem na fila"""
        return len(self.registros)
    
    def primeiro(self) -> Optional[RegistroConsumo]:
        """
        VER PRIMEIRO DA FILA: Mostra o primeiro registro sem remover
        Como espiar quem é o primeiro da fila sem chamá-lo
        """
        if not self.esta_vazia():
            return self.registros[0]  # Mostra o primeiro sem remover
        return None