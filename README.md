# 🛡️ Projeto de Teste de Software: E-commerce de Jogos Digitais

## 🎓 Trabalho Acadêmico

Este projeto foi desenvolvido como requisito avaliativo da disciplina **Teste de Software** com o objetivo de aplicar e exercitar as principais técnicas, conceitos e metodologias no ciclo de vida de um produto digital.

O sistema selecionado para aplicação dos testes é um protótipo de **E-commerce de Jogos Digitais**.

---

## 🎯 Objetivo Geral do Projeto

Garantir a qualidade do sistema de E-commerce de Jogos Digitais, aplicando um processo de teste sistemático que abrange desde o planejamento e documentação até a execução e automatização

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


**© 2025 - Projeto Acadêmico de Teste de Software**
