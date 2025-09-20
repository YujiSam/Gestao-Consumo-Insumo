import datetime
from models.insumo import Insumo  # Importamos a classe Insumo para usar aqui

class RegistroConsumo:
    """
    CLASSE REGISTRO CONSUMO: Representa cada vez que alguém usa um produto
    
    Pense como um ticket de compra:
    - Insumo: qual produto foi usado
    - Data: quando foi usado
    - Quantidade Consumida: quantas unidades foram usadas
    - Custo Total: quanto custou esse uso (quantidade × preço unitário)
    """
    
    def __init__(self, insumo: Insumo, data: datetime.date, quantidade_consumida: int):
        self.insumo = insumo  # Qual produto foi usado
        self.data = data  # Data do uso
        self.quantidade_consumida = quantidade_consumida  # Quantas unidades usadas
        self.custo_total = quantidade_consumida * insumo.custo_unitario  # Custo total

        insumo.quantidade -= quantidade_consumida
    
    def __str__(self):
        """
        Como o registro será mostrado na tela
        Ex: "2024-01-15: Reagente A - 5 unidades - R$ 77.50"
        """
        return f"{self.data}: {self.insumo.nome} - {self.quantidade_consumida} unidades - R$ {self.custo_total:.2f}"