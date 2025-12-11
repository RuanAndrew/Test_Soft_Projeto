# 📄 Especificação de Casos de Uso


## UC01 – ADQUIRIR JOGO 


**DESCRIÇÃO SUCINTA:** O Cliente busca um jogo no catálogo, adiciona ao carrinho e efetua a compra para liberá-lo em sua biblioteca pessoal.

**ATORES** 
1. Cliente (Usuário Logado)

**PRÉ-CONDIÇÕES** 
1. O usuário deve estar autenticado no sistema (Login realizado).  
2. O catálogo deve possuir jogos cadastrados com status "Ativo".

**FLUXO BÁSICO** 
1. O Cliente seleciona a opção de "Buscar Jogo" ou navega pelo Catálogo.  
2. O Sistema exibe a lista de jogos disponíveis com seus respectivos preços.  
3. O Cliente seleciona um jogo específico para ver detalhes.  
4. O Sistema exibe a capa, descrição, preço e o botão de compra.  
5. O Cliente seleciona a opção "Adicionar ao Carrinho".  
6. O Sistema valida se o usuário já possui o jogo (verificando a regra RN1).  
7. O Sistema adiciona o item e atualiza o valor total do carrinho.  
8. O Cliente seleciona a opção "Finalizar Compra".  
9. O Sistema processa o pagamento.  
10. O Sistema libera o acesso ao jogo na conta do usuário, conforme regra RN2.  
11. O Sistema exibe a mensagem "Compra realizada com sucesso" e redireciona para a Biblioteca.  
12. O caso de uso é encerrado.

**FLUXOS ALTERNATIVOS**

**(A1) Alternativa ao Passo 6 – Jogo já adquirido** <br>
1.a O Sistema identifica que o jogo já consta na biblioteca do usuário (RN1).  
1.b O Sistema exibe um botão para Jogar/Instalar agora

**(A2) Alternativa ao Passo 8 – Carrinho Vazio ou Desistência** <br>
2.a O Cliente decide remover o item do carrinho antes de finalizar.  
2.b O Sistema atualiza o total para R$ 0,00.  
2.c O Sistema desabilita o botão "Finalizar Compra".  
2.d O caso de uso retorna ao Passo 1 ou encerra.


**REGRAS DE NEGÓCIO** <br>
**(RN1)** Verificação de Posse Única: Um usuário não pode comprar um jogo que já esteja vinculado à sua conta (status COMPRADO).  
**(RN2)** Liberação Imediata: Após a confirmação do pagamento, o status do jogo deve mudar para "COMPRADO" e o download deve ficar disponível imediatamente.

---

## UC02 – GERENCIAR BIBLIOTECA

**DESCRIÇÃO SUCINTA:** O Cliente gerencia o ciclo de vida dos jogos adquiridos realizando download, instalação ou desinstalação

**ATORES** 
1. Cliente (Usuário Logado)

**PRÉ-CONDIÇÕES** 
1. Possuir jogos na conta (caso de uso "UC01 – Adquirir Jogo") 

**FLUXO BÁSICO**
1. O Cliente acessa a área "Minha Biblioteca".  
2. O Sistema lista todos os jogos adquiridos pelo usuário.
3. O Cliente localiza um jogo com status "NÃO INSTALADO"
4. O Cliente seleciona a opção "Baixar/Instalar".  
5. O Sistema simula o download e altera o status do jogo para "INSTALADO".  
6. O Sistema habilita o botão "Jogar".  
7. O caso de uso é encerrado.

**FLUXOS ALTERNATIVOS**

**(A1) Alternativa ao Passo 3 – Desinstalar Jogo** <br>
1.a O Cliente seleciona um jogo que já possui status "INSTALADO".  
1.b O Cliente seleciona a opção "Desinstalar".  
1.c O Sistema remove o jogo e altera o status para "NÃO INSTALADO".  
1.d O Sistema exibe a opção "Instalar".  
1.e O caso de uso é encerrado.


---
