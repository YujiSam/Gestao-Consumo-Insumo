import pytest
import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from system.sistema_consumo import SistemaConsumo
from models.insumo import Insumo
from models.registro_consumo import RegistroConsumo

class TestSistema:
    """Testes para a classe SistemaConsumo"""
    
    def test_sistema_inicializacao(self):
        """Testa se o sistema é inicializado corretamente"""
        sistema = SistemaConsumo()
        
        assert sistema.insumos == []
        assert sistema.registros_completos == []
        assert sistema.fila_consumo.esta_vazia()
        assert sistema.pilha_consulta.esta_vazia()
    
    def test_carregar_insumos_exemplo(self):
        """Testa se o sistema carrega insumos de exemplo corretamente"""
        sistema = SistemaConsumo()
        sistema.carregar_insumos_exemplo()
        
        # Deve ter 8 insumos (4 reagentes + 4 descartáveis)
        assert len(sistema.insumos) == 8
        
        # Verifica se tem ambos os tipos
        tipos = [insumo.tipo for insumo in sistema.insumos]
        assert 'reagente' in tipos
        assert 'descartavel' in tipos
        
        # Verifica se todos têm quantidade positiva
        for insumo in sistema.insumos:
            assert insumo.quantidade > 0
            assert insumo.custo_unitario > 0
    
    def test_simular_consumo_diario(self):
        """Testa a simulação de consumo diário"""
        sistema = SistemaConsumo()
        sistema.carregar_insumos_exemplo()
        
        # Simula 5 dias de consumo
        sistema.simular_consumo_diario(5)
        
        # Deve ter registros de consumo
        assert len(sistema.registros_completos) > 0
        
        # As estruturas não devem estar vazias
        assert not sistema.fila_consumo.esta_vazia()
        assert not sistema.pilha_consulta.esta_vazia()
        
        # A fila e pilha devem ter o mesmo número de registros
        assert sistema.fila_consumo.tamanho() == len(sistema.registros_completos)
        assert sistema.pilha_consulta.tamanho() == len(sistema.registros_completos)
    
    def test_busca_sequencial_sistema(self):
        """Testa a busca sequencial integrada no sistema"""
        sistema = SistemaConsumo()
        sistema.carregar_insumos_exemplo()
        sistema.simular_consumo_diario(10)
        
        # Busca por um insumo que deve existir
        resultados = sistema.busca_sequencial("Reagente A")
        assert resultados is not None
        
        # Se encontrou resultados, verifica se são do insumo correto
        if resultados:
            for registro in resultados:
                assert registro.insumo.nome == "Reagente A"
    
    def test_ordenacao_sistema(self):
        """Testa a ordenação integrada no sistema"""
        sistema = SistemaConsumo()
        sistema.carregar_insumos_exemplo()
        sistema.simular_consumo_diario(10)
        
        # Testa ordenação por quantidade
        if sistema.registros_completos:
            ordenados = sistema.merge_sort_por_quantidade(sistema.registros_completos[:5])
            
            # Verifica se está ordenado (menor para maior)
            quantidades = [r.quantidade_consumida for r in ordenados]
            assert quantidades == sorted(quantidades)
        
        # Testa ordenação por validade
        if sistema.registros_completos:
            ordenados = sistema.quick_sort_por_validade(sistema.registros_completos[:5])
            
            # Verifica se está ordenado por validade
            validades = [r.insumo.validade for r in ordenados]
            assert validades == sorted(validades)
    
    def test_estoque_apos_consumo(self):
        """Testa se o estoque é reduzido corretamente após o consumo"""
        sistema = SistemaConsumo()
        sistema.carregar_insumos_exemplo()
        
        # Guarda estoque inicial
        estoque_inicial = {insumo.nome: insumo.quantidade for insumo in sistema.insumos}
        
        # Simula consumo
        sistema.simular_consumo_diario(10)
        
        # Verifica se o estoque foi reduzido
        for insumo in sistema.insumos:
            if insumo.quantidade > 0:  # Apenas se ainda tiver estoque
                assert insumo.quantidade <= estoque_inicial[insumo.nome]
    
    def test_gerar_relatorio_completo(self):
        """Testa se o relatório completo é gerado sem erros"""
        sistema = SistemaConsumo()
        sistema.carregar_insumos_exemplo()
        sistema.simular_consumo_diario(5)
        
        # Esta função deve executar sem lançar exceções
        try:
            sistema.gerar_relatorio_completo()
            assert True  # Se chegou aqui, não houve erro
        except Exception as e:
            pytest.fail(f"gerar_relatorio_completo() falhou com erro: {e}")