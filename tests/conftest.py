import pytest
from unittest.mock import MagicMock
from src.services.BibliotecaService import BibliotecaService
from src.services.CadastroService import CadastroService
from src.services.CatalogoService import CatalogoService
from src.services.CarrinhoService import CarrinhoService
from src.repository.RepositorioMemoria import RepositorioMemoria
from src.models.Jogo import Jogo
from src.models.Catalogo import Catalogo

@pytest.fixture
def mock_repository():
    return MagicMock()

@pytest.fixture
def unit_biblioteca_service(mock_repository):
    return BibliotecaService(repositorio=mock_repository)

@pytest.fixture
def unit_cadastro_service(mock_repository):
    return CadastroService(repositorio=mock_repository)

@pytest.fixture
def unit_catalogo_service(mock_repository):
    service = CatalogoService(repositorio=mock_repository)
    mock_repository.buscar_jogos_por_termo.return_value = [
        Jogo(id=1, titulo="The Witcher 3", preco=99.99)
    ]
    return service

@pytest.fixture
def db_memory():
    return RepositorioMemoria()

@pytest.fixture
def integ_biblioteca_service(db_memory):
    return BibliotecaService(repositorio=db_memory)

@pytest.fixture
def integ_cadastro_service(db_memory):
    return CadastroService(repositorio=db_memory)

@pytest.fixture
def integ_catalogo_service(db_memory):
    return CatalogoService(repositorio=db_memory)

@pytest.fixture
def carrinho_service():
    return CarrinhoService()

@pytest.fixture
def catalogo_com_jogos():
    catalogo = Catalogo()
    catalogo.adicionar_jogo(Jogo(id=1, titulo="The Witcher 3"))
    return catalogo