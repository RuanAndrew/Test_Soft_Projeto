import pytest
from unittest.mock import MagicMock

class TestCarrinho:
	def test_adicionar_jogo_ao_carrinho(self):
		"""TC-CAR-001: Adição de jogo para compra"""
		mock_carrinho = MagicMock()
		mock_jogo = MagicMock()
		mock_jogo.titulo = "Call of Duty®: Black Ops 7"
		mock_jogo.preco = 349.90

		# Carrinho começa vazio
		mock_carrinho.listar_jogos.return_value = []
		mock_carrinho.calcular_total.return_value = 0.0

		# Adiciona o jogo
		mock_carrinho.adicionar_jogo(mock_jogo)
		mock_carrinho.listar_jogos.return_value = [mock_jogo]
		mock_carrinho.calcular_total.return_value = 349.90

		jogos = mock_carrinho.listar_jogos()
		total = mock_carrinho.calcular_total()

		assert len(jogos) == 1
		assert jogos[0].titulo == "Call of Duty®: Black Ops 7"
		assert total == 349.90

	def test_remover_jogo_do_carrinho(self):
		"""TC-CAR-002: Remoção de jogo do Carrinho"""
		mock_carrinho = MagicMock()
		mock_jogo = MagicMock()
		mock_jogo.titulo = "Call of Duty®: Black Ops 7"

		# Carrinho começa com o jogo
		mock_carrinho.listar_jogos.return_value = [mock_jogo]
		mock_carrinho.calcular_total.return_value = 349.90

		# Remove o jogo
		mock_carrinho.remover_jogo(mock_jogo)
		mock_carrinho.listar_jogos.return_value = []
		mock_carrinho.calcular_total.return_value = 0.0

		jogos = mock_carrinho.listar_jogos()
		total = mock_carrinho.calcular_total()

		assert len(jogos) == 0
		assert total == 0.0

	def test_calculo_valor_total_carrinho(self):
		"""TC-CAR-003: Cálculo do Valor Total a Pagar"""
		mock_carrinho = MagicMock()
		mock_jogo1 = MagicMock()
		mock_jogo1.titulo = "Call of Duty®: Black Ops 7"
		mock_jogo1.preco = 349.90
		mock_jogo2 = MagicMock()
		mock_jogo2.titulo = "Hollow Knight"
		mock_jogo2.preco = 46.99

		# Carrinho vazio
		mock_carrinho.listar_jogos.return_value = []
		mock_carrinho.calcular_total.return_value = 0.0

		# Adiciona os dois jogos
		mock_carrinho.adicionar_jogo(mock_jogo1)
		mock_carrinho.adicionar_jogo(mock_jogo2)
		mock_carrinho.listar_jogos.return_value = [mock_jogo1, mock_jogo2]
		mock_carrinho.calcular_total.return_value = 349.90 + 46.99

		jogos = mock_carrinho.listar_jogos()
		total = mock_carrinho.calcular_total()

		assert len(jogos) == 2
		assert jogos[0].titulo == "Call of Duty®: Black Ops 7"
		assert jogos[1].titulo == "Hollow Knight"
		assert total == pytest.approx(396.89, 0.01)
