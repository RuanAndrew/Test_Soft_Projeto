import pytest
from unittest.mock import MagicMock

class TestCatalogo:
    
    def test_busca_jogo_existente_ativo(self, unit_catalogo_service):
        """Caso de Teste: TC-CAT-001 - Busca de Jogo Existente e Ativo"""
        termo_busca = "The Witcher 3"
        
        resultado = unit_catalogo_service.buscar_jogo_por_termo(termo_busca)

        assert resultado["sucesso"] is True
        assert len(resultado["jogos"]) == 1
        jogo_encontrado = resultado["jogos"][0]
        
        assert jogo_encontrado.titulo == termo_busca
        assert jogo_encontrado.preco == 99.99
        assert jogo_encontrado.status == "ativo"
       
    def test_busca_por_termo_nao_encontrado(self, unit_catalogo_service, mock_repository):
        """Caso de Teste: TC-CAT-002 - Busca por Termo Não Encontrado"""
        termo_busca = "Mineirinho Ultra Adventures"
        
        mock_repository.buscar_jogos_por_termo.return_value = []
        
        resultado = unit_catalogo_service.buscar_jogo_por_termo(termo_busca)

        assert resultado["sucesso"] is True
        assert len(resultado["jogos"]) == 0

        mensagem_esperada = "Nenhum jogo encontrado para sua busca"
        assert mensagem_esperada in resultado["mensagem"]
        