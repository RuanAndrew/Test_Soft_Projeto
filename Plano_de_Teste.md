# 📝 Plano de Testes (IEEE 829)

## 1. Identificador do Plano de Teste

| Identificador | PT-ECOMM-GAMES-V1.0 |
|---------------|---------------------|
| Sistema       | E-commerce de Jogos Digitais |
| Versão Documento | 1.0 |
| Data da Versão | 2025-11-12 |

---

## 2. Introdução
Este documento descreve o plano para a condução do ciclo de testes do sistema E-commerce de Jogos Digitais. O objetivo principal é validar a qualidade do sistema, assegurando que os requisitos de negócio e funcionalidades essenciais sejam atendidos.

**Objetivos Específicos do Teste:**
- Garantir o correto gerenciamento do catálogo de jogos, incluindo busca e visualização.
- Assegurar a funcionalidade e segurança do processamento de cadastro e autenticação de usuários.
- Verificar o fluxo completo de compra, desde a adição de itens ao carrinho até a finalização do pedido.
- Validar o controle da biblioteca de jogos do usuário, incluindo a aquisição e o acesso aos títulos comprados.

---

## 3. Itens de Teste
O teste será concentrado nas seguintes funcionalidades (módulos em escopo):

| Módulo                  | Funcionalidades em Teste |
|-------------------------|-------------------------|
| Gerenciamento de Usuário| Criação, exclusão e atualização de conta; Login e Logout; Validação de dados de entrada (e-mail duplicado, senha fraca). |
| Catálogo                | Busca de jogos; Visualização de detalhes do jogo; Filtragem de resultados. |
| Carrinho                | Adição e remoção de itens ao carrinho; Cálculo de subtotal; Finalização da compra. |
| Biblioteca do Usuário   | Visualização da biblioteca de jogos adquiridos; Verificação de que apenas jogos comprados aparecem; Simulação de "download" (verificação de permissão). |

---

## 4. Itens Não-Testados
Os seguintes módulos e funcionalidades estão fora do escopo deste ciclo de testes:
- Módulos dos Parceiros (ex: painel de upload de jogos pelo desenvolvedor ou publisher).
- Integração com APIs de pagamento (a ser validada em um ciclo de testes dedicado ou por terceiros).

---

## 5. Estratégia de Abordagem
A estratégia combina testes automatizados e manuais em vários níveis, priorizando a estabilidade do fluxo de compra e autenticação.

**Níveis de Teste:**
- Teste Unitário: Focado em validar a lógica de negócio de classes e funções individuais.
- Teste de Integração: Validará a interação entre os módulos (ex: "Carrinho" e "Usuário").
- Teste de Sistema (E2E): Testará os fluxos de ponta-a-ponta, simulando o uso real (caixa-preta).

**Tipos de Teste:**
- Teste de Funcionalidade (Caixa-Preta: Usando Partição de Equivalência e Valor Limite)
- Teste de Segurança (Básico): Assegurar que os dados e o sistema não sejam acessados indevidamente.
- Teste de Regressão: Garantir que correções não introduziram novos problemas.
- Teste de Desempenho (Básico): Verificar o tempo de resposta e processamento.

---

## 6. Critérios de Aprovação/Reprovação de Itens
Um item de teste (funcionalidade) será considerado aprovado se:
- O resultado da execução do caso de teste corresponder ao resultado esperado (100% Pass).
- Não houver bugs de severidade Crítica ou Alta abertos associados à funcionalidade.

---

## 7. Critérios de Suspensão e Retomada de Teste
**Critérios de Suspensão:**
A execução do Teste de Sistema será suspensa se forem identificados 3 ou mais defeitos de severidade Crítica ou Alta no módulo principal (Fluxo de Compra ou Login/Cadastro).

**Critérios de Retomada:**
Os testes só serão retomados após a equipe de desenvolvimento corrigir os defeitos de bloqueio e uma nova build estável for disponibilizada e validada pelo time de testes (teste de Sanidade/Smoke Test).

---

## 8. Entregáveis do Teste
Os seguintes artefatos serão gerados e entregues ao final do ciclo de testes:
- Plano de Testes (TP) Aprovado.
- Casos de Teste (TCS) Documentados.
- Scripts de Testes Automatizados (Pytest).
- Matriz de Defeitos (Gerenciada no Trello).
- Relatório Final de Testes (TSR).

---

## 9. Tarefas de Teste
- Planejamento e Revisão do TP.
- Criação, Revisão e Mapeamento dos Casos de Teste (incluindo técnicas de AVL/PE).
- Configuração do Ambiente de Teste.
- Desenvolvimento dos Scripts de Teste Automatizado.
- Execução dos Testes Manuais (Sistema/E2E).
- Registro, Acompanhamento e Re-teste de Defeitos (Matriz de Defeitos).
- Medição de Cobertura de Código (Pytest-Cov).
- Geração e Aprovação do Relatório Final.

---

## 10. Requisitos de Ambiente
- **Hardware:** Servidor de Testes dedicado, Estações de trabalho dos testers.
- **Software Base:** Python, Ambiente Virtual Python.
- **Ferramentas:** Pytest, Pytest-Cov, Trello, Git.
- **Configuração:** O ambiente deve ser configurado para espelhar as configurações da Produção.

---

## 11. Responsabilidades
| Papel                  | Responsabilidade Principal |
|------------------------|---------------------------|
| Gerente de Projetos    | Aprovação de documentos e Decisões de Go/No-Go. |
| Analista de Qualidade (QA) | Criação/Execução de Casos de Teste, Automação, Registro de Defeitos e Relatórios. |
| Desenvolvedores        | Correção de Defeitos e Entrega de Builds Estáveis. |

---

## 12. Pessoal e Treinamento
- **Pessoal:** 1 Analista de Qualidade Sênior (Liderança/Automação), 1 Analista de Qualidade Júnior (Execução Manual).
- **Treinamento:** O Analista Júnior requer treinamento nas ferramentas de automação (Pytest) e nas regras de negócio da plataforma.

---

## 13. Cronograma
O ciclo de testes se alinha com o cronograma geral do projeto. Marcos principais:
- Aprovação do Plano de Testes.
- Conclusão da Automação da Suíte de Regressão.
- Início da Execução do Teste de Sistema.
- Fim do Ciclo de Correção e Re-teste.
- Entrega do Relatório Final (**18/12/2025**).

---

## 14. Estimativas de Teste
A estimativa de esforço (em horas) será determinada pela técnica de Wideband Delphi, baseada na complexidade de cada módulo. As estimativas de cobertura de código são de no mínimo **80%** (Critério de Saída).

---

## 15. Riscos e Contingências
| ID      | Risco                                                        | Mitigação / Contingência |
|---------|--------------------------------------------------------------|-------------------------|
| Risco 1 | Definição de escopo muito grande ou em constante mudança.    | Foco estrito nos módulos definidos. Novas ideias documentadas como "Backlog Futuro" no Trello. |
| Risco 2 | Falha Crítica no Ambiente de Testes.                         | Ter um snapshot ou backup do ambiente pronto. Definir um tempo máximo de inatividade de 4 horas para restauração. |
| Risco 3 | Dependência excessiva da Automação.                          | Manter uma documentação robusta dos Casos de Teste manuais e garantir a execução manual dos fluxos de maior risco (Caixa-Preta). |

---

## 16. Aprovações
| Nome   | Título                       | Assinatura | Data         |
|--------|------------------------------|------------|--------------|
| [Ruan] | Gerente de Projetos          |            |              |
| [Vanessa] | Analista de Qualidade Sênior |            |              |
