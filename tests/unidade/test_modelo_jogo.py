import pytest
from src.models.Jogo import Jogo


class TestModeloJogo:
    """Testes unitários para o modelo Jogo - Teste de Caixa Branca"""

    def test_criar_jogo_com_todos_parametros(self):
        """Teste básico de criação de jogo com todos os parâmetros"""
        jogo = Jogo(
            id=1,
            titulo="The Witcher 3",
            preco=99.99,
            status="ativo",
            descricao="RPG de ação"
        )

        assert jogo.id == 1
        assert jogo.titulo == "The Witcher 3"
        assert jogo.preco == 99.99
        assert jogo.status == "ativo"
        assert jogo.descricao == "RPG de ação"

    def test_criar_jogo_com_parametros_minimos(self):
        """Teste de criação com apenas ID e título (parâmetros obrigatórios)"""
        jogo = Jogo(id=2, titulo="Cyberpunk 2077")

        assert jogo.id == 2
        assert jogo.titulo == "Cyberpunk 2077"
        assert jogo.preco == 0.0  # Default
        assert jogo.status == "ativo"  # Default
        assert jogo.descricao == ""  # Default

    def test_comparacao_igualdade_por_id(self):
        """Teste de igualdade entre objetos Jogo baseado no ID"""
        jogo1 = Jogo(id=1, titulo="The Witcher 3", preco=99.99)
        jogo2 = Jogo(id=1, titulo="The Witcher 3: Wild Hunt", preco=49.99)

        # Mesmo ID, consideram-se iguais
        assert jogo1 == jogo2

    def test_comparacao_desigualdade_por_id(self):
        """Teste de desigualdade entre objetos Jogo com IDs diferentes"""
        jogo1 = Jogo(id=1, titulo="The Witcher 3", preco=99.99)
        jogo2 = Jogo(id=2, titulo="The Witcher 3", preco=99.99)

        # IDs diferentes, não são iguais
        assert jogo1 != jogo2

    def test_comparacao_com_objeto_diferente(self):
        """Teste de comparação com objeto de tipo diferente"""
        jogo = Jogo(id=1, titulo="The Witcher 3")
        outro_objeto = "Não sou um jogo"

        assert jogo != outro_objeto

    def test_representacao_em_string(self):
        """Teste da representação em string do objeto"""
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99, status="ativo")
        representacao = repr(jogo)

        assert "Jogo" in representacao
        assert "1" in representacao
        assert "The Witcher 3" in representacao
        assert "99.99" in representacao
        assert "ativo" in representacao

    def test_modificar_preco_jogo(self):
        """Teste de modificação do preço após criação"""
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        jogo.preco = 49.99

        assert jogo.preco == 49.99

    def test_modificar_status_jogo(self):
        """Teste de modificação do status após criação"""
        jogo = Jogo(id=1, titulo="The Witcher 3", status="ativo")

        jogo.status = "inativo"

        assert jogo.status == "inativo"

    def test_preco_limite_minimo(self):
        """Teste de valor limite mínimo para preço"""
        jogo = Jogo(id=1, titulo="Free Game", preco=0.0)

        assert jogo.preco == 0.0

    def test_preco_limite_maximo(self):
        """Teste de valor limite máximo para preço"""
        jogo = Jogo(id=1, titulo="Premium Game", preco=9999.99)

        assert jogo.preco == 9999.99

    def test_status_valores_validos(self):
        """Teste de valores válidos para status"""
        status_validos = ["ativo", "inativo", "em_manutencao", "descontinuado"]

        for status in status_validos:
            jogo = Jogo(id=1, titulo="Game", status=status)
            assert jogo.status == status

    def test_titulo_com_caracteres_especiais(self):
        """Teste de título com caracteres especiais"""
        titulo = "Call of Duty®: Black Ops 7™"
        jogo = Jogo(id=1, titulo=titulo)

        assert jogo.titulo == titulo

    def test_descricao_longa(self):
        """Teste com descrição longa"""
        descricao = "A" * 500  # Descrição com 500 caracteres
        jogo = Jogo(id=1, titulo="Game", descricao=descricao)

        assert jogo.descricao == descricao
        assert len(jogo.descricao) == 500
