from typing import Optional
from models.registro_consumo import RegistroConsumo

class PilhaConsulta:
    """
    PILHA DE CONSULTA: Organiza os registros com os mais recentes primeiro (como pilha de pratos)
    
    PRINCÍPIO: Último que entra é o primeiro que sai (LIFO - Last In, First Out)
    Use quando quiser ver os registros mais recentes primeiro
    """
    
    def __init__(self):
        self.registros = []  # Lista vazia para guardar os registros
    
    def empilhar(self, registro: RegistroConsumo):
        """
        EMPILHAR: Adiciona um novo registro no topo da pilha
        Como colocar um prato limpo em cima da pilha
        """
        self.registros.append(registro)
    
    def desempilhar(self) -> Optional[RegistroConsumo]:
        """
        DESEMPILHAR: Remove e retorna o último registro (o do topo)
        Como pegar o prato de cima da pilha
        """
        if not self.esta_vazia():
            return self.registros.pop()  # Remove o último
        return None
    
    def topo(self) -> Optional[RegistroConsumo]:
        """
        VER TOPO: Mostra o último registro sem remover
        Como espiar o prato do topo sem pegá-lo
        """
        if not self.esta_vazia():
            return self.registros[-1]  # Mostra o último
        return None
    
    def esta_vazia(self) -> bool:
        """VERIFICAR SE PILHA ESTÁ VAZIA"""
        return len(self.registros) == 0
    
    def tamanho(self) -> int:
        """CONTAR REGISTROS: Quantos registros tem na pilha"""
        return len(self.registros)