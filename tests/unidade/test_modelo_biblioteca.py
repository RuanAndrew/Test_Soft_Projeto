import pytest
from src.models.Jogo import Jogo
from src.models.Biblioteca import Biblioteca


class TestModeloBiblioteca:
    """Testes unitários para o modelo Biblioteca - Teste de Caixa Branca"""

    def test_criar_biblioteca_vazia(self):
        """Teste de criação de uma biblioteca vazia"""
        biblioteca = Biblioteca(usuario_id=1)

        assert biblioteca.usuario_id == 1
        assert biblioteca.jogos_comprados == []
        assert biblioteca.jogos_instalados == []

    def test_adicionar_jogo_a_biblioteca(self):
        """Teste de adição de um jogo à biblioteca de comprados"""
        biblioteca = Biblioteca(usuario_id=1)
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        resultado = biblioteca.adicionar_jogo(jogo)

        assert resultado is True
        assert len(biblioteca.jogos_comprados) == 1
        assert jogo in biblioteca.jogos_comprados

    def test_adicionar_jogo_duplicado(self):
        """Teste de tentativa de adicionar o mesmo jogo duas vezes"""
        biblioteca = Biblioteca(usuario_id=1)
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        biblioteca.adicionar_jogo(jogo)
        resultado = biblioteca.adicionar_jogo(jogo)

        assert resultado is False
        assert len(biblioteca.jogos_comprados) == 1

    def test_remover_jogo_da_biblioteca(self):
        """Teste de remoção de um jogo da biblioteca"""
        biblioteca = Biblioteca(usuario_id=1)
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        biblioteca.adicionar_jogo(jogo)
        resultado = biblioteca.remover_jogo(jogo)

        assert resultado is True
        assert len(biblioteca.jogos_comprados) == 0

    def test_remover_jogo_nao_existente(self):
        """Teste de tentativa de remover um jogo que não está na biblioteca"""
        biblioteca = Biblioteca(usuario_id=1)
        jogo1 = Jogo(id=1, titulo="The Witcher 3", preco=99.99)
        jogo2 = Jogo(id=999, titulo="Game Inexistente", preco=50.0)

        biblioteca.adicionar_jogo(jogo1)
        resultado = biblioteca.remover_jogo(jogo2)

        assert resultado is False
        assert len(biblioteca.jogos_comprados) == 1

    def test_instalar_jogo_comprado(self):
        """Teste de instalação de um jogo que foi comprado"""
        biblioteca = Biblioteca(usuario_id=1)
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        biblioteca.adicionar_jogo(jogo)
        resultado = biblioteca.instalar_jogo(jogo)

        assert resultado is True
        assert jogo in biblioteca.jogos_instalados

    def test_instalar_jogo_nao_comprado(self):
        """Teste de tentativa de instalar um jogo não comprado"""
        biblioteca = Biblioteca(usuario_id=1)
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        resultado = biblioteca.instalar_jogo(jogo)

        assert resultado is False
        assert len(biblioteca.jogos_instalados) == 0

    def test_instalar_jogo_ja_instalado(self):
        """Teste de tentativa de instalar novamente um jogo já instalado"""
        biblioteca = Biblioteca(usuario_id=1)
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        biblioteca.adicionar_jogo(jogo)
        biblioteca.instalar_jogo(jogo)
        resultado = biblioteca.instalar_jogo(jogo)

        assert resultado is False
        assert len(biblioteca.jogos_instalados) == 1

    def test_desinstalar_jogo(self):
        """Teste de desinstalação de um jogo"""
        biblioteca = Biblioteca(usuario_id=1)
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        biblioteca.adicionar_jogo(jogo)
        biblioteca.instalar_jogo(jogo)
        resultado = biblioteca.desinstalar_jogo(jogo)

        assert resultado is True
        assert jogo not in biblioteca.jogos_instalados
        assert jogo in biblioteca.jogos_comprados  # Jogo continua comprado

    def test_desinstalar_jogo_nao_instalado(self):
        """Teste de tentativa de desinstalar um jogo não instalado"""
        biblioteca = Biblioteca(usuario_id=1)
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        biblioteca.adicionar_jogo(jogo)
        resultado = biblioteca.desinstalar_jogo(jogo)

        assert resultado is False

    def test_possui_jogo_comprado(self):
        """Teste de verificação se possuir um jogo comprado"""
        biblioteca = Biblioteca(usuario_id=1)
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        biblioteca.adicionar_jogo(jogo)
        assert biblioteca.possui_jogo(jogo) is True

    def test_nao_possui_jogo(self):
        """Teste de verificação se não possuir um jogo"""
        biblioteca = Biblioteca(usuario_id=1)
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        assert biblioteca.possui_jogo(jogo) is False

    def test_listar_jogos_comprados(self):
        """Teste de listagem de todos os jogos comprados"""
        biblioteca = Biblioteca(usuario_id=1)
        jogo1 = Jogo(id=1, titulo="The Witcher 3", preco=99.99)
        jogo2 = Jogo(id=2, titulo="Cyberpunk 2077", preco=199.90)

        biblioteca.adicionar_jogo(jogo1)
        biblioteca.adicionar_jogo(jogo2)

        lista = biblioteca.listar_jogos_comprados()

        assert len(lista) == 2
        assert jogo1 in lista
        assert jogo2 in lista

    def test_listar_jogos_instalados(self):
        """Teste de listagem de todos os jogos instalados"""
        biblioteca = Biblioteca(usuario_id=1)
        jogo1 = Jogo(id=1, titulo="The Witcher 3", preco=99.99)
        jogo2 = Jogo(id=2, titulo="Cyberpunk 2077", preco=199.90)

        biblioteca.adicionar_jogo(jogo1)
        biblioteca.adicionar_jogo(jogo2)
        biblioteca.instalar_jogo(jogo1)

        lista = biblioteca.listar_jogos_instalados()

        assert len(lista) == 1
        assert jogo1 in lista
        assert jogo2 not in lista

    def test_remover_jogo_remove_tambem_instalado(self):
        """Teste que remover um jogo também o remove dos instalados"""
        biblioteca = Biblioteca(usuario_id=1)
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        biblioteca.adicionar_jogo(jogo)
        biblioteca.instalar_jogo(jogo)

        biblioteca.remover_jogo(jogo)

        assert jogo not in biblioteca.jogos_comprados
        assert jogo not in biblioteca.jogos_instalados

    def test_fluxo_completo_compra_instalacao_desinstalacao(self):
        """Teste do fluxo completo: compra -> instalação -> desinstalação"""
        biblioteca = Biblioteca(usuario_id=1)
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        # Compra
        assert biblioteca.adicionar_jogo(jogo) is True
        assert biblioteca.possui_jogo(jogo) is True

        # Instalação
        assert biblioteca.instalar_jogo(jogo) is True
        assert jogo in biblioteca.listar_jogos_instalados()

        # Desinstalação
        assert biblioteca.desinstalar_jogo(jogo) is True
        assert jogo not in biblioteca.listar_jogos_instalados()
        assert jogo in biblioteca.listar_jogos_comprados()

    def test_multiplos_jogos_fluxo_completo(self):
        """Teste de fluxo completo com múltiplos jogos"""
        biblioteca = Biblioteca(usuario_id=1)
        jogos = [
            Jogo(id=1, titulo="The Witcher 3", preco=99.99),
            Jogo(id=2, titulo="Cyberpunk 2077", preco=199.90),
            Jogo(id=3, titulo="Elden Ring", preco=249.90),
        ]

        # Compra todos
        for jogo in jogos:
            biblioteca.adicionar_jogo(jogo)

        assert len(biblioteca.listar_jogos_comprados()) == 3

        # Instala alguns
        biblioteca.instalar_jogo(jogos[0])
        biblioteca.instalar_jogo(jogos[1])

        assert len(biblioteca.listar_jogos_instalados()) == 2

        # Remove um
        biblioteca.remover_jogo(jogos[0])

        assert len(biblioteca.listar_jogos_comprados()) == 2
        assert len(biblioteca.listar_jogos_instalados()) == 1
