# Plano de Testes

Sistema: E-commerce de Jogos Digitais

## Objetivos do Plano

O objetivo deste plano é validar a qualidade do sistema de E-commerce de Jogos Digitais, assegurando que os principais requisitos de negócio sejam atendidos. Os objetivos específicos incluem:

- Garantir o correto gerenciamento do catálogo de jogos, incluindo busca e visualização.

- Assegurar a funcionalidade e segurança do processamento de cadastro e autenticação de usuários.

- Verificar o fluxo completo de compra, desde a adição de itens ao carrinho até a finalização do pedido.

- Validar o controle da biblioteca de jogos do usuário, incluindo a aquisição e o acesso aos títulos comprados.

## Escopo do Teste

### Módulos em Escopo

O escopo deste plano de testes focara nos seguintes módulos do sistema:

- Gerenciamento de Usuário

- Catálogo

- Carrinho

- Biblioteca do Usuário

### Módulos Fora de Escopo

Os seguintes itens não serão testados neste ciclo, para mitigar o risco 1 (escopo muito grande ou em constante mudança):

- Módulos dos Parceiros (ex: painel de upload de jogos pelo desenvolvedor ou publisher).

- Integração com APIS de pagamento.

## Itens de Teste

O esforço de teste será concentrado nas seguintes funcionalidades:

### Módulo de Usuário:

- Criação, exclusão e atualização de conta.

- Login e Logout.

- Validação de dados de entrada (ex: e-mail duplicado, senha fraca).

### Módulo de Catálogo:

- Busca de jogos.

- Visualização de detalhes do jogo.

- Filtragem de resultados.

### Módulo de Carrinho:

- Adição e remoção de itens ao carrinho.

- Cálculo de subtotal.

- Finalização da compra.

### Módulo de Biblioteca:

- Visualização da biblioteca de jogos adquiridos.

- Verificação de que apenas jogos comprados aparecem na biblioteca.

- Simulação de "download" de jogo (verificação de permissão).

## Níveis e Tipos de Teste

### Níveis de Teste

- Teste Unitário: Focado em validar a lógica de negócio de classes e funções individuais.

- Teste de Integração: Validará a interação entre os módulos (ex: "Carrinho" e "Usuário" para verificar autenticação; "Carrinho" e "Biblioteca" após a compra).

- Teste de Sistema: Testará os fluxos de ponta-a-ponta (end-to-end) nos "Itens de Teste" definidos, simulando o uso real do sistema (caixa-preta).

### Tipos de Teste

- Teste de funcionalidade: Validar se as funcionalidades se comportam conforme a especificação.

- Teste de segurança: Assegurar que os dados e o sistema não sejam acessados indevidamente.

- Teste de Regressão: Garantir que novas implementações ou correções de defeitos não introduziram novos problemas em funcionalidades existentes.

- Teste de desempenho: Verificar o tempo de resposta e processamento.

## Critérios de Entrada e Saída

### Critérios de Entrada

O ciclo de Teste de Sistema só poderá iniciar quando os seguintes critérios forem atendidos:

- Documentação Aprovada: Os requisitos funcionais e o Plano de Testes estão revisados e aprovados.

- Ambiente Configurado: O ambiente de desenvolvimento, incluindo o repositório Git, ambiente virtual Python e as ferramentas (pytest, pytest-cov), está configurado e funcional.

- Funcionalidades Mínimas: As funcionalidades mínimas viáveis para os módulos de Usuário, Catálogo, Carrinho e Biblioteca estão definidas para este ciclo de teste.

### Critérios de Saída

O ciclo de testes será considerado concluído quando os seguintes critérios forem atingidos:

- Todos os casos de teste de sistema planejados foram executados.

- Todos as funcionalidades cobertas por pelo menos um caso de teste.

- Meta de cobertura de código de 80% atingida pelo pytest-cov.

- Não há bugs de severidade Crítica ou Alta em aberto.

- Todos os bugs registrados no Trello possuem um status final (ex: Corrigido, Validado, Adiado).

- A suíte de Testes de Regressão automatizada está executando com 100% de aprovação (Green).

- Todos os artefatos de entrega (Plano, Casos de Teste, Matriz de Defeitos, Scripts pytest e Relatório Final) estão completos e revisados.

## Ferramentas

- Python: Linguagem base para o desenvolvimento e testes.

- Pytest: Framework principal para automação de testes unitários e de integração (TDD).

- Pytest-Cov: Ferramenta para medição da cobertura de código (Code Coverage).

- Trello: Ferramenta para gerenciamento de projeto (Scrum), incluindo a Matriz de Defeitos.

- Git: Sistema de controle de versão para o código-fonte e scripts de teste.

## Riscos

- Risco 1: Definição de escopo muito grande ou em constante mudança.

    - Mitigação: Foco estrito nos módulos definidos na Seção 2. Novas ideias ou funcionalidades serão documentadas no Trello como "Backlog Futuro" e não farão parte deste ciclo.
