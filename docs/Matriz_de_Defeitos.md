# 📋 Matriz de Defeitos

| ID   | Data       | Módulo      | Descrição do Defeito                            | Passos para Reproduzir | Severidade | Prioridade | Status      | Responsável | Observações |
|------|------------|-------------|------------------------------------------------|-----------------------|------------|------------|-------------|-------------|-------------|
| BUG-1| 2025-12-17 | Biblioteca  | Mensagem de erro com aspas divergentes         | Executar TC-LIB-003   | Baixa      | Baixa      | Corrigido   | Dev Team       | Removidas aspas da mensagem |
|BUG-002|2025-12-17|Carrinho|Violação da RN1: Sistema permite adicionar ao carrinho um jogo que o usuário já possui.|1. Logar com usuário que já tem "The Witcher 3".<br> 2. Ir ao catálogo.<br> 3. Clicar em "Adicionar ao Carrinho".|Alta|Alta|Aberto|Dev Team|
|BUG-003|2025-12-17|Catálogo (Repo)|Busca Case-Sensitive: A busca falha se o usuário não digitar as letras maiúsculas/minúsculas exatamente iguais ao título.|1. Acessar o catálogo.<br> 2. Pesquisar por "witcher" (tudo minúsculo).<br> 3. Verificar que retorna 0 jogos (esperado: The Witcher 3).|Média|Média|Aberto|Dev Team|
|BUG-004|2025-12-17|Catálogo (Service)|Exibição de Jogos Inativos: O Service não esta filtrando os jogos que estão inativos.|1. Ter um jogo com status "inativo".<br> 2. Buscar jogos no catálogo.<br> 3. O Serviço exibe o jogo inativo para o cliente.|Média|Alta|Aberto|Dev Team

**Legenda de Status:** Aberto, Em correção, Corrigido, Re-testar, Fechado

**Resumo de Defeitos:**
- Total de Defeitos Encontrados: **4**
- Defeitos Críticos: **0**
- Defeitos Altos: **2** (BUG-002, BUG-004)
- Defeitos Médios: **2** (BUG-003, BUG-004)
- Defeitos Baixos: **1** (BUG-1)
- Defeitos em Aberto: **3** (BUG-002, BUG-003, BUG-004)
- Defeitos Corrigidos: **1** (BUG-1)
- Taxa de Resolução: **25%** (1/4 corrigido)

