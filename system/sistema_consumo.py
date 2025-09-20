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
        
        # 🧪 CRIAR REAGENTES (produtos para exames)
        for i, nome in enumerate(nomes_reagentes):
            # Gera uma data de validade aleatória (entre 2 meses e 1 ano)
            validade = hoje + datetime.timedelta(days=random.randint(60, 365))
            # Quantidade aleatória em estoque (entre 200 e 500 unidades)
            quantidade = random.randint(200, 500)
            # Cria o produto e adiciona na lista de insumos
            self.insumos.append(Insumo(id_counter, nome, quantidade, validade, 'reagente', custos_reagentes[i]))
            id_counter += 1  # Próximo ID
        
        # 🧤 CRIAR DESCATÁVEIS (produtos de uso único)  
        for i, nome in enumerate(nomes_descartaveis):
            # Validade mais longa (entre 3 meses e 2 anos)
            validade = hoje + datetime.timedelta(days=random.randint(90, 730))
            # Maior quantidade em estoque (entre 300 e 800 unidades)
            quantidade = random.randint(300, 800)
            # Cria o produto e adiciona na lista
            self.insumos.append(Insumo(id_counter, nome, quantidade, validade, 'descartavel', custos_descartaveis[i]))
            id_counter += 1  # Próximo ID
    
    def simular_consumo_diario(self, dias: int = 30):
        """
        ⏰ SIMULA CONSUMO DIÁRIO: Cria registros de uso dos produtos
        
        Imagine que isso simula 30 dias de trabalho em um hospital:
        - Cada dia, alguns produtos são usados
        - A quantidade usada é aleatória
        - O estoque vai diminuindo com o tempo
        
        Parâmetro: dias = quantos dias quer simular (padrão: 30 dias)
        """
        hoje = datetime.date.today()  # Data atual
        
        # Para cada dia que vamos simular
        for dia in range(dias):
            # Calcula a data desse dia (começando de hoje e voltando no tempo)
            data = hoje - datetime.timedelta(days=dia)
            
            # 📋 Filtra apenas os produtos que ainda têm estoque
            insumos_disponiveis = [insumo for insumo in self.insumos if insumo.quantidade > 0]
            
            # Se não tiver mais produtos disponíveis, pula o dia
            if not insumos_disponiveis:
                continue  # Vai para o próximo dia
                
            # 🎲 Escolhe quantos produtos serão usados neste dia (2 a 5, ou menos se tiver poucos)
            num_consumos = random.randint(2, min(5, len(insumos_disponiveis)))
            # Escolhe aleatoriamente quais produtos serão usados
            insumos_do_dia = random.sample(insumos_disponiveis, num_consumos)
            
            # Para cada produto escolhido para ser usado neste dia
            for insumo in insumos_do_dia:
                # 🔢 Calcula quanto pode ser consumido (no máximo 20 unidades por vez)
                max_consumo_possivel = min(20, insumo.quantidade)
                
                # Se não tiver quantidade suficiente, pula este produto
                if max_consumo_possivel < 1:
                    continue
                
                # 📊 Define a quantidade mínima que pode ser consumida (1 unidade)
                min_consumo = 1
                
                # Se o máximo possível for menor que o mínimo, usa o máximo
                if max_consumo_possivel < min_consumo:
                    quantidade_consumida = max_consumo_possivel
                else:
                    # Gera uma quantidade aleatória entre 1 e o máximo possível
                    quantidade_consumida = random.randint(min_consumo, max_consumo_possivel)
                
                # ➖ Reduz a quantidade no estoque do produto
                insumo.quantidade -= quantidade_consumida
                
                # 📝 Cria um registro desse consumo
                registro = RegistroConsumo(insumo, data, quantidade_consumida)
                
                # 📥 Adiciona o registro em todas as estruturas:
                self.fila_consumo.enfileirar(registro)     # Na fila (ordem cronológica)
                self.pilha_consulta.empilhar(registro)     # Na pilha (ordem inversa)
                self.registros_completos.append(registro)  # Na lista completa (para buscas)
    
    # (Aqui viriam os outros métodos: busca_sequencial, busca_binaria_por_data, etc.)
    # que já foram implementados mas não estão mostrados neste trecho

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