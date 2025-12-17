# 🛡️ Projeto de Teste de Software: E-commerce de Jogos Digitais

## 🎓 Trabalho Acadêmico

Este projeto foi desenvolvido como requisito avaliativo da disciplina **Teste de Software** com o objetivo de aplicar e exercitar as principais técnicas, conceitos e metodologias no ciclo de vida de um produto digital.

O sistema selecionado para aplicação dos testes é um protótipo de **E-commerce de Jogos Digitais**.

---

## 🎯 Objetivo Geral do Projeto

Garantir a qualidade do sistema de E-commerce de Jogos Digitais, aplicando um processo de teste sistemático que abrange desde o planejamento e documentação até a execução e automatização, conforme os padrões da indústria e diretrizes acadêmicas.

## 📊 Status do Projeto

| Item | Status | Cobertura |
|------|--------|-----------|
| Plano de Testes | ✅ Completo | IEEE 829 |
| Casos de Teste | ✅ 14 casos | 6+ requisitos |
| Testes Automatizados | ✅ 56 testes | 97% cobertura |
| Matriz de Defeitos | ✅ Completa | 1 defeito (corrigido) |
| Relatório Final | ✅ Completo | Com evidências |

---

## 📂 Artefatos de Entrega

### ✅ Documentação

| Artefato | Descrição | Local |
| :--- | :--- | :--- |
| **Plano de Teste** | Documento mestre (IEEE 829) definindo objetivos, escopo, estratégias, critérios de entrada/saída e riscos. | [docs/Plano_de_Teste.md](docs/Plano_de_Teste.md) |
| **Casos de Teste** | 14 casos de teste documentados com técnicas de especificação (PE, AVL, TD, TS) | [docs/Casos_de_Teste.md](docs/Casos_de_Teste.md) |
| **Matriz de Defeitos** | Registro formal de todas as falhas encontradas, com severidade, prioridade e status. | [docs/Matriz_de_Defeitos.md](docs/Matriz_de_Defeitos.md) |
| **Casos de Uso** | Especificação de 3 casos de uso principais com fluxos. | [docs/Casos%20de%20Uso.md](docs/Casos%20de%20Uso.md) |
| **Relatório Final** | Análise completa de cobertura, evidências (logs/prints) e conclusões. | [docs/Relatorio_Final.md](docs/Relatorio_Final.md) |

### ✅ Scripts de Automação

| Arquivo | Testes | Cobertura | Status |
|---------|--------|-----------|--------|
| `test_modelo_jogo.py` | 13 | 100% | ✅ PASS |
| `test_modelo_biblioteca.py` | 17 | 100% | ✅ PASS |
| `test_carrinho_integracao.py` | 13 | 100% | ✅ PASS |
| `test_carrinho.py` | 3 | 100% | ✅ PASS |
| `test_catalogo.py` | 2 | 100% | ✅ PASS |
| `test_cadastrar_usuario.py` | 5 | 94% | ✅ PASS |
| `test_biblioteca.py` | 3 | 94% | ✅ PASS |
| **TOTAL** | **56** | **97%** | **✅ 56 PASS** |

---

## 🏗️ Arquitetura do Sistema

```
src/
├── models/
│   ├── Usuario.py          (Entidade de usuário)
│   ├── Jogo.py            (Entidade de jogo)
│   ├── Catalogo.py        (Coleção de jogos)
│   └── Biblioteca.py      (Biblioteca do usuário)
│
└── services/
    ├── CadastroService.py     (Gestão de contas)
    ├── CatalogoService.py     (Busca de jogos)
    ├── CarrinhoService.py     (Carrinho de compras)
    └── BibliotecaService.py   (Biblioteca pessoal)

tests/
└── unidade/
    ├── test_modelo_jogo.py
    ├── test_modelo_biblioteca.py
    ├── test_carrinho.py
    ├── test_carrinho_integracao.py
    ├── test_catalogo.py
    ├── test_cadastrar_usuario.py
    └── test_biblioteca.py
```

---

## 🧪 Principais Funcionalidades Testadas

### 1️⃣ Catálogo de Jogos (CAT)
- ✅ Busca de jogo existente e ativo (Partição de Equivalência)
- ✅ Busca por termo não encontrado (Partição de Equivalência)

### 2️⃣ Carrinho de Compras (CAR)
- ✅ Adição de jogo para compra
- ✅ Esvaziar carrinho (Análise de Valor Limite)
- ✅ Cálculo do valor total a pagar
- ✅ Adição de múltiplos itens
- ✅ Remover itens específicos

### 3️⃣ Biblioteca do Usuário (LIB)
- ✅ Visualização de jogo comprado
- ✅ Baixar/Jogar jogo
- ✅ Busca por jogo não adquirido
- ✅ Desinstalação de jogo

### 4️⃣ Gerenciamento de Usuário (USR)
- ✅ Criar nova conta (Partição de Equivalência)
- ✅ Alterar senha
- ✅ Atualizar dados do perfil
- ✅ Falha ao fazer login (Teste Negativo)
- ✅ Logout

---

## 🧬 Técnicas de Teste Aplicadas

### Técnicas Baseadas em Especificação

#### 1. **Partição de Equivalência (PE)**
- Testes de classe válida: termo existente
- Testes de classe inválida: termo não existe
- Dividem entradas em grupos com comportamento similar

#### 2. **Análise de Valor Limite (AVL)**
- Testes nos limites: carrinho vazio (0 itens)
- Preço mínimo: R$ 0.00
- Preço máximo: R$ 9999.99
- Múltiplos itens no carrinho

#### 3. **Tabela de Decisão**
- Mapeamento de condições e ações
- Exemplo: Posse de jogo → Liberar download

#### 4. **Transição de Estados**
- Ciclo: Compra → Instalação → Desinstalação
- Verificação de mudanças de status

#### 5. **Casos de Uso**
- UC01: Adquirir Jogo
- UC02: Gerenciar Biblioteca
- UC03: Gerenciar Conta

---

## 📋 Tipos de Teste Realizados

### 1. **Testes Unitários (Caixa-Branca)**
- 40 testes de métodos individuais
- Validação de lógica interna
- Cobertura: 97%

### 2. **Testes de Integração**
- 13 testes de integração entre módulos
- Carrinho + Modelos Jogo
- Biblioteca + Usuário

### 3. **Testes Funcionais (Caixa-Preta)**
- 3 testes validando comportamentos do usuário
- Sem conhecimento da implementação interna

### 4. **Testes de Regressão**
- Re-testes após correção de BUG-1
- Validação que correção não introduziu novos problemas

### 5. **Testes Negativos**
- Falha ao fazer login com credenciais inválidas
- Remoção de item não existente no carrinho
- Desinstalação de jogo não instalado

---

## 🚀 Como Executar os Testes

### Pré-requisitos
```bash
python --version  # 3.10+
pip install -r requirements.txt
```

### Instalar Dependências
```bash
pip install pytest==9.0.1 pytest-cov==7.0.0 colorama==0.4.6
```

### Executar Todos os Testes
```bash
pytest tests/ -v
```

### Executar com Cobertura
```bash
pytest tests/ -v --cov=src --cov-report=term-missing
```

### Executar Arquivo Específico
```bash
pytest tests/unidade/test_carrinho.py -v
```

### Executar Teste Específico
```bash
pytest tests/unidade/test_carrinho.py::TestCarrinho::test_adicionar_jogo_ao_carrinho -v
```

### Gerar Relatório HTML
```bash
pytest tests/ --cov=src --cov-report=html
open htmlcov/index.html
```

---

## 📈 Resultados Finais

### Execução de Testes
```
============================= test session starts ==============================
Platform: Linux, Python 3.12.1, pytest-9.0.1

Collecting... 56 items

RESULTADO FINAL:
✅ 56 PASSED                                                          [100%]
❌ 0 FAILED                                                           [0%]
Tempo Total: 0.15 segundos

Coverage Report:
src/models/Biblioteca.py               100%
src/models/Jogo.py                     100%
src/services/CarrinhoService.py        100%
src/services/CatalogoService.py        100%
src/services/BibliotecaService.py       94%
src/services/CadastroService.py         94%
src/models/Catalogo.py                  86%
───────────────────────────────────────────
TOTAL COVERAGE                          97%
============================== 56 passed in 0.15s =========================
```

### Defeitos Encontrados
- **Total:** 1
- **Críticos:** 0
- **Altos:** 0
- **Médios:** 0
- **Baixos:** 1 ✅ Corrigido
- **Taxa de Resolução:** 100%

---

## 📚 Documentação das Técnicas

### Exemplo: Partição de Equivalência - TC-CAT-001
```
Entrada: "The Witcher 3"
Classe Válida: Termo que existe no banco de dados e jogo está ATIVO
Esperado: Sistema retorna o jogo com detalhes e preço
Status: ✅ PASS
```

### Exemplo: Análise de Valor Limite - TC-CAR-002
```
Pré-condição: Carrinho com 1 item (LIMITE INFERIOR)
Ação: Remover o item
Esperado: Carrinho vazio, mensagem "Seu carrinho está vazio"
Status: ✅ PASS
```

### Exemplo: Teste Negativo - TC-USR-004
```
Entrada: E-mail válido + Senha incorreta
Esperado: Acesso negado com mensagem "E-mail ou senha incorretos"
Status: ✅ PASS
```

---

## 📊 Matriz de Rastreabilidade

| Req | Caso Uso | Caso Teste | Status |
|-----|----------|-----------|--------|
| R1 | UC01 | TC-CAT-001, TC-CAT-002 | ✅ |
| R2 | UC01 | TC-CAR-001, TC-CAR-002, TC-CAR-003 | ✅ |
| R3 | UC02 | TC-LIB-001, TC-LIB-002, TC-LIB-003, TC-LIB-004 | ✅ |
| R4 | UC03 | TC-USR-001, TC-USR-002, TC-USR-003, TC-USR-004, TC-USR-005 | ✅ |

---

## 💡 Recomendações Futuras

### Curto Prazo ✅
- [x] Implementar 56 testes unitários
- [x] Alcançar 95%+ de cobertura
- [x] Corrigir todos os defeitos críticos

### Médio Prazo 📅
- [ ] Testes E2E com Selenium/Playwright
- [ ] Testes de Performance
- [ ] Testes de Segurança
- [ ] CI/CD com GitHub Actions

### Longo Prazo 🎯
- [ ] Testes de Compatibilidade
- [ ] Análise de Acessibilidade (WCAG)
- [ ] Testes de Usabilidade
- [ ] Análise Estática de Segurança (SAST)

---

## 👥 Informações do Projeto

**Versão:** 1.0  
**Data de Conclusão:** 17 de dezembro de 2025  
**Framework de Teste:** pytest  
**Cobertura Alcançada:** 97%  
**Status:** ✅ **APROVADO**

---

## 📞 Contato e Suporte

Para dúvidas sobre a execução dos testes ou interpretação dos resultados, consultar:
- Plano de Testes: [docs/Plano_de_Teste.md](docs/Plano_de_Teste.md)
- Casos de Teste: [docs/Casos_de_Teste.md](docs/Casos_de_Teste.md)
- Relatório Final: [docs/Relatorio_Final.md](docs/Relatorio_Final.md)

---

**© 2025 - Projeto Acadêmico de Teste de Software**
