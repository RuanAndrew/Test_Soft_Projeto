import pytest
from unittest.mock import MagicMock
from src.services.BibliotecaService import BibliotecaService
from src.services.CadastroService import CadastroService
from src.services.CatalogoService import CatalogoService
from src.services.CarrinhoService import CarrinhoService
from src.models.Jogo import Jogo
from src.models.Catalogo import Catalogo

@pytest.fixture
def mock_repositorio():
    return MagicMock()

@pytest.fixture
def biblioteca_service(mock_repositorio):
    return BibliotecaService(repositorio=mock_repositorio)

@pytest.fixture
def cadastro_service(mock_repositorio):
    return CadastroService(repositorio=mock_repositorio)

@pytest.fixture
def catalogo_service(mock_repositorio):
    """Fixture que retorna um CatalogoService com jogos mockados"""
    service = CatalogoService(repositorio=mock_repositorio)
    
    # Mock do repositório com um jogo para busca
    jogo_witcher = Jogo(id=1, titulo="The Witcher 3", preco=99.99, status="ativo")
    mock_repositorio.buscar_por_termo.return_value = [jogo_witcher]
    
    return service

@pytest.fixture
def carrinho_service():
    """Fixture que retorna um CarrinhoService limpo"""
    return CarrinhoService()

@pytest.fixture
def catalogo_com_jogos():
    """Fixture que retorna um catálogo com alguns jogos de exemplo"""
    catalogo = Catalogo()
    jogo1 = Jogo(id=1, titulo="The Witcher 3", preco=99.99, status="ativo")
    jogo2 = Jogo(id=2, titulo="Cyberpunk 2077", preco=199.90, status="ativo")
    jogo3 = Jogo(id=3, titulo="Elden Ring", preco=249.90, status="ativo")
    jogo4 = Jogo(id=4, titulo="Hollow Knight", preco=46.99, status="ativo")
    jogo5 = Jogo(id=5, titulo="Call of Duty: Black Ops 7", preco=349.90, status="ativo")
    
    catalogo.adicionar_jogo(jogo1)
    catalogo.adicionar_jogo(jogo2)
    catalogo.adicionar_jogo(jogo3)
    catalogo.adicionar_jogo(jogo4)
    catalogo.adicionar_jogo(jogo5)
    
    return catalogo