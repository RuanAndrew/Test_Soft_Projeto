# 📝 Casos de Teste

## Sistema: E-commerce de Jogos Digitais
A estrutura do ID do Caso de Teste é: TC-[MÓDULO_ABREVIADO]-[NÚMERO_SEQUENCIAL] 

Exemplo: TC-CAT-001. Onde "TC" é a abreviação de "Test Case"

---

## 🔎 Módulo: Catálogo (CAT)

### TC-CAT-001: Busca de Jogo Existente e Ativo

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verificar busca de jogo existente e ativo. |
| **Entrada** | Buscar o jogo **"The Witcher 3"** |
| **Pré-Requisitos** | 1. O sistema deve estar online. <br> 2. O jogo "The Witcher 3" deve estar cadastrado no banco de dados com status ativo. |
| **Passos do Teste** | 1. Acessar a página principal da loja. <br> 2. Digitar na barra de pesquisa **"The Witcher 3"**. <br> 3. Pressionar a tecla "Enter" ou clicar no ícone de busca. |
| **Resultado Esperado** | O sistema deve exibir uma lista contendo o card do **"The Witcher 3"**, mostrando título, preço e capa. |

### TC-CAT-002: Busca por Termo Não Encontrado

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Busca por termo não corresponde a nenhum jogo. |
| **Entrada** | Buscar o jogo **"Mineirinho Ultra Adventures"** |
| **Pré-Requisitos** | 1. O sistema deve estar online. |
| **Passos do Teste** | 1. Acessar a página principal da loja. <br> 2. Digitar na barra de pesquisa **"Mineirinho Ultra Adventures"**. <br> 3. Pressionar a tecla "Enter" ou clicar no ícone de busca. |
| **Resultado Esperado** | O sistema deve retornar uma lista vazia e exibir ao usuário a mensagem: **"Nenhum jogo encontrado para sua busca"**. |

---

## 🛒 Módulo: Carrinho (CAR)

### TC-CAR-001: Adição Bem-Sucedida de Item Único

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se um jogo é adicionado com sucesso ao carrinho e se o carrinho reflete a inclusão. |
| **Entrada** | Jogo: **"Call of Duty®: Black Ops 7"** (Preço: **R$ 349,90**) |
| **Pré-condições** | O usuário deve estar logado e o carrinho deve estar vazio. O jogo deve estar disponível no catálogo. |
| **Passos** | 1. O usuário acessa a página de detalhes do jogo **"Call of Duty®: Black Ops 7"**. <br> 2. O usuário clica no botão "Adicionar ao Carrinho". <br> 3. O usuário navega para a página do Carrinho de Compras. |
| **Resultado Esperado** | O carrinho exibe o jogo **"Call of Duty®: Black Ops 7"**. O ícone/contador do carrinho deve mostrar **(1)** item. O subtotal deve ser **R$ 349,90**. |

### TC-CAR-002: Remoção de Item e Atualização do Carrinho

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se um item é removido e se o carrinho é esvaziado, com o subtotal zerado. |
| **Entrada** | Jogo para Remover: **"Call of Duty®: Black Ops 7"** (Preço: **R$ 349,90**) |
| **Pré-condições** | O usuário deve estar logado. O carrinho deve conter apenas o jogo **"Call of Duty®: Black Ops 7"**. |
| **Passos** | 1. O usuário acessa a página do Carrinho. <br> 2. O usuário localiza o jogo **"Call of Duty®: Black Ops 7"**. <br> 3. O usuário clica no botão/ícone de "Remover" (X ou lixeira) para o item. <br> 4. O sistema atualiza o carrinho. |
| **Resultado Esperado** | O jogo **"Call of Duty®: Black Ops 7"** é removido da lista. O carrinho exibe a mensagem **"Seu carrinho está vazio"**. O subtotal é atualizado para **R$ 0,00**. |

### TC-CAR-003: Cálculo do Valor Total a Pagar

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se o sistema calcula o valor total somando o preço de itens diferentes no carrinho. |
| **Entrada** | Jogo 1: **"Call of Duty®: Black Ops 7"** (Preço: **R$ 349,90**); Jogo 2: **"Hollow Knight"** (Preço: **R$ 46,99**) |
| **Pré-condições** | O usuário deve estar logado e o carrinho deve estar vazio. Ambos os jogos devem estar disponíveis. |
| **Passos** | 1. O usuário adiciona o Jogo 1 ao carrinho. <br> 2. O usuário adiciona o Jogo 2 ao carrinho. <br> 3. O usuário acessa a página do Carrinho. |
| **Resultado Esperado** | O campo **Total estimado** deve exibir o valor exato da soma dos preços: **R$ 396,89**. |
