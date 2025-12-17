class Usuario:
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.biblioteca = []
    
    def __repr__(self):
        return f"Usuario(id={self.id}, nome='{self.nome}', email='{self.email}')"