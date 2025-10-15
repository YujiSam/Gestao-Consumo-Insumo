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

## 🧠 Programação Dinâmica (Otimização do Consumo de Insumos)

Implementação: calcular_consumo_otimo() em system/sistema_consumo.py
Uso no contexto: Modela o problema de consumo e reposição de insumos ao longo do tempo como uma decisão sequencial, aplicando Programação Dinâmica para encontrar o plano de uso que minimiza desperdícios e evita faltas de estoque.

## Formulação do Problema

Estado: quantidade atual de insumo em estoque em determinado dia

Decisão: quanto consumir e/ou repor naquele dia

Função de Transição: atualiza o estoque considerando consumo, validade e chegada de novas unidades

Função Objetivo: minimizar o desperdício total de insumos e o custo de reposição ao longo do período analisado

## ⚙️ Versões Desenvolvidas

Para garantir desempenho e consistência, foram criadas três versões do algoritmo de Programação Dinâmica:

## 🌀 Versão Recursiva
Implementa a definição matemática diretamente, ideal para entendimento conceitual da decomposição em subproblemas.

## 🧩 Versão com Memorização (Top-Down)
Armazena os resultados de subproblemas já resolvidos, evitando recomputações e melhorando a eficiência sem alterar a lógica.

## ⬇️ Versão Iterativa (Bottom-Up)
Constrói a solução de forma progressiva a partir dos menores subproblemas, oferecendo o melhor desempenho em cenários reais.

## ✅ Todas as versões retornam o mesmo resultado final, comprovando a consistência da modelagem matemática.

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

# 🖊️Autores:

Gustavo Yuji Osugi - RM 555034

Otavio Santos de Lima Ferrão - RM 556452

Renan Simões Gonçalves - RM 555584

Victor Hugo de Paula - RM 554787

Vitor Rivas Cardoso - RM 556404
