class Filme:
    def __init__(self, nome, ano, plataforma, generos):
        self.nome = nome
        self.ano = ano
        self.plataforma = plataforma
        self.generos = generos

    def __str__(self):
        return f'{self.nome} ({self.ano}) - {self.plataforma} - Gêneros: {", ".join(self.generos)}'

    def to_dict(self):
        return {
            'nome': self.nome,
            'ano': self.ano,
            'plataforma': self.plataforma,
            'generos': self.generos
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['nome'], data['ano'], data['plataforma'], data['generos'])
    