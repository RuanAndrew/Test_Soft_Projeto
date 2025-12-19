# Relatório Final de Testes - E-commerce de Jogos Digitais

**Data da Entrega:** 18 de dezembro de 2025  
**Projeto:** Teste de Software - Sistema E-commerce de Jogos Digitais  
**Versão:** 1.1

---

## 1. Descrição do Sistema Testado

### 1.1 Resumo Técnico

O presente relatório documenta o processo de validação da qualidade do sistema de E-commerce de Jogos Digitais, detalhando as estratégias de teste, execução e análise de defeitos.

O sistema testado implementa uma arquitetura em camadas seguindo o padrão MVC (Model-View-Controller), desenvolvido em Python 3.14 com o framework de testes pytest 9.0.1. A arquitetura é composta por:

**Camada de Modelos (Models):**
- `Usuario.py`: Entidade de usuário com atributos id, nome, email e senha
- `Jogo.py`: Entidade de jogo com atributos id, título, preço, status e descrição
- `Catalogo.py`: Coleção de jogos disponíveis no sistema
- `Biblioteca.py`: Biblioteca pessoal do usuário com gerenciamento de jogos comprados

**Camada de Serviços (Services):**
- `CadastroService.py`: Gestão de contas de usuário e autenticação
- `CatalogoService.py`: Busca e filtragem de jogos no catálogo
- `CarrinhoService.py`: Gerenciamento do carrinho de compras
- `BibliotecaService.py`: Acesso e controle da biblioteca pessoal do usuário

**Camada de Persistência:**
- `RepositorioMemoria.py`: Implementação de repositório em memória para isolamento dos testes, contendo usuários pré-carregados, catálogo com 10 jogos e bibliotecas de compras

### 1.2 Escopo dos Testes

O foco da campanha de testes concentrou-se na validação do backend e da lógica de negócios do sistema. A utilização de persistência em memória (`RepositorioMemoria.py`) permitiu o isolamento completo dos testes, eliminando dependências externas e garantindo reprodutibilidade dos resultados.

As funcionalidades críticas validadas incluem:
- **Cadastro de Usuário (USR):** Criação de conta, autenticação, alteração de senha e atualização de perfil
- **Catálogo (CAT):** Busca de jogos por termo e filtragem por status
- **Carrinho (CAR):** Adição e remoção de itens, cálculo de totais
- **Biblioteca (LIB):** Visualização de jogos comprados, instalação e desinstalação

---

## 2. Metodologia e Estratégia de Teste

### 2.1 Aplicação do TDD (Test-Driven Development)

A estratégia de validação adotou a metodologia TDD (Test-Driven Development). O ciclo de desenvolvimento seguiu o padrão Red-Green-Refactor:

1. **Red (Vermelho):** Testes foram escritos antes da implementação, baseados nos requisitos documentados nos casos de uso (UC01, UC02, UC03) e casos de teste. Estes testes inicialmente falhavam por ausência de implementação.

2. **Green (Verde):** Implementação mínima do código foi desenvolvida para fazer os testes passarem, garantindo que as regras de negócio fossem atendidas desde a concepção.

3. **Refactor (Refatoração):** Após a aprovação dos testes, o código foi refatorado mantendo a funcionalidade e melhorando a qualidade.

**Exemplo prático de aplicação do TDD:**

Os testes unitários em `tests/unidade/test_modelo_jogo.py` foram criados antes da implementação final da classe `Jogo.py`. Estes testes validaram regras de negócio como:
- Preço não pode ser negativo (teste de valor limite mínimo)
- Comparação de jogos baseada em ID (teste de igualdade)
- Validação de status válidos (teste de valores permitidos)

A implementação da classe `Jogo.py` foi então desenvolvida para atender a estes testes, garantindo que as regras de negócio estivessem corretas desde o início.

### 2.2 Técnicas de Especificação Utilizadas

#### 2.2.1 Partição de Equivalência (PE)

A técnica de Partição de Equivalência foi aplicada para identificar classes válidas e inválidas de entrada, reduzindo o número de casos de teste necessários.

**Aplicação no Catálogo:**
- **Classe válida:** Busca com termo existente no catálogo (TC-CAT-001)
- **Classe inválida:** Busca com termo inexistente (TC-CAT-002)

Implementado em `tests/integracao/test_catalogo_integracao.py` através do método `test_busca_real_encontrada` e `test_busca_real_nenhum_resultado`.

**Aplicação no Carrinho:**
- **Classe válida:** Adição de jogo disponível e não possuído pelo usuário
- **Classe inválida:** Tentativa de adicionar jogo já comprado (violação de RN1)

#### 2.2.2 Análise de Valor Limite (AVL)

A Análise de Valor Limite foi utilizada para testar comportamentos em situações de borda.

**Aplicação no Carrinho:**
- **Limite inferior:** Carrinho vazio (0 itens) - `test_carrinho_vazio_inicialmente` em `tests/integracao/test_carrinho_integracao.py`
- **Limite superior:** Múltiplos itens no carrinho - `test_adicionar_multiplos_jogos_ao_carrinho`
- **Valor mínimo de preço:** Jogos gratuitos (R$ 0,00) - `test_calculo_total_apenas_jogos_gratuitos`
- **Valor máximo de preço:** Jogos premium (R$ 9999,99) - `test_preco_limite_maximo` em `tests/unidade/test_modelo_jogo.py`

#### 2.2.3 Tabela de Decisão

A Tabela de Decisão foi aplicada para validar a funcionalidade de adição ao carrinho considerando múltiplas condições simultâneas (TC-CAR-006), documentada em `docs/Casos_de_Teste.md`. As condições avaliadas incluíram:
- C1: Jogo está ativo no catálogo?
- C2: Usuário já possui o jogo?
- C3: Jogo já está no carrinho?
- C4: Usuário está autenticado?

#### 2.2.4 Transição de Estados

A técnica de Transição de Estados foi utilizada para validar o ciclo completo de vida do jogo no sistema:
- Estado inicial: Jogo não comprado
- Transição: Compra realizada
- Estado final: Jogo disponível na biblioteca com status "COMPRADO"
- Transição adicional: Download/Instalação
- Estado final: Jogo com status "INSTALADO"

Implementado em `tests/sistema/test_e2e_jornada_comprador.py` através do teste end-to-end que valida o fluxo completo do usuário.

### 2.3 Níveis de Teste

#### 2.3.1 Testes Unitários (Caixa Branca)

Os testes unitários focaram na validação de métodos e funções individuais, com conhecimento da implementação interna. Foram executados 44 testes unitários distribuídos em:
- `tests/unidade/test_modelo_jogo.py`: 13 testes validando a classe Jogo
- `tests/unidade/test_modelo_biblioteca.py`: 17 testes validando a classe Biblioteca
- `tests/unidade/test_carrinho.py`: 3 testes validando o CarrinhoService isolado
- `tests/unidade/test_catalogo.py`: 2 testes validando o CatalogoService isolado
- `tests/unidade/test_cadastrar_usuario.py`: 5 testes validando o CadastroService isolado
- `tests/unidade/test_biblioteca.py`: 4 testes validando o BibliotecaService isolado

Estes testes utilizaram mocks para isolar dependências e validar lógica interna, precondições e pós-condições.

#### 2.3.2 Testes de Integração (Caixa Preta)

Os testes de integração validaram o comportamento do sistema através da interação entre componentes, sem conhecimento detalhado da implementação interna. Foram executados 15 testes de integração em:
- `tests/integracao/test_carrinho_integracao.py`: 7 testes validando integração Carrinho + Modelos
- `tests/integracao/test_catalogo_integracao.py`: 3 testes validando integração CatalogoService + RepositorioMemoria
- `tests/integracao/test_cadastro_integracao.py`: 2 testes validando integração CadastroService + RepositorioMemoria
- `tests/integracao/test_integracao_biblioteca.py`: 3 testes validando integração Biblioteca + Usuário + Repositório

Estes testes utilizaram o `RepositorioMemoria` com dados pré-carregados para validar a persistência e recuperação de dados.

#### 2.3.3 Testes de Sistema (End-to-End)

Os testes de sistema simularam a jornada completa do usuário, validando fluxos críticos de ponta-a-ponta. Foi executado 1 teste E2E em `tests/sistema/test_e2e_jornada_comprador.py`, cobrindo o cenário: Registro → Login → Busca → Carrinho → Compra → Biblioteca → Download.

---

## 3. Cobertura e Execução dos Testes

### 3.1 Volume de Testes

Foram documentados 19 casos de teste no documento `docs/Casos_de_Teste.md`, superando o mínimo de 6 casos exigido. Estes casos de teste cobrem os módulos:
- Catálogo (TC-CAT-001 a TC-CAT-003): 3 casos
- Carrinho (TC-CAR-001 a TC-CAR-006): 6 casos
- Biblioteca (TC-LIB-001 a TC-LIB-004): 4 casos
- Conta de Usuário (TC-USR-001 a TC-USR-005): 5 casos
- Sistema End-to-End (TC-SYS-001): 1 caso

Embora todos os cenários manuais tenham sido cobertos, a suíte automatizada foi expandida para 60 testes (44 unitários, 15 de integração, 1 E2E) para garantir maior robustez e prevenção de regressão. Esta expansão ocorreu porque:

1. **Múltiplos cenários por caso de teste:** Um caso de teste manual pode gerar múltiplos scripts automatizados para validar diferentes aspectos. Por exemplo, TC-CAR-003 (Cálculo de Total) gerou tanto testes unitários quanto de integração.

2. **Validação de bordas:** Testes adicionais foram criados para validar valores limite e casos extremos não explicitamente documentados nos casos de teste manuais.

3. **Isolamento de componentes:** Testes unitários foram criados para validar componentes isoladamente, enquanto testes de integração validam a interação entre componentes.

Portanto, não existe uma relação 1:1 entre casos de teste documentados e scripts automatizados, sendo esta expansão uma prática recomendada para garantir cobertura abrangente.

### 3.2 Métricas de Cobertura

A cobertura de código foi medida utilizando pytest-cov 7.0.0, fornecendo evidência técnica da qualidade do código através de análise estática (Caixa Branca).

| Módulo | Statements | Missing | Cobertura |
|--------|------------|---------|-----------|
| `Biblioteca.py` | 33 | 0 | 100% |
| `Jogo.py` | 13 | 0 | 100% |
| `CarrinhoService.py` | 11 | 0 | 100% |
| `CatalogoService.py` | 12 | 0 | 100% |
| `BibliotecaService.py` | 16 | 1 | 94% |
| `CadastroService.py` | 18 | 1 | 94% |
| `Catalogo.py` | 7 | 1 | 86% |
| **TOTAL** | **110** | **3** | **97%** |

A cobertura de 97% indica que 97% das linhas de código foram executadas durante os testes, com apenas 3 linhas não cobertas distribuídas em três módulos. As linhas não cobertas correspondem a caminhos de código alternativos ou tratamento de erros não exercitados nos testes atuais.

### 3.3 Execução dos Testes

A execução da suíte completa de testes resultou em:

```
============================= test session starts ==============================
Platform: Linux 5.15.0, Python 3.12.1, pytest-9.0.1

Collecting... 60 items

SUMMARY:
✅ 57 PASSED                                                          [95%]
❌ 3 FAILED                                                           [5%]
⏭️  0 SKIPPED                                                           [0%]

Tempo Total: 0.22 segundos
```

**Distribuição de Resultados:**
- Testes Unitários: 44 testes, 44 aprovados (100%)
- Testes de Integração: 15 testes, 12 aprovados (80%), 3 reprovados (20%)
- Testes E2E: 1 teste, 1 aprovado (100%)

**Testes Reprovados:**
1. `test_carrinho_integracao.py::TestCarrinhoIntegracao::test_adicionar_jogo_ja_comprado` - Relacionado a BUG-002
2. `test_catalogo_integracao.py::TestCatalogoIntegracao::test_busca_real_encontrada` - Relacionado a BUG-003
3. `test_catalogo_integracao.py::TestCatalogoIntegracao::test_listar_todos_exibe_somente_ativos` - Relacionado a BUG-004

---

## 4. Evidências e Análise dos Resultados

### 4.1 Evidências de Execução

#### 4.1.1 Log de Cobertura

```bash
$ pytest tests/ -v --cov=src --cov-report=term-missing

================================ tests coverage ================================
_______________ coverage: platform linux, python 3.12.1-final-0 ________________

Name                                Stmts   Miss  Cover   Missing
-----------------------------------------------------------------
src/models/Biblioteca.py               33      0   100%
src/models/Catalogo.py                 7      1    86%   9
src/models/Jogo.py                     13      0   100%
src/services/BibliotecaService.py      16      1    94%   31
src/services/CadastroService.py        18      1    94%   36
src/services/CarrinhoService.py        11      0   100%
src/services/CatalogoService.py        12      0   100%
-----------------------------------------------------------------
TOTAL                                 110      3    97%
============================== 57 passed, 3 failed in 0.22s ==============================
```

#### 4.1.2 Testes Críticos Aprovados

**TC-CAR-003: Cálculo de Total**
```python
# tests/integracao/test_carrinho_integracao.py::test_calculo_total_dois_jogos
carrinho.adicionar_jogo(jogo1)  # Call of Duty: R$ 349,90
carrinho.adicionar_jogo(jogo2)  # Hollow Knight: R$ 46,99
assert carrinho.calcular_total() == pytest.approx(396.89, 0.01)
# Resultado: PASS
```

**TC-LIB-003: Acesso Restrito**
```python
# Validação de mensagem para jogo não adquirido
mensagem_esperada = "Parece que este jogo ainda não é seu! Adquira Street Fighter na loja."
# Resultado: PASS - Mensagem correta
```

**TC-USR-001: Criação de Conta**
```python
# tests/integracao/test_cadastro_integracao.py
result = cadastro_service.criar_conta(usuario)
assert result["sucesso"] == True
assert result["mensagem"] == "Conta criada com sucesso!"
# Resultado: PASS
```

### 4.2 Análise de Defeitos

A análise dos resultados revelou que os testes automatizados cumpriram seu objetivo ao identificar 3 defeitos críticos que violam regras de negócio do sistema. O fato dos testes terem falhado é um sucesso da metodologia de teste, pois impediu que código defeituoso fosse considerado "pronto" para produção.

#### 4.2.1 BUG-002: Violação de Regra de Negócio (Carrinho)

**Descrição:** O sistema permitiu adicionar ao carrinho um jogo que o usuário já possui na biblioteca, violando a Regra de Negócio RN1 (Verificação de Posse Única).

**Análise Técnica:**
- **Localização:** `tests/integracao/test_carrinho_integracao.py::test_adicionar_jogo_ja_comprado`
- **Causa Raiz:** O `CarrinhoService` não realiza validação prévia consultando a biblioteca do usuário antes de adicionar o jogo ao carrinho.
- **Impacto:** Permite que usuários tentem comprar jogos já adquiridos, gerando confusão e possível tentativa de compra duplicada.
- **Severidade:** Alta - Violação direta de requisito de negócio documentado
- **Prioridade:** Alta - Bloqueia funcionalidade crítica do sistema

**Evidência do Teste:**
```python
# Teste esperava que o carrinho permanecesse vazio após tentativa de adicionar jogo já comprado
carrinho.adicionar_jogo(jogo_ja_tem)  # jogo_ja_tem = The Witcher 3 (já na biblioteca)
assert len(carrinho.listar_jogos()) == 0  # FALHOU: carrinho contém 1 item
```

#### 4.2.2 BUG-003: Falha de Filtragem (Catálogo - Busca Case-Sensitive)

**Descrição:** A busca no catálogo é case-sensitive, causando falsos negativos quando o usuário digita o termo de busca com capitalização diferente do título armazenado.

**Análise Técnica:**
- **Localização:** `tests/integracao/test_catalogo_integracao.py::test_busca_real_encontrada`
- **Causa Raiz:** O método de busca em `CatalogoService` ou `RepositorioMemoria` realiza comparação exata de strings sem normalização de case (lowercase/uppercase).
- **Impacto:** Usuários não encontram jogos mesmo digitando o nome correto, degradando a experiência do usuário e reduzindo a usabilidade do sistema.
- **Severidade:** Média - Funcionalidade parcialmente operacional
- **Prioridade:** Média - Impacta usabilidade mas não bloqueia funcionalidade

**Evidência do Teste:**
```python
# Busca por "witcher" (minúsculo) deveria encontrar "The Witcher 3"
resultado = integ_catalogo_service.buscar_jogo_por_termo("witcher")
assert len(resultado["jogos"]) == 1  # FALHOU: retornou 0 jogos
assert resultado["jogos"][0].titulo == "The Witcher 3"  # Não executado devido à falha anterior
```

#### 4.2.3 BUG-004: Falha de Filtragem (Catálogo - Exibição de Itens Inativos)

**Descrição:** O sistema exibe jogos inativos na listagem do catálogo, quando deveria filtrar e exibir apenas jogos com status "ativo".

**Análise Técnica:**
- **Localização:** `tests/integracao/test_catalogo_integracao.py::test_listar_todos_exibe_somente_ativos`
- **Causa Raiz:** O método `listar_todos()` em `CatalogoService` não aplica filtro por status antes de retornar os jogos.
- **Impacto:** Usuários visualizam jogos indisponíveis para compra, gerando frustração ao tentar adicionar ao carrinho jogos que não podem ser adquiridos.
- **Severidade:** Média - Funcionalidade parcialmente operacional
- **Prioridade:** Alta - Impacta diretamente a experiência de compra

**Evidência do Teste:**
```python
# Listagem deveria conter apenas jogos ativos
resultado = integ_catalogo_service.listar_todos()
titulos = [j.titulo for j in resultado["jogos"]]
assert "The Witcher 3" in titulos  # PASS
assert "Grand Theft Auto VI" not in titulos  # FALHOU: jogo inativo foi exibido
```

#### 4.2.4 Matriz de Defeitos

Os defeitos foram catalogados na Matriz de Defeitos (`docs/Matriz_de_Defeitos.md`) com severidade e prioridade:

| ID | Módulo | Descrição | Severidade | Prioridade | Status |
|----|--------|-----------|------------|------------|--------|
| BUG-1 | Biblioteca | Mensagem com aspas divergentes | Baixa | Baixa | Corrigido |
| BUG-002 | Carrinho | Violação RN1: permite adicionar jogo já comprado | Alta | Alta | Aberto |
| BUG-003 | Catálogo | Busca case-sensitive falha | Média | Média | Aberto |
| BUG-004 | Catálogo | Exibe jogos inativos na listagem | Média | Alta | Aberto |

**Resumo de Defeitos:**
- Total de Defeitos Encontrados: 4
- Defeitos Corrigidos: 1 (25% de taxa de resolução)
- Defeitos em Aberto: 3 (2 Alta severidade, 1 Média severidade)

### 4.3 Análise da Eficácia dos Testes

A taxa de aprovação de 95% (57 de 60 testes) indica que a maioria das funcionalidades está operacional. No entanto, os 3 testes reprovados identificaram defeitos críticos que violam requisitos de negócio documentados, demonstrando que:

1. **Os testes de integração foram eficazes** ao identificar falhas na interação entre componentes que não seriam detectadas por testes unitários isolados.

2. **A metodologia TDD foi validada** ao garantir que os testes foram escritos antes da implementação, permitindo detectar violações de requisitos desde o início.

3. **A cobertura de 97% não garante ausência de defeitos**, pois os bugs encontrados estão relacionados a lógica de negócio incorreta, não a código não coberto.

---

## 5. Conclusão Técnica

Conclui-se que, apesar da alta cobertura de código (97%) e da taxa de aprovação de 95% (57 de 60 testes), o sistema não atende aos critérios de aceite para produção devido a falhas críticas nas regras de negócio de compra e busca.

Os testes automatizados cumpriram seu objetivo ao identificar 3 defeitos que violam requisitos documentados:
- **BUG-002:** Violação da Regra de Negócio RN1 (posse única de jogos)
- **BUG-003:** Busca case-sensitive causando falsos negativos
- **BUG-004:** Exibição de jogos inativos no catálogo

A metodologia TDD aplicada durante o desenvolvimento garantiu que os testes fossem escritos baseados nos requisitos, permitindo detectar estas violações. A estratégia de testes de integração foi fundamental para identificar falhas na interação entre componentes que não seriam detectadas por testes unitários isolados.

**Recomendações:**
1. Corrigir os defeitos apontados na Matriz de Defeitos (BUG-002, BUG-003, BUG-004) antes de uma nova rodada de testes de regressão.
2. Implementar validação de regras de negócio no `CarrinhoService` antes de adicionar itens ao carrinho.
3. Normalizar strings para comparação case-insensitive na busca do catálogo.
4. Aplicar filtro de status "ativo" no método `listar_todos()` do `CatalogoService`.
5. Re-executar a suíte completa de testes após correções para validar que os defeitos foram resolvidos e que não foram introduzidos novos problemas.

Após a correção dos defeitos e re-execução dos testes com 100% de aprovação, o sistema poderá ser considerado pronto para produção.

---

## 6. Artefatos de Entrega

- **Plano de Testes (IEEE 829):** [Plano_de_Teste.md](Plano_de_Teste.md)
- **Casos de Teste:** [Casos_de_Teste.md](Casos_de_Teste.md) - 19 casos documentados
- **Matriz de Defeitos:** [Matriz_de_Defeitos.md](Matriz_de_Defeitos.md)
- **Casos de Uso:** [Casos de Uso.md](Casos%20de%20Uso.md)
- **Scripts de Testes Automatizados:**
  - Testes Unitários: 6 arquivos, 44 testes
  - Testes de Integração: 4 arquivos, 15 testes
  - Testes E2E: 1 arquivo, 1 teste
- **Relatório Final:** Este documento

---

## 7. Informações Técnicas

**Ambiente de Execução:**
- Data: 18 de dezembro de 2025
- Versão Python: 3.14
- Framework de Testes: pytest 9.0.1
- Coverage Tool: pytest-cov 7.0.0

