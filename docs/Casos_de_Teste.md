# 📝 Casos de Teste

## Sistema: E-commerce de Jogos Digitais
A estrutura do ID do Caso de Teste é: TC-[MÓDULO_ABREVIADO]-[NÚMERO_SEQUENCIAL] 

Exemplo: TC-CAT-001. Onde "TC" é a abreviação de "Test Case"

---

## 🔎 Módulo: Catálogo (CAT)
### TC-CAT-001: Busca de Jogo Existente e Ativo 
**Técnica :** Partição de Equivalência

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verificar busca com termo existente no banco (Classe Válida) |
| **Entrada** | **"The Witcher 3"** |
| **Pré-condições** | O jogo deve estar cadastrado e com status "Ativo". |
| **Passos** | 1. Acessar a página principal. <br> 2. Digitar **"The Witcher 3"** e confirmar. |
| **Resultado Esperado** | O sistema deve exibir o card do jogo **"The Witcher 3"** com preço e detalhes visíveis |

### TC-CAT-002: Busca por Termo Não Encontrado 
**Técnica :** Partição de Equivalência


| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verificar busca com termo que não corresponde a nenhum jogo (Classe Inválida). |
| **Entrada** | **"Mineirinho Ultra Adventures"** |
| **Pré-condições** | O jogo NÃO deve existir no catálogo. |
| **Passos** | 1. Acessar a página principal. <br> 2. Digitar **"Mineirinho Ultra Adventures"** e confirmar. |
| **Resultado Esperado** | O sistema deve retornar uma lista vazia e exibir ao usuário a mensagem: **"Nenhum jogo encontrado para sua busca"**. |

### TC-CAT-003: Listagem Completa Dos Jogos Ativos No Catálogo
**Técnica :** Partição de Equivalência


| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se a listagem completa do catálogo exibe apenas os jogos com status "ativo", ocultando os "inativos". |
| **Entrada** | Ação de "Ver Todos os Jogos" |
| **Pré-condições** | O banco deve conter jogos mistos (Ativos e Inativos). |
| **Passos** | 1. Acessar a página catálogo. <br> 2. Solicitar listagem de todos os jogos. |
| **Resultado Esperado** | O sistema deve retornar uma lista contendo apenas os jogos ativos. O jogo inativo não deve aparecer. |

---

## 🛒 Módulo: Carrinho (CAR)

### TC-CAR-001: Adição de jogo para compra
**Técnica:** Partição de Equivalência

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se um jogo é adicionado com sucesso ao carrinho e se o carrinho reflete a inclusão. |
| **Entrada** | **Call of Duty®: Black Ops 7** (Preço: R$ 349,90) |
| **Pré-condições** | * O usuário deve estar logado. <br> * O carrinho deve estar vazio. <br> * O jogo deve estar disponível no catálogo. |
| **Passos** | 1. O usuário acessa a página de detalhes do jogo **"Call of Duty®: Black Ops 7"**. <br> 2. O usuário clica no botão "Adicionar ao Carrinho". <br> 3. O usuário navega para a página do Carrinho de Compras. |
| **Resultado Esperado** | O carrinho exibe o jogo **"Call of Duty®: Black Ops 7"**. <br> O ícone/contador do carrinho deve mostrar **(1)** item. <br> O total deve ser **R$ 349,90**. |

### TC-CAR-002: Esvaziar Carrinho 
**Técnica:** Análise de Valor Limite (AVL)

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se um jogo é removido e se o carrinho é esvaziado (Testa o limite inferior do carrinho) |
| **Entrada** | Ação de Remover Item. |
| **Pré-condições** | Carrinho contendo exatamente **1 item**. |
| **Passos** | 1. No carrinho, clicar no ícone de "Remover" |
| **Resultado Esperado** | O item é removido da lista. <br> O carrinho exibe a mensagem **"Seu carrinho está vazio"**. <br> O total é atualizado para **R$ 0,00**. | |

### TC-CAR-003: Cálculo do Valor Total a Pagar
**Técnica:** Partição de Equivalência

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se o sistema calcula o valor total somando o preço de itens diferentes no carrinho. |
| **Entrada** | Jogo 1: **"Call of Duty®: Black Ops 7"** (Preço: **R$ 349,90**); <br> Jogo 2: **"Hollow Knight"** (Preço: **R$ 46,99**) |
| **Pré-condições** | * O usuário deve estar logado. <br> * O carrinho deve estar vazio. <br> * Ambos os jogos devem estar disponíveis. |
| **Passos** | 1. O usuário adiciona o Jogo 1 ao carrinho. <br> 2. O usuário adiciona o Jogo 2 ao carrinho. <br> 3. O usuário acessa a página do Carrinho. |
| **Resultado Esperado** | O campo **Total estimado** deve exibir o valor exato da soma dos preços: **R$ 396,89**. |

### TC-CAR-004: Bloqueio de Compra de Jogo Já Adquirido
**Técnica:** Partição de Equivalência

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Valida se o botão de compra é bloqueado ou se o sistema rejeita a adição ao carrinho de um jogo que o usuário já possui na biblioteca. |
| **Entrada** | Ação "Adicionar ao Carrinho" no jogo "The Witcher 3" |
| **Pré-condições** | Usuário JÁ POSSUI "The Witcher 3" na biblioteca com status "COMPRADO" ou "INSTALADO". |
| **Passos** | 1. Acessar a página do catálogo ou detalhes do jogo "The Witcher 3". <br> 2. Tentar clicar no botão de adicionar ao carrinho.|
| **Resultado Esperado** | O sistema deve impedir a ação.|

### TC-CAR-005: Compra de Jogos Gratuitos
**Técnica:** Análise de Valor Limite (AVL)

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica o comportamento do cálculo total quando os itens custam R$ 0,00. |
| **Entrada** | Jogo: "Free Game Demo" (Preço: R$ 0,00) |
| **Pré-condições** | Carrinho vazio. |
| **Passos** | 1. Adicionar o jogo gratuito ao carrinho. <br> 2. Ir para o checkout. |
| **Resultado Esperado** | O Total a Pagar deve ser R$ 0,00. O botão de "Finalizar Compra" deve funcionar normalmente, sem exigir pagamento. |

---

## 📚 Módulo: Biblioteca do Usuário (LIB)

### TC-LIB-001: Visualização de Jogo Comprado
**Técnica:** Partição de Equivalência

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se um jogo comprado pelo usuário é exibido corretamente na sua biblioteca pessoal. |
| **Entrada** | **"Cyberpunk 2077"** |
| **Pré-condições** | * O usuário deve estar logado. <br> * O jogo **"Cyberpunk 2077"** deve ter sido comprado e creditado na conta do usuário. |
| **Passos** | 1. O usuário acessa a página da **Biblioteca do Usuário**. <br> 2. O usuário verifica a lista de jogos na biblioteca. <br> 3. O usuário localiza o jogo **"Cyberpunk 2077"**. |
| **Resultado Esperado** | O card do jogo **"Cyberpunk 2077"** deve estar visível na lista e a opção "Baixar" ou "Jogar" |

### TC-LIB-002: Baixar/Jogar
**Técnica:** Partição de Equivalência

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Valida se a funcionalidade de "Baixar" está disponível e funcional apenas para jogos comprados. |
| **Entrada** | **"Cyberpunk 2077"** |
| **Pré-condições** | * O usuário deve estar logado. <br> * O jogo **"Cyberpunk 2077"** deve ter sido comprado e creditado na conta do usuário. |
| **Passos** | 1. O usuário acessa a página da Biblioteca do Usuário. <br> 2. O usuário localiza o jogo **"Cyberpunk 2077"**. <br> 3. O usuário clica no botão **"Baixar"** ou **"Jogar"**. |
| **Resultado Esperado** | O botão "Baixar/Jogar" deve estar **ativo**. <br> Ao clicar, o sistema deve iniciar o download ou abrir o jogo  |

### TC-LIB-003: Busca por Jogo Não Adquirido
**Técnica:** Partição de Equivalência

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Assegura que um jogo não comprado pelo usuário **não** aparece em sua biblioteca e verifica se o sistema oferece uma chamada para adquiri-lo. |
| **Entrada** | **"Street Fighter"** |
| **Pré-condições** | * O usuário deve estar logado. <br> * O jogo **"Street Fighter"** deve existir no catálogo, mas **NÃO** deve ter sido comprado pelo usuário de teste. |
| **Passos** | 1. O usuário acessa a página da Biblioteca do Usuário. <br> 2. O usuário utiliza a barra de busca da biblioteca para procurar por **"Street Fighter"**. <br> |
| **Resultado Esperado** | Deve ser exibida uma mensagem chamativa, como **"Parece que este jogo ainda não é seu! Adquira 'Street Fighter' na loja."** junto a um **link/botão** que direcione para a página de detalhes do jogo no Catálogo. |


### TC-LIB-004: Desinstalação de Jogo
**Técnica:** Transição de Estados (instalado -> desinstalado)

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se o usuário consegue desinstalar um jogo previamente instalado e se o sistema atualiza corretamente o status do jogo na biblioteca.|
| **Entrada** | **"Street Fighter"** (Ação de Desinstalar)|
| **Pré-condições** | * O usuário deve estar logado. <br> * O jogo "Street Fighter" deve constar na biblioteca do usuário. <br> * O jogo deve estar atualmente com o status "Instalado" na máquina. |
| **Passos** | 1. O usuário acessa a página da Biblioteca do Usuário. <br>  2. O usuário localiza e seleciona o jogo "Street Fighter".<br>  3. O usuário clica na opção/botão "Desinstalar". <br>  4. O usuário confirma a ação na janela de aviso. <br> |
| **Resultado Esperado** | O jogo deve ser removido da máquina, e na biblioteca o status deve ser atualizado para “Não instalado”, exibindo um botão como “Instalar novamente”. Uma mensagem de feedback deve aparecer informando "O jogo foi desinstalado com sucesso."|

---                                                                                        
## 👤 Módulo: Conta do Usuário (USR)

### TC-USR-001: Criar Nova Conta
**Técnica:** Partição de Equivalência

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se um novo usuário consegue criar uma conta no sistema com dados válidos.|
| **Entrada** | Nome: Matheus <br> E-mail: matheus@email.com <br> Senha: Teste@123|
| **Pré-condições** | * O usuário não deve possuir uma conta registrada com o e-mail fornecido. <br> * O sistema deve estar online. |
| **Passos** | 1. Acessar a página de Cadastro.<br> 2. Preencher os campos: nome, e-mail e senha.<br> 3. Clicar no botão "Criar conta". |
| **Resultado Esperado** | A conta deve ser criada com sucesso e o sistema deve redirecionar para a página de boas-vindas ou dashboard, exibindo a mensagem "Conta criada com sucesso!".|

### TC-USR-002: Alterar Senha
**Técnica:** Partição de Equivalência

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Valida se o usuário consegue alterar sua senha com sucesso.|
| **Entrada** | Senha atual: Teste@123 <br> Nova senha: NovaSenha@456|
| **Pré-condições** | * O usuário deve estar logado.<br>* A senha atual deve ser válida. |
| **Passos** | 1. Acessar o menu de Configurações da Conta.<br>2. Selecionar a opção "Alterar Senha".<br>3. Digitar a senha atual.<br> 4. Digitar e confirmar a nova senha.<br>5. Clicar em "Salvar".|
| **Resultado Esperado** | Mensagem: "Senha alterada com sucesso." O sistema deve exigir a nova senha no próximo login.|

### TC-USR-003: Atualizar Dados do Perfil
**Técnica:** Partição de Equivalência

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se o usuário consegue atualizar dados do perfil, como nome ou e-mail.|
| **Entrada** | Nome atualizado: **Zezinho da silva**|
| **Pré-condições** | * O usuário deve estar logado. |
| **Passos** | 1. Acessar o menu Perfil.<br> 2. Editar pelo menos um campo.<br> 3. Clicar em "Salvar alterações".|
| **Resultado Esperado** | O sistema exibe a mensagem "Dados atualizados com sucesso." Os novos dados devem ser refletidos imediatamente no perfil.|

### TC-USR-004: Falha ao Fazer Login
**Técnica:** Partição de Equivalência

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Testa se o sistema lida corretamente com tentativas de login inválidas.|
| **Entrada** | E-mail: joao@email.com <br> Senha: SenhaErrada|
| **Pré-condições** | * O usuário deve já possuir uma conta registrada. |
| **Passos** | 1. Acessar a página de Login.<br>2. Digitar e-mail válido.<br>3. Digitar senha incorreta.<br> 4. Clicar em "Entrar".|
| **Resultado Esperado** | O sistema deve exibir mensagem amigável: "E-mail ou senha incorretos. Tente novamente." O usuário não deve ser autenticado.|

### TC-USR-005: Logout
**Técnica:** Transição de Estados (logado -> deslogado)

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Verifica se o usuário consegue encerrar sua sessão corretamente.|
| **Entrada** | Ação de Logout (Encerrar Sessão)|
| **Pré-condições** | * O usuário deve estar logado. |
| **Passos** | 1. Clicar no menu do usuário.<br>2. Selecionar a opção "Sair" ou "Logout".|
| **Resultado Esperado** | O sistema finaliza a sessão e redireciona o usuário para a tela de login ou página inicial pública.|
                                                                
---                                                                                        
## 🔄 Módulo: Sistema (SYS) - End-to-End

### TC-SYS-001: Jornada Completa do Usuário 
Técnica baseada nos casos de uso UC01, UC02, UC03

| Item | Detalhe |
| :--- | :--- |
| **Descrição** | Valida o fluxo principal de valor do software: de um visitante desconhecido até um jogador com o jogo baixado. |
| **Entrada** | Dados de novo usuário + Seleção de Jogo + Fluxo de Compra. |
| **Pré-condições** | Banco de dados limpo para esse usuário (novo registro). |
| **Passos** | 1. (USR) Registrar nova conta "GamerPro".<br> 2. (USR) Fazer Login.<br> 3. (CAT) Buscar por "Street Fighter".<br> 4. (CAR) Adicionar ao Carrinho e Validar Total.<br> 5. (CAR) Finalizar Compra.<br> 6. (LIB) Verificar se jogo aparece na Biblioteca com status "Comprado".<br> 7. (LIB) Clicar em "Baixar".|
| **Resultado Esperado** | O fluxo não deve apresentar erros bloqueantes. Ao final, o jogo deve estar com status "Baixando/Instalado" e o saldo/histórico de compras atualizado. |