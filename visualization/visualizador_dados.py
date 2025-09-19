import pandas as pd
from tabulate import tabulate
from typing import List
import matplotlib.pyplot as plt
import numpy as np
from models.insumo import Insumo
from models.registro_consumo import RegistroConsumo

class VisualizadorDados:
    """
    🎨 VISUALIZADOR DE DADOS: Transforma números em gráficos que qualquer um entende!
    
    Pense como um painel de controle de hospital onde:
    - Cores mostram situações críticas
    - Gráficos mostram tendências
    - Qualquer pessoa vê e entende a situação
    """

    # ... (os métodos anteriores de tabelas aqui) ...

    @staticmethod
    def gerar_grafico_consumo_diario(registros: List[RegistroConsumo]):
        """
        📅 GRÁFICO DE CONSUMO DIÁRIO: Mostra quanto foi consumido cada dia
        
        IDEIA: Ver em quais dias o hospital mais consumiu insumos
        CORES: Azul claro → consumo normal / Azul escuro → picos de consumo
        """
        if not registros:
            print("📊 Nenhum dado para gerar gráfico de consumo diário")
            return
        
        df = VisualizadorDados.criar_dataframe_consumo(registros)
        consumo_diario = df.groupby('Data')['Quantidade'].sum()
        
        # Configura o gráfico
        plt.figure(figsize=(12, 6))
        barras = consumo_diario.plot(kind='bar', color='skyblue', edgecolor='black', alpha=0.7)
        
        # Personaliza o gráfico
        plt.title('📈 CONSUMO DIÁRIO DE INSUMOS', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Data', fontsize=12)
        plt.ylabel('Unidades Consumidas', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', alpha=0.3)
        
        # Adiciona valores nas barras
        for i, valor in enumerate(consumo_diario):
            plt.text(i, valor + 0.1, f'{valor}', ha='center', va='bottom', fontsize=9)
        
        plt.tight_layout()
        plt.show()

    @staticmethod
    def gerar_grafico_top_insumos(registros: List[RegistroConsumo], top_n: int = 5):
        """
        🏆 TOP INSUMOS: Mostra os produtos mais consumidos
        
        IDEIA: Saber quais produtos gastamos mais
        CORES: Vermelho → mais consumidos / Laranja → menos consumidos
        """
        if not registros:
            print("📊 Nenhum dado para gerar gráfico de top insumos")
            return
        
        df = VisualizadorDados.criar_dataframe_consumo(registros)
        consumo_por_insumo = df.groupby('Insumo')['Quantidade'].sum().nlargest(top_n)
        
        plt.figure(figsize=(12, 6))
        cores = plt.cm.Reds(np.linspace(0.5, 0.9, len(consumo_por_insumo)))
        barras = plt.bar(consumo_por_insumo.index, consumo_por_insumo.values, color=cores, edgecolor='darkred')
        
        plt.title(f'🏆 TOP {top_n} INSUMOS MAIS CONSUMIDOS', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Insumos', fontsize=12)
        plt.ylabel('Total Consumido (unidades)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', alpha=0.3)
        
        # Adiciona valores nas barras
        for bar, valor in zip(barras, consumo_por_insumo.values):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                    f'{valor}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        plt.show()

    @staticmethod
    def gerar_grafico_custo_por_tipo(registros: List[RegistroConsumo]):
        """
        💰 CUSTO POR TIPO: Mostra quanto gastamos com reagentes vs descartáveis
        
        IDEIA: Saber onde está indo mais dinheiro
        CORES: Azul → reagentes / Verde → descartáveis
        """
        if not registros:
            print("📊 Nenhum dado para gerar gráfico de custos")
            return
        
        df = VisualizadorDados.criar_dataframe_consumo(registros)
        custo_por_tipo = df.groupby('Tipo')['Custo Total'].sum()
        
        plt.figure(figsize=(10, 7))
        cores = ['#FF6B6B', '#4ECDC4']  # Vermelho para reagentes, Verde para descartáveis
        explode = (0.1, 0)  # Destaca a fatia maior
        
        plt.pie(custo_por_tipo.values, labels=custo_por_tipo.index, autopct='%1.1f%%',
                colors=cores, startangle=90, explode=explode, shadow=True)
        
        plt.title('💰 DISTRIBUIÇÃO DE CUSTOS POR TIPO', fontsize=16, fontweight='bold', pad=20)
        plt.axis('equal')
        plt.show()

    @staticmethod
    def gerar_grafico_estoque_baixo(insumos: List[Insumo]):
        """
        ⚠️ ESTOQUE BAIXO: Alerta visual dos produtos que estão acabando
        
        IDEIA: Ver rapidamente o que precisa ser comprado URGENTE
        CORES: Vermelho → crítico / Laranja → baixo / Verde → ok
        """
        # Filtra insumos com menos de 50 unidades
        insumos_baixos = [i for i in insumos if i.quantidade < 50]
        
        if not insumos_baixos:
            print("✅ Todos os insumos com estoque suficiente!")
            return
        
        nomes = [i.nome for i in insumos_baixos]
        quantidades = [i.quantidade for i in insumos_baixos]
        
        # Define cores baseadas na quantidade
        cores = []
        for qtd in quantidades:
            if qtd < 10:
                cores.append('red')     # Crítico - VERMELHO
            elif qtd < 30:
                cores.append('orange')  # Baixo - LARANJA
            else:
                cores.append('yellow')  # Atenção - AMARELO
        
        plt.figure(figsize=(12, 6))
        barras = plt.bar(nomes, quantidades, color=cores, edgecolor='black', alpha=0.8)
        
        plt.title('⚠️ ALERTA: INSUMOS COM ESTOQUE BAIXO', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Insumos', fontsize=12)
        plt.ylabel('Unidades em Estoque', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', alpha=0.3)
        
        # Linha de alerta
        plt.axhline(y=10, color='red', linestyle='--', alpha=0.7, label='Nível Crítico (10 unidades)')
        plt.axhline(y=30, color='orange', linestyle='--', alpha=0.7, label='Nível Baixo (30 unidades)')
        
        # Valores nas barras
        for bar, valor in zip(barras, quantidades):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                    f'{valor}', ha='center', va='bottom', fontweight='bold')
        
        plt.legend()
        plt.tight_layout()
        plt.show()

    @staticmethod
    def gerar_grafico_validade_proxima(insumos: List[Insumo], dias_limite: int = 30):
        """
        ⏰ VALIDADE PRÓXIMA: Mostra produtos que vencem em breve
        
        IDEIA: Evitar perder produtos por vencimento
        CORES: Vermelho → vence em 7 dias / Laranja → vence em 30 dias
        """
        from datetime import date
        hoje = date.today()
        
        # Filtra insumos que vencem nos próximos dias
        insumos_proximos = []
        for insumo in insumos:
            if insumo.quantidade > 0:  # Só os que têm estoque
                dias_restantes = (insumo.validade - hoje).days
                if 0 <= dias_restantes <= dias_limite:
                    insumos_proximos.append((insumo, dias_restantes))
        
        if not insumos_proximos:
            print(f"✅ Nenhum insumo vence nos próximos {dias_limite} dias!")
            return
        
        # Ordena por validade mais próxima
        insumos_proximos.sort(key=lambda x: x[1])
        
        nomes = [f"{i[0].nome}\n({i[0].validade})" for i in insumos_proximos]
        dias = [i[1] for i in insumos_proximos]
        quantidades = [i[0].quantidade for i in insumos_proximos]
        
        # Cores baseadas na urgência
        cores = []
        for d in dias:
            if d <= 7:
                cores.append('red')
            elif d <= 15:
                cores.append('orange')
            else:
                cores.append('gold')
        
        plt.figure(figsize=(14, 7))
        barras = plt.bar(nomes, quantidades, color=cores, edgecolor='black', alpha=0.8)
        
        plt.title(f'⏰ INSUMOS COM VALIDADE PRÓXIMA (próximos {dias_limite} dias)', 
                fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Insumo (Data de Validade)', fontsize=12)
        plt.ylabel('Quantidade em Estoque', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', alpha=0.3)
        
        # Adiciona dias restantes
        for bar, dias_restantes, qtd in zip(barras, dias, quantidades):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                    f'{dias_restantes}d', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        plt.show()

    @staticmethod
    def gerar_dashboard_completo(registros: List[RegistroConsumo], insumos: List[Insumo]):
        """
        🎛️ DASHBOARD COMPLETO: Todos os gráficos importantes de uma vez!
        
        IDEIA: Painel de controle com visão geral completa
        """
        print("🚀 GERANDO DASHBOARD COMPLETO...")
        print("="*60)
        
        # Gera todos os gráficos sequencialmente
        VisualizadorDados.gerar_grafico_consumo_diario(registros)
        VisualizadorDados.gerar_grafico_top_insumos(registros)
        VisualizadorDados.gerar_grafico_custo_por_tipo(registros)
        VisualizadorDados.gerar_grafico_estoque_baixo(insumos)
        VisualizadorDados.gerar_grafico_validade_proxima(insumos)
        
        print("✅ Dashboard completo gerado!")