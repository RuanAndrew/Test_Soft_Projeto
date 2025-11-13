# Casos de Teste

Casos de teste do sistema de E-commerce de Jogos Digitais

Para definir o id do caso de teste siga essa estrutura -> [TIPO_ARTEFATO]-[MÓDULO]-[NÚMERO_SEQUENCIAL]

exemplo: TC-CAT-001

TC é a abreviação de "Test Case"

CAT é a abreviação do módulo Catálogo

001 é um numero unico para aquele módulo

## Test Case ID -> TC-CAT-001

### Descrição do teste

Verificar busca de jogo existente e ativo

### Entrada 

Buscar o jogo "The Witcher 3"

### Pré-Requisitos

        1 - O sistema deve estar online
        2 - "The Witcher 3" esta cadastrado no banco de dados com status ativo

### Passos do teste

    1 - Acessar a pagina principal da loja
    2 - Digitar na barra de pesquisa "The Witcher 3"
    3 - Pressionar a tecla ""Enter"" ou clicar no icone de busca

### Resultado esperado

O sistema deve exibir uma lista contendo
 o card do "The Witcher 3", mostrando titulo, preço e capa


### Status

Pendente

## Test Case ID -> TC-CAT-002

### Descrição do teste

Busca por termo não corresponde a nenhum jogo

### Entrada 

Buscar o jogo "Mineirinho Ultra Adventures"

### Pré-Requisitos

        1 - O sistema deve estar online

### Passos do teste

    1 - Acessar a pagina principal da loja
    2 - Digitar na barra de pesquisa "Mineirinho Ultra Adventures"
    3 - Pressionar a tecla ""Enter"" ou clicar no icone de busca

### Resultado esperado

O sistema deve retornar uma lista vazia e exibir ao úsuario a mensagem: "Nenhum jogo encontrado para sua busca"

### Status

Pendente