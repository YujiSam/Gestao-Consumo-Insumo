from typing import List, Optional
import datetime
from models.registro_consumo import RegistroConsumo

def busca_sequencial(registros: List[RegistroConsumo], nome_insumo: str) -> List[RegistroConsumo]:
    """
    BUSCA SEQUENCIAL: Procura um produto olhando registro por registro
    
    FUNCIONA COMO: Procurar um nome na lista telefônica página por página
    VANTAGEM: Funciona em qualquer ordem, sempre acha se existir
    DESVANTAGEM: Pode ser lento se tiver muitos registros
    
    Retorna TODOS os registros que encontrarmos do produto
    """
    resultados = []  # Lista vazia para guardar o que encontrarmos
    
    # Vamos olhar cada registro um por um
    for registro in registros:
        # Se o nome do produto bater (ignorando maiúsculas/minúsculas)
        if registro.insumo.nome.lower() == nome_insumo.lower():
            resultados.append(registro)  # Adiciona na lista de resultados
    
    return resultados  # Retorna tudo que encontramos

def busca_binaria_por_data(registros: List[RegistroConsumo], data_alvo: datetime.date) -> Optional[RegistroConsumo]:
    """
    BUSCA BINÁRIA: Procura por data de forma inteligente e rápida
    
    FUNCIONA COMO: Procurar uma palavra no dicionário - vai direto para a letra certa
    VANTAGEM: Muito rápido, mesmo com milhões de registros
    DESVANTAGEM: Precisa que os registros estejem ORDENADOS por data
    
    Retorna UM registro da data específica ou None se não achar
    """
    if not registros:  # Se não tiver registros, retorna vazio
        return None
        
    # Primeiro ordenamos os registros por data (do mais antigo para o mais recente)
    registros_ordenados = sorted(registros, key=lambda x: x.data)
    
    # Configuramos onde começar e terminar a busca
    esquerda, direita = 0, len(registros_ordenados) - 1
    
    # Enquanto tiver registros para procurar
    while esquerda <= direita:
        meio = (esquerda + direita) // 2  # Pega o registro do meio
        registro_meio = registros_ordenados[meio]  # Registro do meio
        
        if registro_meio.data == data_alvo:  # Achou a data certa!
            return registro_meio
        elif registro_meio.data < data_alvo:  # Data do meio é mais antiga
            esquerda = meio + 1  # Procura na metade direita (datas mais recentes)
        else:  # Data do meio é mais recente
            direita = meio - 1  # Procura na metade esquerda (datas mais antigas)
    
    return None  # Não encontrou a data