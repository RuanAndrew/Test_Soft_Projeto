import pytest
from unittest.mock import MagicMock
from src.services.BibliotecaService import BibliotecaService

class TestBiblioteca:

    @pytest.fixture
    def mock_repositorio(self):
        return MagicMock()

    @pytest.fixture
    def service(self, mock_repositorio):
        return BibliotecaService(repositorio=mock_repositorio)

    def test_visualizar_jogo_comprado(self, service, mock_repositorio):
        """Caso de teste: TC-LIB-001"""
        
        mock_repositorio.buscar_compra_por_usuario.return_value = {
            "jogo_id": 101, 
            "status": "COMPRADO"
        }
        
        mock_usuario = MagicMock()
        mock_usuario.id = 1
        mock_jogo = MagicMock()
        mock_jogo.id = 101

        resultado = service.buscar_jogo(usuario=mock_usuario, jogo=mock_jogo)

        assert resultado["sucesso"] is True
        assert resultado["download_disponivel"] is True 

    def test_baixar_jogo_comprado_com_sucesso(self, service, mock_repositorio):
        """Caso de teste: TC-LIB-002"""

        mock_repositorio.verificar_posse.return_value = True

        mock_usuario = MagicMock()
        mock_usuario.id = 1
        mock_jogo = MagicMock()
        mock_jogo.titulo = "Cyberpunk 2077"

        resultado = service.iniciar_download(usuario=mock_usuario, jogo=mock_jogo)

        assert resultado["sucesso"] is True
        assert "Iniciando download" in resultado["mensagem"]
        
        mock_repositorio.verificar_posse.assert_called_once()