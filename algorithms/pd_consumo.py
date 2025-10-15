# algorithms/pd_consumo.py
from functools import lru_cache
from typing import List, Tuple

def _normalizar_estoques(estoques: List[int], bloco: int) -> Tuple[int, ...]:
    """
    Normaliza estoques usando o bloco.
    Garante que cada estoque >= 1 (mantém mínimos para a PD).
    """
    return tuple(max(1, (q + bloco - 1) // bloco) for q in estoques)  # arredonda para cima

# ---------------------------
# 1) Recursiva (apenas para testes pequenos)
# ---------------------------
def consumo_otimo_rec(estoques: List[int], dia: int = 0, bloco: int = 1) -> int:
    """
    Recursivo puro (top-down). Use só para estoques muito pequenos.
    - estoques: lista de quantidades (valores inteiros)
    - bloco: discretização (1 = unidade)
    Retorna desperdício mínimo (na escala NORMALIZADA).
    """
    # normaliza e trabalha com cópia curta
    norm = list(_normalizar_estoques(estoques, bloco))

    def _rec(idx: int, estado: Tuple[int, ...]) -> int:
        if idx == len(norm):
            return 0
        melhor = float('inf')
        estoque_atual = estado[idx]
        # testar consumo de 0 até estoque_atual
        for c in range(0, estoque_atual + 1):
            # desperdicio do dia = (estoque - consumo)
            desperdicio_dia = (estoque_atual - c)
            # cria novo estado temporário
            novo_estado = list(estado)
            novo_estado[idx] = estoque_atual - c
            # para os próximos dias só usamos as mesmas coords (modelo simplificado por item por dia)
            # chamamos rec para o próximo índice (cada índice representa um "item/dia" discretizado)
            valor = desperdicio_dia + _rec(idx + 1, tuple(novo_estado))
            if valor < melhor:
                melhor = valor
        return melhor

    return _rec(0, tuple(norm))

# ---------------------------
# 2) Memoizada (top-down com cache)
# ---------------------------
def consumo_otimo_memo(estoques: List[int], bloco: int = 1) -> int:
    norm = _normalizar_estoques(estoques, bloco)
    n = len(norm)

    @lru_cache(maxsize=None)
    def dp(idx: int, estado: Tuple[int, ...]) -> int:
        if idx == n:
            return 0
        melhor = float('inf')
        estoque_atual = estado[idx]
        for c in range(0, estoque_atual + 1):
            desperdicio = (estoque_atual - c)
            novo_estado = list(estado)
            novo_estado[idx] = estoque_atual - c
            valor = desperdicio + dp(idx + 1, tuple(novo_estado))
            if valor < melhor:
                melhor = valor
        return melhor

    return dp(0, tuple(norm))

# ---------------------------
# 3) Iterativa (bottom-up) - eficiente se usando normalização pequena
# ---------------------------
def consumo_otimo_iterativo(estoques: List[int], bloco: int = 1) -> int:
    norm = list(_normalizar_estoques(estoques, bloco))
    n = len(norm)
    # dp[i] = desperdício mínimo considerando índices i..n-1
    dp = [0] * (n + 1)  # dp[n] = 0

    # percorre de trás pra frente
    for i in range(n - 1, -1, -1):
        melhor = float('inf')
        estoque_atual = norm[i]
        for c in range(0, estoque_atual + 1):
            desperdicio = (estoque_atual - c) + dp[i + 1]
            if desperdicio < melhor:
                melhor = desperdicio
        dp[i] = melhor

    return dp[0]
