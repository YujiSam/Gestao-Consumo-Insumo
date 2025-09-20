# 📋 Relatório Técnico - Sistema de Gestão de Consumo de Insumos
# 🏥 Contexto do Problema

O desafio envolve a baixa visibilidade no apontamento de consumo em unidades de diagnóstico, onde o registro do uso de materiais como reagentes e equipamentos descartáveis não é feito com precisão, resultando em discrepâncias de estoque, falta de materiais essenciais e aumento de custos.
# 🎯 Solução Implementada

Sistema completo de gestão de consumo que utiliza estruturas de dados clássicas e algoritmos eficientes para fornecer visibilidade total do consumo de insumos médicos.
# 🏗️ Estruturas de Dados e Algoritmos Implementados
## 📊 Fila (Queue) - Ordem Cronológica

Implementação: FilaConsumo em structures/fila_consumo.py
Uso no contexto: Registra o consumo diário em ordem cronológica (FIFO - First In, First Out). Cada novo registro é adicionado ao final da fila, garantindo que a ordem temporal seja preservada para auditoria e análise histórica.

Aplicação prática: Monitoramento do fluxo de consumo ao longo do tempo, processamento de registros na sequência correta e manutenção de histórico sequencial.
## 📚 Pilha (Stack) - Ordem Inversa

Implementação: PilhaConsulta em structures/pilha_consulta.py
Uso no contexto: Permite consultar os últimos consumos primeiro (LIFO - Last In, First Out). Ideal para verificação rápida dos registros mais recentes e identificação de padrões de consumo recentes.

Aplicação prática: Acesso rápido aos consumos recentes, facilitação da correção de registros errôneos e análise de tendências recentes.
## 🔍 Busca Sequencial

Implementação: busca_sequencial() em algorithms/busca.py
Uso no contexto: Percorre todos os registros para encontrar todos os consumos de um insumo específico. Funciona em listas não ordenadas e garante que todos os registros relevantes sejam encontrados.

Aplicação prática: Consultas pontuais por insumo específico, relatórios de consumo por produto e análise de uso individual de insumos.
## ⚡ Busca Binária

Implementação: busca_binaria_por_data() em algorithms/busca.py
Uso no contexto: Encontra registros por data específica de forma extremamente eficiente. Requer dados ordenados e oferece performance O(log n).

Aplicação prática: Consultas rápidas por período específico, relatórios diários e análise temporal eficiente.
## 🔄 Merge Sort

Implementação: merge_sort_por_quantidade() em algorithms/ordenacao.py
Uso no contexto: Ordena registros por quantidade consumida usando algoritmo estável e eficiente com complexidade O(n log n).

Aplicação prática: Identificação de insumos com maior/menor consumo, análise de padrões de uso e otimização de estoque.
## 🚀 Quick Sort

Implementação: quick_sort_por_validade() em algorithms/ordenacao.py
Uso no contexto: Ordena registros por validade do insumo usando algoritmo eficiente com excelente performance na prática.

Aplicação prática: Gestão de validade de insumos, prevenção de perdas por vencimento e priorização de uso.
# 📈 Sistema de Visualização
## 🎨 Visualizador de Dados

Implementação: VisualizadorDados em visualization/visualizador_dados.py
Funcionalidades:

    Gráfico de consumo diário com barras interativas

    Top insumos mais consumidos com cores gradientes

    Distribuição de custos por tipo (gráfico de pizza)

    Alertas visuais de estoque baixo com código de cores

    Gráfico de validades próximas com contagem regressiva

Benefícios: Transforma dados brutos em insights visuais imediatamente compreensíveis, facilitando a tomada de decisão.

# 🚀 Funcionalidades Principais
## ✅ Gestão Completa de Estoque

    Controle de insumos com validade e custos

    Registro preciso de consumo diário

    Atualização automática de estoque

## ✅ Análise e Relatórios

    Estatísticas de consumo e custos

    Identificação de padrões de uso

    Alertas de estoque baixo e validade próxima

## ✅ Visualização Intuitiva

    Dashboard com gráficos interativos

    Relatórios formatados profissionalmente

    Código de cores para situações críticas

# 🛠️ Tecnologias Utilizadas

    Python 3.8+

    Pandas para manipulação de dados

    Matplotlib para visualização gráfica

    Tabulate para relatórios formatados

    Pytest para testes automatizados

# 🎯 Resultados Esperados

    🎯 100% de visibilidade do consumo diário

    📉 30% de redução em discrepâncias de estoque

    💰 25% de economia com compras otimizadas

    ⏰ 40% menos tempo com processos manuais

    ⚠️ Alertas proativos para validade e reposição

# 📝 Como Executar

## Instalar dependências
pip install -r requirements.txt

## Executar sistema principal
python main.py

## Executar testes
python -m pytest tests/
