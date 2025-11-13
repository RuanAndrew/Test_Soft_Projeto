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
| **Entrada** | **The Witcher 3** |
| **Pré-condições** | * O sistema deve estar online. <br> * O jogo "The Witcher 3" deve estar cadastrado no banco de dados com status ativo. |
| **Passos do Teste** | 1. Acessar a página principal da loja. <br> 2. Digitar na barra de pesquisa **"The Witcher 3"**. <br> 3. Pressionar a tecla "Enter" ou clicar no ícone de busca. |
| **Resultado Esperado** | O sistema deve exibir uma lista contendo o card do **"The Witcher 3"**, mostrando título, preço e capa. |

### TC-CAT-002: Busca por Termo Não Encontrado

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Busca por termo não corresponde a nenhum jogo. |
| **Entrada** | **Mineirinho Ultra Adventures** |
| **Pré-condições** | * O sistema deve estar online. |
| **Passos do Teste** | 1. Acessar a página principal da loja. <br> 2. Digitar na barra de pesquisa **"Mineirinho Ultra Adventures"**. <br> 3. Pressionar a tecla "Enter" ou clicar no ícone de busca. |
| **Resultado Esperado** | O sistema deve retornar uma lista vazia e exibir ao usuário a mensagem: **"Nenhum jogo encontrado para sua busca"**. |

---

## 🛒 Módulo: Carrinho (CAR)

### TC-CAR-001: Adição de jogo para compra

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se um jogo é adicionado com sucesso ao carrinho e se o carrinho reflete a inclusão. |
| **Entrada** | **Call of Duty®: Black Ops 7** (Preço: R$ 349,90) |
| **Pré-condições** | * O usuário deve estar logado. <br> * O carrinho deve estar vazio. <br> * O jogo deve estar disponível no catálogo. |
| **Passos** | 1. O usuário acessa a página de detalhes do jogo **"Call of Duty®: Black Ops 7"**. <br> 2. O usuário clica no botão "Adicionar ao Carrinho". <br> 3. O usuário navega para a página do Carrinho de Compras. |
| **Resultado Esperado** | O carrinho exibe o jogo **"Call of Duty®: Black Ops 7"**. <br> O ícone/contador do carrinho deve mostrar **(1)** item. <br> O total deve ser **R$ 349,90**. |

### TC-CAR-002: Remoção de jogo do Carrinho

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se um jogo é removido e se o carrinho é esvaziado, com o total zerado. |
| **Entrada** | **Call of Duty®: Black Ops 7**  |
| **Pré-condições** | * O usuário deve estar logado. <br> * O carrinho deve conter apenas o jogo **"Call of Duty®: Black Ops 7"**. |
| **Passos** | 1. O usuário acessa a página do Carrinho. <br> 2. O usuário localiza o jogo **"Call of Duty®: Black Ops 7"**. <br> 3. O usuário clica no botão/ícone de "Remover" (X ou lixeira) para o item. <br> 4. O sistema atualiza o carrinho. |
| **Resultado Esperado** | O jogo **"Call of Duty®: Black Ops 7"** é removido da lista. <br> O carrinho exibe a mensagem **"Seu carrinho está vazio"**. <br> O total é atualizado para **R$ 0,00**. |

### TC-CAR-003: Cálculo do Valor Total a Pagar

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se o sistema calcula o valor total somando o preço de itens diferentes no carrinho. |
| **Entrada** | Jogo 1: **"Call of Duty®: Black Ops 7"** (Preço: **R$ 349,90**); <br> Jogo 2: **"Hollow Knight"** (Preço: **R$ 46,99**) |
| **Pré-condições** | * O usuário deve estar logado. <br> * O carrinho deve estar vazio. <br> * Ambos os jogos devem estar disponíveis. |
| **Passos** | 1. O usuário adiciona o Jogo 1 ao carrinho. <br> 2. O usuário adiciona o Jogo 2 ao carrinho. <br> 3. O usuário acessa a página do Carrinho. |
| **Resultado Esperado** | O campo **Total estimado** deve exibir o valor exato da soma dos preços: **R$ 396,89**. |

---

## 📚 Módulo: Biblioteca do Usuário (LIB)

### TC-LIB-001: Visualização de Jogo Comprado

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se um jogo comprado pelo usuário é exibido corretamente na sua biblioteca pessoal. |
| **Entrada** | **"Cyberpunk 2077"** |
| **Pré-condições** | * O usuário deve estar logado. <br> * O jogo **"Cyberpunk 2077"** deve ter sido comprado e creditado na conta do usuário. |
| **Passos** | 1. O usuário acessa a página da **Biblioteca do Usuário**. <br> 2. O usuário verifica a lista de jogos na biblioteca. <br> 3. O usuário localiza o jogo **"Cyberpunk 2077"**. |
| **Resultado Esperado** | O card do jogo **"Cyberpunk 2077"** deve estar visível na lista e a opção "Baixar" ou "Jogar" |

### TC-LIB-002: Baixar/Jogar

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Valida se a funcionalidade de "Baixar" está disponível e funcional apenas para jogos comprados. |
| **Entrada** | **"Cyberpunk 2077"** |
| **Pré-condições** | * O usuário deve estar logado. <br> * O jogo **"Cyberpunk 2077"** deve ter sido comprado e creditado na conta do usuário. |
| **Passos** | 1. O usuário acessa a página da Biblioteca do Usuário. <br> 2. O usuário localiza o jogo **"Cyberpunk 2077"**. <br> 3. O usuário clica no botão **"Baixar"** ou **"Jogar"**. |
| **Resultado Esperado** | O botão "Baixar/Jogar" deve estar **ativo**. <br> Ao clicar, o sistema deve iniciar o download ou abrir o jogo  |

### TC-LIB-003: Busca por Jogo Não Adquirido

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Assegura que um jogo não comprado pelo usuário **não** aparece em sua biblioteca e verifica se o sistema oferece uma chamada para adquiri-lo. |
| **Entrada** | **"Street Fighter"** |
| **Pré-condições** | * O usuário deve estar logado. <br> * O jogo **"Street Fighter"** deve existir no catálogo, mas **NÃO** deve ter sido comprado pelo usuário de teste. |
| **Passos** | 1. O usuário acessa a página da Biblioteca do Usuário. <br> 2. O usuário utiliza a barra de busca da biblioteca para procurar por **"Street Fighter"**. <br> |
| **Resultado Esperado** | Deve ser exibida uma mensagem chamativa, como **"Parece que este jogo ainda não é seu! Adquira 'Street Fighter' na loja."** junto a um **link/botão** que direcione para a página de detalhes do jogo no Catálogo. |
