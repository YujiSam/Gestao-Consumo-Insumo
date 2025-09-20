import datetime
import random
from typing import List
from models.insumo import Insumo
from models.registro_consumo import RegistroConsumo
from structures.fila_consumo import FilaConsumo
from structures.pilha_consulta import PilhaConsulta
from algorithms.busca import busca_sequencial, busca_binaria_por_data
from algorithms.ordenacao import merge_sort_por_quantidade, quick_sort_por_validade

class SistemaConsumo:
    """
    🏥 SISTEMA PRINCIPAL DE GESTÃO DE CONSUMO
    
    Esta é a classe mais importante que coordena tudo:
    - Gerencia o estoque de insumos
    - Controla os registros de consumo  
    - Usa todas as estruturas e algoritmos juntos
    - É o "cérebro" do sistema completo
    
    Pense como o gerente de uma farmácia que:
    1. Mantém o controle de todos os produtos
    2. Registra cada vez que alguém usa algo
    3. Gera relatórios sobre o que foi usado
    4. Avisa quando está faltando algo
    """
    
    def __init__(self):
        """
        CONSTRUTOR: Inicializa o sistema com tudo vazio
        
        É como abrir uma loja nova:
        - Estoque vazio
        - Nenhuma venda registrada
        - Caixa registradora zerada
        """
        self.fila_consumo = FilaConsumo()        # Para ordem cronológica (FIFO)
        self.pilha_consulta = PilhaConsulta()    # Para consulta inversa (LIFO)  
        self.insumos: List[Insumo] = []          # Lista de todos os produtos em estoque
        self.registros_completos: List[RegistroConsumo] = []  # Histórico de tudo que foi consumido
    
    def carregar_insumos_exemplo(self):
        """
        📦 CARREGA DADOS DE EXEMPLO: Cria produtos fictícios para testar o sistema
        
        É como abastecer o estoque pela primeira vez com:
        - Reagentes: produtos para fazer exames (mais caros)
        - Descartáveis: produtos de uso único (mais baratos)
        """
        # Lista de nomes de produtos que teremos no sistema
        nomes_reagentes = ['Reagente A', 'Reagente B', 'Reagente C', 'Reagente D']
        nomes_descartaveis = ['Luvas', 'Máscaras', 'Tubos', 'Agulhas']
        
        # Preços de cada produto (em reais)
        custos_reagentes = [15.50, 22.30, 18.75, 35.20]        # Reagentes são mais caros
        custos_descartaveis = [2.10, 1.50, 3.75, 0.95]         # Descartáveis são mais baratos
        
        id_counter = 1  # Contador para dar um ID único para cada produto
        hoje = datetime.date.today()  # Data de hoje
        
        # Criar reagentes
        for i, nome in enumerate(nomes_reagentes):
            # Sorteia o tipo de validade
            tipo_validade = random.choice(['dentro', 'proximo', 'vencido_recente', 'muito_vencido'])
            
            if tipo_validade == 'dentro':
                dias = random.randint(60, 365)  # Dentro da validade
            elif tipo_validade == 'proximo':
                dias = random.randint(1, 30)    # Próximo a vencer
            elif tipo_validade == 'vencido_recente':
                dias = random.randint(-30, -1)  # Vencido recentemente
            else:  # muito_vencido
                dias = random.randint(-365, -31)  # Muito vencido
            
            validade = hoje + datetime.timedelta(days=dias)
            quantidade = random.randint(200, 500)
            self.insumos.append(Insumo(id_counter, nome, quantidade, validade, 'reagente', custos_reagentes[i]))
            id_counter += 1
        
        # Criar descartáveis (com mesma lógica)
        for i, nome in enumerate(nomes_descartaveis):
            tipo_validade = random.choice(['dentro', 'proximo', 'vencido_recente', 'muito_vencido'])
            
            if tipo_validade == 'dentro':
                dias = random.randint(90, 730)
            elif tipo_validade == 'proximo':
                dias = random.randint(1, 30)
            elif tipo_validade == 'vencido_recente':
                dias = random.randint(-30, -1)
            else:
                dias = random.randint(-365, -31)
            
            validade = hoje + datetime.timedelta(days=dias)
            quantidade = random.randint(300, 800)
            self.insumos.append(Insumo(id_counter, nome, quantidade, validade, 'descartavel', custos_descartaveis[i]))
            id_counter += 1
    
    def simular_consumo_diario(self, dias: int = 30):
        """
        ⏰ SIMULA CONSUMO DIÁRIO: Cria registros de uso dos produtos
        
        Imagine que isso simula 30 dias de trabalho em um hospital:
        - Cada dia, alguns produtos são usados
        - A quantidade usada é aleatória
        - O estoque vai diminuindo com o tempo
        
        Parâmetro: dias = quantos dias quer simular (padrão: 30 dias)
        """
        hoje = datetime.date.today()
    
        for dia in range(dias):
            data = hoje - datetime.timedelta(days=dia)
            
            for insumo in self.insumos:
                if insumo.quantidade < 0:
                    insumo.quantidade = 0
            
            # Filtra apenas insumos com estoque positivo
            insumos_disponiveis = [insumo for insumo in self.insumos if insumo.quantidade > 0]
            
            if not insumos_disponiveis:
                print(f"📅 {data}: Todos os insumos esgotados")
                continue
                    
            num_consumos = random.randint(2, min(5, len(insumos_disponiveis)))
            insumos_do_dia = random.sample(insumos_disponiveis, num_consumos)
            
            for insumo in insumos_do_dia:
                # 🛡️ PROTEÇÃO MÁXIMA: Verifica estoque novamente
                if insumo.quantidade <= 0:
                    continue
                    
                # Calcula consumo seguro
                max_consumo = min(20, insumo.quantidade)
                if max_consumo <= 0:
                    continue
                    
                quantidade_consumida = random.randint(1, max_consumo)
                
                # 🎯 GARANTIA FINAL: Não deixa ficar negativo
                if quantidade_consumida > insumo.quantidade:
                    quantidade_consumida = insumo.quantidade
                
                # Atualiza estoque
                insumo.quantidade -= quantidade_consumida
                
                # Cria registro
                registro = RegistroConsumo(insumo, data, quantidade_consumida)
                self.fila_consumo.enfileirar(registro)
                self.pilha_consulta.empilhar(registro)
                self.registros_completos.append(registro)

    def busca_sequencial(self, nome_insumo: str):
        """Busca sequencial dentro dos registros do sistema"""
        from algorithms.busca import busca_sequencial as busca_seq
        return busca_seq(self.registros_completos, nome_insumo)
    
    def merge_sort_por_quantidade(self, registros: List[RegistroConsumo]):
        """Ordena registros por quantidade usando merge sort"""
        from algorithms.ordenacao import merge_sort_por_quantidade as merge_sort
        return merge_sort(registros)
    
    def quick_sort_por_validade(self, registros: List[RegistroConsumo]):
        """Ordena registros por validade usando quick sort"""
        from algorithms.ordenacao import quick_sort_por_validade as quick_sort
        return quick_sort(registros)

    def gerar_relatorio_completo(self):
        """Gera um relatório completo com todos os dados"""
        print("=" * 80)
        print("📋 RELATÓRIO COMPLETO DO SISTEMA")
        print("=" * 80)
        
        # 1. Mostra estoque atual
        print("\n📦 ESTOQUE ATUAL:")
        print("-" * 40)
        for insumo in self.insumos:
            print(f"• {insumo.nome}: {insumo.quantidade} unidades (Validade: {insumo.validade})")
        
        # 2. Mostra estatísticas básicas
        print(f"\n📊 ESTATÍSTICAS:")
        print("-" * 40)
        print(f"• Total de insumos: {len(self.insumos)}")
        print(f"• Total de registros: {len(self.registros_completos)}")
        
        if self.registros_completos:
            consumo_total = sum(r.quantidade_consumida for r in self.registros_completos)
            custo_total = sum(r.custo_total for r in self.registros_completos)
            print(f"• Consumo total: {consumo_total} unidades")
            print(f"• Custo total: R$ {custo_total:.2f}")
        
        # 3. Testa a fila (ordem cronológica)
        print(f"\n⏰ PRIMEIROS REGISTROS (FILA - ORDEM CRONOLÓGICA):")
        print("-" * 60)
        for i, registro in enumerate(self.fila_consumo.registros[:3]):
            print(f"{i+1}. {registro}")
        
        # 4. Testa a pilha (ordem inversa)
        print(f"\n🔙 ÚLTIMOS REGISTROS (PILHA - ORDEM INVERSA):")
        print("-" * 60)
        ultimos = self.pilha_consulta.registros[-3:] if self.pilha_consulta.registros else []
        for i, registro in enumerate(reversed(ultimos)):
            print(f"{i+1}. {registro}")
        
        # 5. Testa busca sequencial
        print(f"\n🔍 BUSCA SEQUENCIAL ('Reagente A'):")
        print("-" * 40)
        resultados = self.busca_sequencial("Reagente A")
        for i, registro in enumerate(resultados[:2]):
            print(f"{i+1}. {registro}")
        if len(resultados) > 2:
            print(f"... e mais {len(resultados) - 2} registros")
        
        # 6. Testa ordenação
        if self.registros_completos:
            print(f"\n📊 ORDENAÇÃO POR QUANTIDADE (TOP 3):")
            print("-" * 40)
            ordenados = self.merge_sort_por_quantidade(self.registros_completos[:3])
            for i, registro in enumerate(ordenados):
                print(f"{i+1}. {registro.insumo.nome}: {registro.quantidade_consumida} unidades")
        
# 💡 NOTA: Os métodos de busca e ordenação já estão implementados,
# mas como estão em arquivos separados (algorithms/busca.py e algorithms/ordenacao.py),
# não precisam ser repetidos aqui. O sistema já pode usá-los através dos imports!