import pytest
from unittest.mock import MagicMock

class TestCatalogo:
    
    def test_busca_jogo_existente_ativo(self, catalogo_service):
        """Caso de Teste: TC-CAT-001"""
        termo_busca = "The Witcher 3"
        
        resultado = catalogo_service.buscar_jogo_por_termo(termo_busca)

        assert resultado["sucesso"] is True
        assert len(resultado["jogos"]) == 1
        jogo_encontrado = resultado["jogos"][0]
        
        assert jogo_encontrado.titulo == termo_busca
        ## adicionar verificação para o preço
        assert jogo_encontrado.status == "ativo"
       

    def busca_por_termo_nao_encontrado(self, catalogo_service):
        """Caso de Teste: TC-CAT-002 """
        termo_busca = "Mineirinho Ultra Adventures"
        
        resultado = catalogo_service.buscar_jogo_por_termo(termo_busca)

        assert resultado["sucesso"] is True
        assert len(resultado["jogos"]) == 0

        mensagem_esperada = f"Nenhum jogo encontrado para sua busca"
        assert mensagem_esperada in resultado["mensagem"]
        