import pytest
from unittest.mock import MagicMock
from src.services.BibliotecaService import BibliotecaService
from src.services.CadastroService import CadastroService
@pytest.fixture
def mock_repositorio():
    return MagicMock()

@pytest.fixture
def biblioteca_service(mock_repositorio):
    return BibliotecaService(repositorio=mock_repositorio)

@pytest.fixture
def cadastro_service(mock_repositorio):
    return CadastroService(repositorio=mock_repositorio)