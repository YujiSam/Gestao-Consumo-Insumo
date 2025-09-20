# ver_graficos.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from system.sistema_consumo import SistemaConsumo
from visualization.visualizador_dados import VisualizadorDados

def main():
    print("GERANDO OS GRÁFICOS...")
    
    # Cria e carrega o sistema
    sistema = SistemaConsumo()
    sistema.carregar_insumos_exemplo()
    sistema.simular_consumo_diario(30)
    
    # Gera apenas os gráficos
    print("📈 Gerando gráfico de consumo diário...")
    VisualizadorDados.gerar_grafico_consumo_diario(sistema.registros_completos)
    
    print("🏆 Gerando gráfico dos insumos mais consumidos...")
    VisualizadorDados.gerar_grafico_top_insumos(sistema.registros_completos)
    
    print("💰 Gerando gráfico de custos por tipo...")
    VisualizadorDados.gerar_grafico_custo_por_tipo(sistema.registros_completos)
    
    print("⚠️  Gerando gráfico de estoque baixo...")
    VisualizadorDados.gerar_grafico_estoque_baixo(sistema.insumos)
    
    print("⏰ Gerando gráfico de validades próximas...")
    VisualizadorDados.gerar_grafico_validade_proxima(sistema.insumos)
    
    print("✅ Todos os gráficos gerados!")

if __name__ == "__main__":
    main()