import pytest
import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.insumo import Insumo
from models.registro_consumo import RegistroConsumo

class TestModels:
    """Testes para as classes de modelo (Insumo e RegistroConsumo)"""
    
    def test_insumo_creation(self):
        """Testa se um insumo é criado corretamente com todos os atributos"""
        insumo = Insumo(
            id=1, 
            nome="Reagente A", 
            quantidade=100, 
            validade=datetime.date(2024, 12, 31),
            tipo="reagente", 
            custo_unitario=15.50
        )
        
        assert insumo.id == 1
        assert insumo.nome == "Reagente A"
        assert insumo.quantidade == 100
        assert insumo.validade == datetime.date(2024, 12, 31)
        assert insumo.tipo == "reagente"
        assert insumo.custo_unitario == 15.50
    
    def test_insumo_str_representation(self):
        """Testa a representação em string do insumo"""
        insumo = Insumo(1, "Reagente A", 100, datetime.date(2024, 12, 31), "reagente", 15.50)
        expected_str = "Reagente A (ID: 1) - 100 unidades - Validade: 2024-12-31 - R$ 15.50"
        assert str(insumo) == expected_str
    
    def test_registro_consumo_creation(self):
        """Testa se um registro de consumo é criado corretamente"""
        insumo = Insumo(1, "Reagente A", 100, datetime.date(2024, 12, 31), "reagente", 15.50)
        data_consumo = datetime.date(2024, 1, 15)
        registro = RegistroConsumo(insumo, data_consumo, 5)
        
        assert registro.insumo == insumo
        assert registro.data == data_consumo
        assert registro.quantidade_consumida == 5
        assert registro.custo_total == 77.50  # 5 * 15.50
    
    def test_registro_reduz_estoque(self):
        """Testa se o registro de consumo reduz o estoque do insumo"""
        insumo = Insumo(1, "Reagente A", 100, datetime.date(2024, 12, 31), "reagente", 15.50)
        estoque_inicial = insumo.quantidade
        
        registro = RegistroConsumo(insumo, datetime.date.today(), 5)
        
        assert insumo.quantidade == estoque_inicial - 5  # Estoque deve reduzir
        assert insumo.quantidade == 95
    
    def test_registro_str_representation(self):
        """Testa a representação em string do registro"""
        insumo = Insumo(1, "Reagente A", 100, datetime.date(2024, 12, 31), "reagente", 15.50)
        registro = RegistroConsumo(insumo, datetime.date(2024, 1, 15), 5)
        
        expected_str = "2024-01-15: Reagente A - 5 unidades - R$ 77.50"
        assert str(registro) == expected_str