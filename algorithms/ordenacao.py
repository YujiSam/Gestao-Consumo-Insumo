from typing import List
from models.registro_consumo import RegistroConsumo

def merge_sort_por_quantidade(registros: List[RegistroConsumo]) -> List[RegistroConsumo]:
    """
    MERGE SORT: Ordena registros por quantidade consumida (do menor para o maior)
    
    FUNCIONA COMO: Separar cartas de baralho em montinhos pequenos, ordenar cada montinho
    e depois juntar tudo ordenado
    
    VANTAGEM: Sempre rápido, não importa como os dados estejam
    """
    if len(registros) <= 1:  # Se tiver 0 ou 1 registro, já está ordenado
        return registros
    
    meio = len(registros) // 2  # Divide a lista no meio
    # Ordena cada metade separadamente (isso chama a si mesmo - RECURSÃO)
    esquerda = merge_sort_por_quantidade(registros[:meio])  # Primeira metade
    direita = merge_sort_por_quantidade(registros[meio:])  # Segunda metade
    
    # Junta as duas metades ordenadas
    return _merge(esquerda, direita)

def _merge(esquerda: List[RegistroConsumo], direita: List[RegistroConsumo]) -> List[RegistroConsumo]:
    """
    FUNÇÃO AUXILIAR: Junta duas listas ordenadas em uma só lista ordenada
    
    FUNCIONA COMO: Juntar dois montinhos de cartas ordenados em um montinho maior ordenado
    """
    resultado = []  # Lista onde vamos juntar tudo
    i = j = 0  # Índices para percorrer as duas listas
    
    # Enquanto tiver elementos nas duas listas
    while i < len(esquerda) and j < len(direita):
        # Compara qual registro tem menor quantidade
        if esquerda[i].quantidade_consumida <= direita[j].quantidade_consumida:
            resultado.append(esquerda[i])  # Coloca o da esquerda primeiro
            i += 1  # Avança na lista da esquerda
        else:
            resultado.append(direita[j])  # Coloca o da direita primeiro
            j += 1  # Avança na lista da direita
    
    # Adiciona o que sobrou das listas (se alguma tiver ficado com elementos)
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado

def quick_sort_por_validade(registros: List[RegistroConsumo]) -> List[RegistroConsumo]:
    """
    QUICK SORT: Ordena registros por validade do produto (do que vence primeiro)
    
    FUNCIONA COMO: Escolher um produto do meio (pivô) e separar os outros em:
    - Menores: vencem antes do pivô
    - Iguais: vencem na mesma data do pivô  
    - Maiores: vencem depois do pivô
    
    VANTAGEM: Muito rápido na prática
    """
    if len(registros) <= 1:  # Lista vazia ou com 1 elemento já está ordenada
        return registros
    
    # Escolhe um elemento do meio como referência (chamado de pivô)
    pivo = registros[len(registros) // 2]
    
    # Separa os registros em três grupos:
    menores = [r for r in registros if r.insumo.validade < pivo.insumo.validade]  # Vencem antes
    iguais = [r for r in registros if r.insumo.validade == pivo.insumo.validade]  # Mesma data
    maiores = [r for r in registros if r.insumo.validade > pivo.insumo.validade]  # Vencem depois
    
    # Ordena os menores e maiores, e junta tudo
    return quick_sort_por_validade(menores) + iguais + quick_sort_por_validade(maiores)