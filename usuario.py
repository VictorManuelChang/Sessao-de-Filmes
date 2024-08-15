class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.generos_preferidos = []

    def adicionar_genero_preferido(self, genero):
        if genero not in self.generos_preferidos:
            self.generos_preferidos.append(genero)

    def __str__(self):
        return f'Usuário: {self.nome} - Gêneros Preferidos: {", ".join(self.generos_preferidos)}'

    def to_dict(self):
        return {
            'nome': self.nome,
            'generos_preferidos': self.generos_preferidos
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data['nome'])
        user.generos_preferidos = data['generos_preferidos']
        return user
