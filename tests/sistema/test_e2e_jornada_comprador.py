import pytest
from src.models.Usuario import Usuario
from src.models.Jogo import Jogo

class TestSistemaE2E:
    """
    Teste de Sistema (End-to-End)
    Simula a jornada completa de um utilizador:
    Registo -> Login -> Pesquisa -> Carrinho -> Compra -> Biblioteca -> Download
    """

    def test_jornada_completa_compra_jogo(
        self, 
        integ_cadastro_service, 
        integ_catalogo_service, 
        integ_biblioteca_service,
        carrinho_service,
        db_memory
    ):

        novo_usuario = Usuario(id=None, nome="GamerPro", email="gamer@sapo.pt", senha="secure_pass")
        
        resp_registo = integ_cadastro_service.criar_conta(novo_usuario)
        assert resp_registo["sucesso"] is True
        
        usuario_login = Usuario(id=None, nome="", email="gamer@sapo.pt", senha="secure_pass")
        resp_login = integ_cadastro_service.fazer_login(usuario_login)
        assert resp_login["sucesso"] is True
        
        usuario_logado = db_memory.buscar_usuario_por_email("gamer@sapo.pt")
        assert usuario_logado is not None

        termo_pesquisa = "Street Fighter"
        resp_busca = integ_catalogo_service.buscar_jogo_por_termo(termo_pesquisa)
        
        assert resp_busca["sucesso"] is True
        assert len(resp_busca["jogos"]) >= 1
        
        jogo_escolhido = resp_busca["jogos"][0]
        assert jogo_escolhido.titulo == "Street Fighter 6"

        carrinho_service.adicionar_jogo(jogo_escolhido)
        
        assert len(carrinho_service.listar_jogos()) == 1
        assert carrinho_service.calcular_total() == 250.00
        
        itens_para_comprar = carrinho_service.listar_jogos()
        assert len(itens_para_comprar) > 0
        
        for jogo in itens_para_comprar:
            sucesso_compra = db_memory.registrar_compra(usuario_logado.id, jogo)
            assert sucesso_compra is True
            
        for jogo in list(itens_para_comprar):
            carrinho_service.remover_jogo(jogo)
            
        assert carrinho_service.calcular_total() == 0.0
        
        resp_download = integ_biblioteca_service.iniciar_download(usuario_logado, jogo_escolhido)
        
        assert resp_download["sucesso"] is True
        assert "Iniciando download" in resp_download["mensagem"]
        assert f"de {jogo_escolhido.titulo}" in resp_download["mensagem"]

        compra_registada = db_memory.buscar_compra_por_usuario(usuario_logado.id, jogo_escolhido.id)
        assert compra_registada["status"] == "COMPRADO"
        