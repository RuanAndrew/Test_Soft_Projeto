from src.models.Usuario import Usuario
from src.models.Jogo import Jogo

class RepositorioMemoria:
    def __init__(self):
        self._usuarios = []
        self._jogos = []
        self._biblioteca = []

        self._semear_dados()

    def _semear_dados(self):

        self._jogos.append(Jogo(1, "The Witcher 3", 99.99, "ativo"))
        self._jogos.append(Jogo(2, "Cyberpunk 2077", 199.90, "ativo"))
        self._jogos.append(Jogo(3, "Hollow Knight", 46.99, "ativo"))
        self._jogos.append(Jogo(4, "Street Fighter 6", 250.00, "ativo"))
        self._jogos.append(Jogo(5, "Grand Theft Auto VI", 0, "inativo"))
        self._jogos.append(Jogo(6, "Minecraft", 29.90, "ativo"))
        self._jogos.append(Jogo(7, "Elden Ring", 229.90, "ativo"))
        self._jogos.append(Jogo(8, "Vampire Survivors", 0.00, "ativo"))
        self._jogos.append(Jogo(9, "Baldur's Gate 3", 199.90, "ativo"))
        self._jogos.append(Jogo(10, "Half-Life 3", 0, "inativo"))

        self._usuarios.append(Usuario(id=1, nome="Tester", email="teste@email.com", senha="123"))
        
        self._usuarios.append(Usuario(id=2, nome="Rodrigo Rico", email="rico@email.com", senha="123"))
        
        self._usuarios.append(Usuario(id=3, nome="Camila", email="camila@email.com", senha="abc"))
        
        self._usuarios.append(Usuario(id=4, nome="Noob", email="noob@email.com", senha="123"))

        self._biblioteca.append({
            "usuario_id": 1,
            "jogo_id": 1,
            "titulo_jogo": "The Witcher 3",
            "status": "COMPRADO"
        })
        self._biblioteca.append({
            "usuario_id": 1,
            "jogo_id": 8,
            "titulo_jogo": "Vampire Survivors",
            "status": "COMPRADO"
        })

        self._biblioteca.append({
            "usuario_id": 2,
            "jogo_id": 2,
            "titulo_jogo": "Cyberpunk 2077",
            "status": "COMPRADO"
        })
        self._biblioteca.append({
            "usuario_id": 2,
            "jogo_id": 4,
            "titulo_jogo": "Street Fighter 6",
            "status": "COMPRADO"
        })
        self._biblioteca.append({
            "usuario_id": 2,
            "jogo_id": 7,
            "titulo_jogo": "Elden Ring",
            "status": "COMPRADO"
        })
        self._biblioteca.append({
            "usuario_id": 2,
            "jogo_id": 9,
            "titulo_jogo": "Baldur's Gate 3",
            "status": "COMPRADO"
        })

        self._biblioteca.append({
            "usuario_id": 3,
            "jogo_id": 3,
            "titulo_jogo": "Hollow Knight",
            "status": "COMPRADO"
        })
        self._biblioteca.append({
            "usuario_id": 3,
            "jogo_id": 6,
            "titulo_jogo": "Minecraft",
            "status": "COMPRADO"
        })

    def buscar_usuario_por_email(self, email):
        for usuario in self._usuarios:
            if usuario.email == email:
                return usuario
        return None

    def salvar_usuario(self, usuario):
        usuario.id = len(self._usuarios) + 1
        self._usuarios.append(usuario)
        return usuario
    
    def atualizar_usuario(self, usuario_atualizado):
        for i, usuario in enumerate(self._usuarios):
            if usuario.id == usuario_atualizado.id:
                self._usuarios[i] = usuario_atualizado
                return True
        return False

    def buscar_jogos_por_termo(self, termo):
        resultado = []
        for jogo in self._jogos:
            if termo in jogo.titulo:
                resultado.append(jogo)
        return resultado
    
    def listar_todos_jogos(self):
        return self._jogos

    def buscar_jogo_por_id(self, jogo_id):
        for jogo in self._jogos:
            if jogo.id == jogo_id:
                return jogo
        return None

    def buscar_compra_por_usuario(self, usuario_id, jogo_id):
        for registro in self._biblioteca:
            if registro["usuario_id"] == usuario_id and registro["jogo_id"] == jogo_id:
                return registro
        return None

    def verificar_posse(self, usuario_id, titulo_jogo):
        for registro in self._biblioteca:
            if registro["usuario_id"] == usuario_id and registro["titulo_jogo"] == titulo_jogo:
                return True
        return False

    def atualizar_status(self, usuario_id, jogo_id, novo_status):
        for registro in self._biblioteca:
            if registro["usuario_id"] == usuario_id and registro["jogo_id"] == jogo_id:
                registro["status"] = novo_status
                return True
        return False

    def registrar_compra(self, usuario_id, jogo):
        novo_registro = {
            "usuario_id": usuario_id,
            "jogo_id": jogo.id,
            "titulo_jogo": jogo.titulo,
            "status": "COMPRADO"
        }
        self._biblioteca.append(novo_registro)
        return True