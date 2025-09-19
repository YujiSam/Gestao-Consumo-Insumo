"""
PACOTE ALGORITHMS: Contém os algoritmos de busca e ordenação
"""
from .busca import busca_sequencial, busca_binaria_por_data
from .ordenacao import merge_sort_por_quantidade, quick_sort_por_validade

__all__ = [
    'busca_sequencial', 
    'busca_binaria_por_data',
    'merge_sort_por_quantidade', 
    'quick_sort_por_validade'
]