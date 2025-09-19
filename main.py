from system.sistema_consumo import SistemaConsumo

def main():
    print("🚀 Iniciando Sistema de Gestão de Consumo de Insumos...")
    
    sistema = SistemaConsumo()
    sistema.carregar_insumos_exemplo()
    sistema.simular_consumo_diario(30)
    
    print("✅ Sistema executado com sucesso!")

if __name__ == "__main__":
    main()