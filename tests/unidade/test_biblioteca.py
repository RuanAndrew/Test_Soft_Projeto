import pytest
from unittest.mock import MagicMock

class TestBiblioteca:

    def test_visualizar_jogo_comprado(self, unit_biblioteca_service, mock_repository):
        """Caso de teste: TC-LIB-001"""
        
        mock_repository.buscar_compra_por_usuario.return_value = {
            "jogo_id": 101, 
            "status": "COMPRADO"
        }
        
        mock_usuario = MagicMock()
        mock_usuario.id = 1
        
        mock_jogo = MagicMock()
        mock_jogo.id = 101

        resultado = unit_biblioteca_service.buscar_jogo(usuario=mock_usuario, jogo=mock_jogo)

        assert resultado["sucesso"] is True
        assert resultado["download_disponivel"] is True 

    def test_baixar_jogo_comprado_com_sucesso(self, unit_biblioteca_service, mock_repository):
        """Caso de teste: TC-LIB-002"""

        mock_repository.verificar_posse.return_value = True

        mock_usuario = MagicMock()
        mock_usuario.id = 1
        mock_jogo = MagicMock()
        mock_jogo.titulo = "Cyberpunk 2077"

        resultado = unit_biblioteca_service.iniciar_download(usuario=mock_usuario, jogo=mock_jogo)

        assert resultado["sucesso"] is True
        assert "Iniciando download" in resultado["mensagem"]
        
        mock_repository.verificar_posse.assert_called_once()

    def test_buscar_jogo_nao_adquirido(self, unit_biblioteca_service, mock_repository):
        """Caso de teste: TC-LIB-003"""
        mock_repository.buscar_compra_por_usuario.return_value = None

        mock_usuario = MagicMock()
        mock_usuario.id = 1
        
        mock_jogo = MagicMock()
        mock_jogo.id = 1
        mock_jogo.titulo = "Street Fighter"

        resultado = unit_biblioteca_service.buscar_jogo(usuario=mock_usuario, jogo=mock_jogo)

        assert resultado["sucesso"] is False
        
        mensagem_esperada = f"Parece que este jogo ainda não é seu! Adquira {mock_jogo.titulo} na loja."
        assert mensagem_esperada in resultado["mensagem"]

    def test_desinstalar_jogo_com_sucesso(self, unit_biblioteca_service, mock_repository):
        """Caso de teste: TC-LIB-004"""

        mock_usuario = MagicMock()
        mock_usuario.id = 1
        
        mock_jogo = MagicMock()
        mock_jogo.id = 1
        mock_jogo.titulo = "Street Fighter"

        mock_repository.obter_status_jogo.return_value = "INSTALADO"

        resultado = unit_biblioteca_service.desinstalar_jogo(usuario=mock_usuario, jogo=mock_jogo)

        assert resultado["sucesso"] is True
        
        assert "O jogo foi desinstalado com sucesso" in resultado["mensagem"]

        mock_repository.atualizar_status.assert_called_once_with(
            mock_usuario.id, 
            mock_jogo.id, 
            "NAO_INSTALADO"
        )