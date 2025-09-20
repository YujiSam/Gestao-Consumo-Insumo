import pytest
import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.insumo import Insumo
from models.registro_consumo import RegistroConsumo
from structures.fila_consumo import FilaConsumo
from structures.pilha_consulta import PilhaConsulta

class TestStructures:
    """Testes para as estruturas de dados (Fila e Pilha)"""
    
    @pytest.fixture
    def exemplo_insumo(self):
        """Cria um insumo de exemplo para os testes"""
        return Insumo(1, "Reagente A", 100, datetime.date(2024, 12, 31), "reagente", 15.50)
    
    @pytest.fixture
    def exemplo_registro(self, exemplo_insumo):
        """Cria um registro de exemplo para os testes"""
        return RegistroConsumo(exemplo_insumo, datetime.date(2024, 1, 15), 5)
    
    def test_fila_vazia_inicialmente(self):
        """Testa se uma nova fila está vazia"""
        fila = FilaConsumo()
        assert fila.esta_vazia() == True
        assert fila.tamanho() == 0
        assert fila.primeiro() is None
    
    def test_fila_enfileirar(self, exemplo_registro):
        """Testa adicionar um registro na fila"""
        fila = FilaConsumo()
        fila.enfileirar(exemplo_registro)
        
        assert fila.esta_vazia() == False
        assert fila.tamanho() == 1
        assert fila.primeiro() == exemplo_registro
    
    def test_fila_desenfileirar(self, exemplo_registro):
        """Testa remover um registro da fila"""
        fila = FilaConsumo()
        fila.enfileirar(exemplo_registro)
        registro_removido = fila.desenfileirar()
        
        assert registro_removido == exemplo_registro
        assert fila.esta_vazia() == True
        assert fila.tamanho() == 0
    
    def test_fila_ordem_fifo(self, exemplo_insumo):
        """Testa se a fila mantém a ordem FIFO (First In, First Out)"""
        fila = FilaConsumo()
        
        # Cria dois registros diferentes
        registro1 = RegistroConsumo(exemplo_insumo, datetime.date(2024, 1, 15), 5)
        registro2 = RegistroConsumo(exemplo_insumo, datetime.date(2024, 1, 16), 3)
        
        # Adiciona na ordem: primeiro registro1, depois registro2
        fila.enfileirar(registro1)
        fila.enfileirar(registro2)
        
        # Remove na mesma ordem: primeiro registro1, depois registro2
        assert fila.desenfileirar() == registro1  # Primeiro a entrar, primeiro a sair
        assert fila.desenfileirar() == registro2  # Segundo a entrar, segundo a sair
    
    def test_pilha_vazia_inicialmente(self):
        """Testa se uma nova pilha está vazia"""
        pilha = PilhaConsulta()
        assert pilha.esta_vazia() == True
        assert pilha.tamanho() == 0
        assert pilha.topo() is None
    
    def test_pilha_empilhar(self, exemplo_registro):
        """Testa adicionar um registro na pilha"""
        pilha = PilhaConsulta()
        pilha.empilhar(exemplo_registro)
        
        assert pilha.esta_vazia() == False
        assert pilha.tamanho() == 1
        assert pilha.topo() == exemplo_registro
    
    def test_pilha_desempilhar(self, exemplo_registro):
        """Testa remover um registro da pilha"""
        pilha = PilhaConsulta()
        pilha.empilhar(exemplo_registro)
        registro_removido = pilha.desempilhar()
        
        assert registro_removido == exemplo_registro
        assert pilha.esta_vazia() == True
        assert pilha.tamanho() == 0
    
    def test_pilha_ordem_lifo(self, exemplo_insumo):
        """Testa se a pilha mantém a ordem LIFO (Last In, First Out)"""
        pilha = PilhaConsulta()
        
        # Cria dois registros diferentes
        registro1 = RegistroConsumo(exemplo_insumo, datetime.date(2024, 1, 15), 5)
        registro2 = RegistroConsumo(exemplo_insumo, datetime.date(2024, 1, 16), 3)
        
        # Adiciona na ordem: primeiro registro1, depois registro2
        pilha.empilhar(registro1)
        pilha.empilhar(registro2)
        
        # Remove na ordem inversa: primeiro registro2 (último), depois registro1
        assert pilha.desempilhar() == registro2  # Último a entrar, primeiro a sair
        assert pilha.desempilhar() == registro1  # Primeiro a entrar, último a sair