import pytest
import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.insumo import Insumo
from models.registro_consumo import RegistroConsumo
from algorithms.busca import busca_sequencial, busca_binaria_por_data
from algorithms.ordenacao import merge_sort_por_quantidade, quick_sort_por_validade

class TestAlgorithms:
    """Testes para os algoritmos de busca e ordenação"""
    
    @pytest.fixture
    def lista_registros(self):
        """Cria uma lista de registros para testar os algoritmos"""
        insumo1 = Insumo(1, "Reagente A", 100, datetime.date(2024, 12, 31), "reagente", 15.50)
        insumo2 = Insumo(2, "Reagente B", 200, datetime.date(2024, 11, 30), "reagente", 22.30)
        insumo3 = Insumo(3, "Luvas", 500, datetime.date(2025, 6, 30), "descartavel", 2.10)
        
        registros = [
            RegistroConsumo(insumo1, datetime.date(2024, 1, 15), 5),   # Quantidade: 5
            RegistroConsumo(insumo2, datetime.date(2024, 1, 16), 3),   # Quantidade: 3
            RegistroConsumo(insumo3, datetime.date(2024, 1, 17), 10),  # Quantidade: 10
            RegistroConsumo(insumo1, datetime.date(2024, 1, 18), 2),   # Quantidade: 2
            RegistroConsumo(insumo2, datetime.date(2024, 1, 19), 7)    # Quantidade: 7
        ]
        
        return registros
    
    def test_busca_sequencial_encontra(self, lista_registros):
        """Testa se a busca sequencial encontra registros existentes"""
        resultados = busca_sequencial(lista_registros, "Reagente A")
        assert len(resultados) == 2  # Deve encontrar 2 registros do Reagente A
        
        for registro in resultados:
            assert registro.insumo.nome == "Reagente A"
    
    def test_busca_sequencial_nao_encontra(self, lista_registros):
        """Testa se a busca sequencial retorna vazio para insumos inexistentes"""
        resultados = busca_sequencial(lista_registros, "Inexistente")
        assert len(resultados) == 0  # Não deve encontrar nada
    
    def test_busca_binaria_encontra(self, lista_registros):
        """Testa se a busca binária encontra registro por data existente"""
        data_alvo = datetime.date(2024, 1, 16)
        resultado = busca_binaria_por_data(lista_registros, data_alvo)
        
        assert resultado is not None
        assert resultado.data == data_alvo
        assert resultado.insumo.nome == "Reagente B"
    
    def test_busca_binaria_nao_encontra(self, lista_registros):
        """Testa se a busca binária retorna None para data inexistente"""
        data_alvo = datetime.date(2024, 2, 1)  # Data que não existe nos registros
        resultado = busca_binaria_por_data(lista_registros, data_alvo)
        
        assert resultado is None
    
    def test_merge_sort_quantidade(self, lista_registros):
        """Testa se o merge sort ordena corretamente por quantidade"""
        ordenados = merge_sort_por_quantidade(lista_registros)
        
        # Verifica se está ordenado do menor para o maior
        quantidades = [r.quantidade_consumida for r in ordenados]
        assert quantidades == sorted(quantidades)
        
        # Primeiro deve ser o de menor quantidade (2)
        assert ordenados[0].quantidade_consumida == 2
        # Último deve ser o de maior quantidade (10)
        assert ordenados[-1].quantidade_consumida == 10
    
    def test_quick_sort_validade(self, lista_registros):
        """Testa se o quick sort ordena corretamente por validade"""
        ordenados = quick_sort_por_validade(lista_registros)
        
        # Verifica se está ordenado por validade (mais próxima primeiro)
        validades = [r.insumo.validade for r in ordenados]
        assert validades == sorted(validades)
        
        # Primeiro deve ser o que vence primeiro (2024-11-30)
        assert ordenados[0].insumo.validade == datetime.date(2024, 11, 30)
        # Último deve ser o que vence por último (2025-06-30)
        assert ordenados[-1].insumo.validade == datetime.date(2025, 6, 30)