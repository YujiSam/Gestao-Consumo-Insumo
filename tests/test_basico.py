import pytest
import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.insumo import Insumo
from models.registro_consumo import RegistroConsumo
from structures.fila_consumo import FilaConsumo
from structures.pilha_consulta import PilhaConsulta
from algorithms.busca import busca_sequencial
from algorithms.ordenacao import merge_sort_por_quantidade
from system.sistema_consumo import SistemaConsumo

def test_criacao_insumo():
    """TESTE BÁSICO 1: Verifica se a classe Insumo funciona"""
    insumo = Insumo(1, "Reagente A", 100, datetime.date(2024, 12, 31), "reagente", 15.50)
    assert insumo.nome == "Reagente A"
    assert insumo.quantidade == 100
    print("✅ Insumo criado corretamente")

def test_criacao_registro():
    """TESTE BÁSICO 2: Verifica se a classe RegistroConsumo funciona"""
    insumo = Insumo(1, "Reagente A", 100, datetime.date(2024, 12, 31), "reagente", 15.50)
    registro = RegistroConsumo(insumo, datetime.date.today(), 5)
    assert registro.quantidade_consumida == 5
    assert registro.custo_total == 77.5
    print("✅ Registro criado corretamente")

def test_registro_reduz_estoque():
    """TESTE BÁSICO 3: Verifica se o registro reduz o estoque"""
    insumo = Insumo(1, "Reagente A", 100, datetime.date(2024, 12, 31), "reagente", 15.50)
    registro = RegistroConsumo(insumo, datetime.date.today(), 5)
    assert insumo.quantidade == 95  # 100 - 5 = 95
    print("✅ Estoque reduzido corretamente")

def test_fila_basica():
    """TESTE BÁSICO 4: Verifica operações básicas da fila"""
    fila = FilaConsumo()
    insumo = Insumo(1, "Reagente A", 100, datetime.date(2024, 12, 31), "reagente", 15.50)
    registro = RegistroConsumo(insumo, datetime.date.today(), 5)
    
    fila.enfileirar(registro)
    assert fila.tamanho() == 1
    assert not fila.esta_vazia()
    
    registro_removido = fila.desenfileirar()
    assert registro_removido == registro
    assert fila.esta_vazia()
    print("✅ Fila funciona corretamente")

def test_pilha_basica():
    """TESTE BÁSICO 5: Verifica operações básicas da pilha"""
    pilha = PilhaConsulta()
    insumo = Insumo(1, "Reagente A", 100, datetime.date(2024, 12, 31), "reagente", 15.50)
    registro = RegistroConsumo(insumo, datetime.date.today(), 5)
    
    pilha.empilhar(registro)
    assert pilha.tamanho() == 1
    assert not pilha.esta_vazia()
    
    registro_removido = pilha.desempilhar()
    assert registro_removido == registro
    assert pilha.esta_vazia()
    print("✅ Pilha funciona corretamente")

def test_busca_sequencial_basica():
    """TESTE BÁSICO 6: Verifica busca sequencial simples"""
    insumo = Insumo(1, "Reagente A", 100, datetime.date(2024, 12, 31), "reagente", 15.50)
    registro = RegistroConsumo(insumo, datetime.date.today(), 5)
    
    resultados = busca_sequencial([registro], "Reagente A")
    assert len(resultados) == 1
    assert resultados[0] == registro
    print("✅ Busca sequencial funciona")

def test_ordenacao_basica():
    """TESTE BÁSICO 7: Verifica ordenação simples"""
    insumo = Insumo(1, "Reagente A", 100, datetime.date(2024, 12, 31), "reagente", 15.50)
    registro1 = RegistroConsumo(insumo, datetime.date.today(), 10)  # Quantidade: 10
    registro2 = RegistroConsumo(insumo, datetime.date.today(), 5)   # Quantidade: 5
    
    ordenados = merge_sort_por_quantidade([registro1, registro2])
    assert ordenados[0].quantidade_consumida == 5   # Menor primeiro
    assert ordenados[1].quantidade_consumida == 10  # Maior depois
    print("✅ Ordenação funciona")

def test_sistema_basico():
    """TESTE BÁSICO 8: Verifica criação básica do sistema"""
    sistema = SistemaConsumo()
    sistema.carregar_insumos_exemplo()
    
    assert len(sistema.insumos) > 0
    assert sistema.fila_consumo.esta_vazia()
    assert sistema.pilha_consulta.esta_vazia()
    assert len(sistema.registros_completos) == 0
    print("✅ Sistema criado corretamente")

def test_sistema_simulacao():
    """TESTE BÁSICO 9: Verifica simulação do sistema"""
    sistema = SistemaConsumo()
    sistema.carregar_insumos_exemplo()
    sistema.simular_consumo_diario(5)  # Simula 5 dias
    
    assert len(sistema.registros_completos) > 0
    assert not sistema.fila_consumo.esta_vazia()
    assert not sistema.pilha_consulta.esta_vazia()
    print("✅ Simulação do sistema funciona")

if __name__ == "__main__":
    """Executa todos os testes básicos quando o arquivo é rodado diretamente"""
    print("🚀 Executando Testes Básicos do Sistema...")
    print("=" * 50)
    
    # Lista de todos os testes básicos
    testes = [
        test_criacao_insumo,
        test_criacao_registro,
        test_registro_reduz_estoque,
        test_fila_basica,
        test_pilha_basica,
        test_busca_sequencial_basica,
        test_ordenacao_basica,
        test_sistema_basico,
        test_sistema_simulacao
    ]
    
    # Executa cada teste
    for teste in testes:
        try:
            teste()
            print(f"✅ {teste.__name__} - PASSOU")
        except Exception as e:
            print(f"❌ {teste.__name__} - FALHOU: {e}")
    
    print("=" * 50)
    print("🎉 Testes Básicos Concluídos!")