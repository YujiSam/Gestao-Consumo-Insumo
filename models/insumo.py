import datetime

class Insumo:
    """
    CLASSE INSUMO: Representa cada item médico que será controlado no sistema
    
    Pense como se fosse uma ficha de cada produto:
    - ID: número de identificação único (como um RG do produto)
    - Nome: como o produto é chamado (ex: "Reagente A", "Luvas")
    - Quantidade: quanto temos em estoque no momento
    - Validade: até quando o produto pode ser usado (data importante!)
    - Tipo: se é "reagente" (para exames) ou "descartavel" (uso único)
    - Custo Unitário: quanto custa cada unidade desse produto
    """
    
    def __init__(self, id: int, nome: str, quantidade: int, validade: datetime.date, 
                tipo: str, custo_unitario: float):
        # Aqui estamos criando a "ficha" do produto com todas as informações
        self.id = id  # Número identificador
        self.nome = nome  # Nome do produto
        self.quantidade = quantidade  # Quantidade em estoque
        self.validade = validade  # Data de validade
        self.tipo = tipo  # Tipo: reagente ou descartavel
        self.custo_unitario = custo_unitario  # Preço de cada unidade
    
    def __str__(self):
        """
        Como o produto será mostrado quando imprimirmos na tela
        Ex: "Reagente A (ID: 1) - 100 unidades - Validade: 2024-12-31 - R$ 15.50"
        """
        return f"{self.nome} (ID: {self.id}) - {self.quantidade} unidades - Validade: {self.validade} - R$ {self.custo_unitario:.2f}"