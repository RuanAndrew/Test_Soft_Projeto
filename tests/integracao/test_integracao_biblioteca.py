import pytest
from src.models.usuario import Usuario
from src.models.Jogo import Jogo
from src.services.BibliotecaService import BibliotecaService

class TestIntegracaoBiblioteca:

    def test_fluxo_real_compra_e_download(self, integ_biblioteca_service, db_memory):

        usuario = db_memory.buscar_usuario_por_email("teste@email.com")
        jogo_existente = Jogo(id=1, titulo="The Witcher 3")
        jogo_novo = Jogo(id=4, titulo="Street Fighter 6")

        resultado = integ_biblioteca_service.iniciar_download(usuario, jogo_existente)
        assert resultado["sucesso"] is True
        assert "Iniciando download" in resultado["mensagem"]

        compra = db_memory.buscar_compra_por_usuario(usuario.id, jogo_existente.id)
        assert compra["status"] == "COMPRADO"

    def test_validacao_jogo_nao_comprado(self, integ_biblioteca_service, db_memory):
        usuario = db_memory.buscar_usuario_por_email("teste@email.com")
        jogo_nao_comprado = Jogo(id=4, titulo="Street Fighter 6")

        resultado = integ_biblioteca_service.buscar_jogo(usuario, jogo_nao_comprado)

        assert resultado["sucesso"] is False
        assert "Parece que este jogo ainda não é seu" in resultado["mensagem"]

    def test_ciclo_completo_instalacao_desinstalacao(self, integ_biblioteca_service, db_memory):
        """
        Cenário: Jogo comprado -> Instalar -> Verificar Status -> Desinstalar -> Verificar Status
        """
        usuario = db_memory.buscar_usuario_por_email("teste@email.com")
        jogo = db_memory.buscar_jogo_por_id(1)
        
        db_memory.atualizar_status(usuario.id, jogo.id, "INSTALADO")
        
        compra = db_memory.buscar_compra_por_usuario(usuario.id, jogo.id)
        assert compra["status"] == "INSTALADO"
        
        resultado = integ_biblioteca_service.desinstalar_jogo(usuario, jogo)
        
        assert resultado["sucesso"] is True
        assert resultado["status_atual"] == "NAO_INSTALADO"
        
        compra_pos = db_memory.buscar_compra_por_usuario(usuario.id, jogo.id)
        assert compra_pos["status"] == "NAO_INSTALADO"
