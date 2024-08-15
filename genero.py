class Genero:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f'{self.id} - {self.nome}'

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['nome'])
