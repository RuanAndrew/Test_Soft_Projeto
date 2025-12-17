class TestCatalogoIntegracao:

    def test_busca_real_encontrada(self, integ_catalogo_service):
        """
        Cenário: Buscar 'Witcher' no banco populado.
        Valida: Se o filtro do RepositorioMemoria retorna o objeto correto.
        """
        resultado = integ_catalogo_service.buscar_jogo_por_termo("witcher")
        
        assert resultado["sucesso"] is True
        assert len(resultado["jogos"]) == 1
        assert resultado["jogos"][0].titulo == "The Witcher 3"
        assert resultado["jogos"][0].preco == 99.99

    def test_busca_real_nenhum_resultado(self, integ_catalogo_service):
        """
        Cenário: Buscar jogo inexistente.
        """
        resultado = integ_catalogo_service.buscar_jogo_por_termo("Mario Kart")
        
        assert resultado["sucesso"] is True
        assert len(resultado["jogos"]) == 0
        assert "Nenhum jogo encontrado" in resultado["mensagem"]

    def test_listar_todos_exibe_somente_ativos(self, integ_catalogo_service):
        resultado = integ_catalogo_service.listar_todos()

        assert resultado["sucesso"] is True
        titulos = [j.titulo for j in resultado["jogos"]]

        assert "The Witcher 3" in titulos
        assert "Grand Theft Auto VI" not in titulos