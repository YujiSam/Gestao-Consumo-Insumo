from datetime import datetime, timedelta
import random
from typing import List, Tuple, Optional
from models.insumo import Insumo
from models.registro_consumo import RegistroConsumo
from structures.fila_consumo import FilaConsumo
from structures.pilha_consulta import PilhaConsulta
from algorithms.busca import busca_sequencial, busca_binaria_por_data
from algorithms.ordenacao import merge_sort_por_quantidade, quick_sort_por_validade
from algorithms.pd_consumo import consumo_otimo_rec, consumo_otimo_memo, consumo_otimo_iterativo

class SistemaConsumo:
    """
    SISTEMA PRINCIPAL DE GESTÃO DE CONSUMO
    """

    def __init__(self):
        self.fila_consumo = FilaConsumo()
        self.pilha_consulta = PilhaConsulta()
        self.insumos: List[Insumo] = []
        self.registros_completos: List[RegistroConsumo] = []

    def carregar_insumos_exemplo(self):
        """
        Carrega insumos de exemplo com quantidades e validade.
        Ajuste os ranges aqui se quiser cenários diferentes.
        """
        nomes_reagentes = ['Reagente A', 'Reagente B', 'Reagente C', 'Reagente D']
        nomes_descartaveis = ['Luvas', 'Máscaras', 'Tubos', 'Agulhas']

        custos_reagentes = [15.50, 22.30, 18.75, 35.20]
        custos_descartaveis = [2.10, 1.50, 3.75, 0.95]

        id_counter = 1
        hoje = datetime.today().date()

        # Reagentes (estoque menor)
        for i, nome in enumerate(nomes_reagentes):
            tipo_validade = random.choice(['dentro', 'proximo', 'vencido_recente', 'muito_vencido'])
            if tipo_validade == 'dentro':
                dias = random.randint(60, 365)
            elif tipo_validade == 'proximo':
                dias = random.randint(1, 30)
            elif tipo_validade == 'vencido_recente':
                dias = random.randint(-30, -1)
            else:
                dias = random.randint(-365, -31)

            validade = hoje + timedelta(days=dias)
            quantidade = random.randint(20, 100)  # reagentes: estoque menor
            self.insumos.append(Insumo(id_counter, nome, quantidade, validade, 'reagente', custos_reagentes[i]))
            id_counter += 1

        # Descartáveis (estoque maior)
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

            validade = hoje + timedelta(days=dias)
            quantidade = random.randint(20, 100)  # descartáveis: estoque maior
            self.insumos.append(Insumo(id_counter, nome, quantidade, validade, 'descartavel', custos_descartaveis[i]))
            id_counter += 1

    def simular_consumo_diario(self, dias: int = 30):
        """
        Simula consumo diário durante `dias` dias.
        Usa RegistroConsumo para registrar e decrementar estoque corretamente.
        """
        hoje = datetime.today().date()

        for dia in range(dias):
            data = hoje - timedelta(days=dia)  # dia atual da simulação
            insumos_disponiveis = [i for i in self.insumos if i.quantidade > 0]

            if not insumos_disponiveis:
                print(f"📅 {data}: Todos os insumos esgotados")
                continue

            # Número de insumos que serão usados nesse dia (1..max)
            max_consumos = min(3, len(insumos_disponiveis))  # reduzir para deixar mais realista
            num_consumos = random.randint(1, max_consumos)

            insumos_do_dia = random.sample(insumos_disponiveis, num_consumos)

            for insumo in insumos_do_dia:
                # consumo por item (mais conservador)
                max_consumo = min(5, insumo.quantidade)  # menor pico por dia
                if max_consumo <= 0:
                    continue
                quantidade_consumida = random.randint(1, max_consumo)

                # cria registro (RegistroConsumo já decrementa insumo.quantidade)
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

    def calcular_consumo_otimo(self, bloco: int = 50, modo_teste_recursivo: bool = True):
        """
        Calcula consumo ótimo usando as três versões (recursiva, memorização e iterativa).
        - bloco: discretização usada por memo e iterativa (maior -> mais rápido, menos preciso)
        - modo_teste_recursivo: se True, roda também a recursiva em estoques pequenos
        Retorna tupla: (rec, memo, iterativo)
        """
        estoques = [i.quantidade for i in self.insumos]
        print("📦 Estoques detectados:", estoques)
        print(f"🧠 Parâmetros: bloco={bloco}, modo_teste_recursivo={modo_teste_recursivo}")

        rec_res = None
        # Só roda recursiva se a lista for pequena para não travar
        if modo_teste_recursivo:
            if len(estoques) <= 10 and max(estoques, default=0) <= 100:
                print("▶️ Rodando versão recursiva...")
                rec_res = consumo_otimo_rec(estoques, bloco=bloco)
                print("   ✅ Resultado recursiva:", rec_res)
            else:
                print("⚠️ Pulando recursiva: estoques muito grandes para rodar recursivo puro.")

        print("▶️ Rodando versão com memorização...")
        memo_res = consumo_otimo_memo(estoques, bloco=bloco)
        print("   ✅ Resultado memorização:", memo_res)

        print("▶️ Rodando versão iterativa (bottom-up)...")
        iter_res = consumo_otimo_iterativo(estoques, bloco=bloco)
        print("   ✅ Resultado iterativa:", iter_res)

        # Verificação de consistência
        if rec_res is not None:
            consistent = (rec_res == memo_res == iter_res)
        else:
            # Se recursiva não rodou, verificamos memo vs iterativa com tolerância
            tol = max(1, int(0.05 * sum(estoques) / bloco))  # heurística
            consistent = (abs(memo_res - iter_res) <= tol)

        print("🧩 Verificando consistência dos resultados...")
        if not consistent:
            print(f"⚠️ Resultados PD diferentes: rec={rec_res}, memo={memo_res}, iterativo={iter_res}")
        else:
            print("✅ Resultados PD consistentes")

        print(f"📊 Desperdício (memo): {memo_res}  |  (iterativo): {iter_res}")
        print("🏁 Cálculo de consumo ótimo finalizado com sucesso.")
        return rec_res, memo_res, iter_res

