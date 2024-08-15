
import json
import random
import os
from filme import Filme
from genero import Genero
from plataforma import Plataforma
from usuario import Usuario

class Sistema:
    def __init__(self):
        self.filmes = []
        self.generos = []
        self.plataformas = []
        self.usuario = Usuario('Usuário Padrão')

        self.data_dir = 'dados'
        os.makedirs(self.data_dir, exist_ok=True)

        self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(os.path.join(self.data_dir, 'filmes.json'), 'r') as f:
                filmes_data = json.load(f)
                self.filmes = [Filme.from_dict(filme) for filme in filmes_data]
        except FileNotFoundError:
            pass

        try:
            with open(os.path.join(self.data_dir, 'generos.json'), 'r') as f:
                generos_data = json.load(f)
                self.generos = [Genero.from_dict(genero) for genero in generos_data]
        except FileNotFoundError:
            pass

        try:
            with open(os.path.join(self.data_dir, 'plataformas.json'), 'r') as f:
                plataformas_data = json.load(f)
                self.plataformas = [Plataforma.from_dict(plataforma) for plataforma in plataformas_data]
        except FileNotFoundError:
            pass

        try:
            with open(os.path.join(self.data_dir, 'usuario.json'), 'r') as f:
                usuario_data = json.load(f)
                self.usuario = Usuario.from_dict(usuario_data)
        except FileNotFoundError:
            pass

    def salvar_dados(self):
        print("Salvando dados...")  # Debugging
        with open(os.path.join(self.data_dir, 'filmes.json'), 'w') as f:
            json.dump([filme.to_dict() for filme in self.filmes], f, indent=4)
        with open(os.path.join(self.data_dir, 'generos.json'), 'w') as f:
            json.dump([genero.to_dict() for genero in self.generos], f, indent=4)
        with open(os.path.join(self.data_dir, 'plataformas.json'), 'w') as f:
            json.dump([plataforma.to_dict() for plataforma in self.plataformas], f, indent=4)
        with open(os.path.join(self.data_dir, 'usuario.json'), 'w') as f:
            json.dump(self.usuario.to_dict(), f, indent=4)
        print("Dados salvos com sucesso.")  # Debugging

    def cadastrar_filme(self, nome, ano, plataforma_nome, generos_nomes):
        plataforma = next((p for p in self.plataformas if p.nome == plataforma_nome), None)
        if not plataforma:
            print(f"Plataforma '{plataforma_nome}' não encontrada.")
            return
        
        generos = [g for g in self.generos if g.nome in generos_nomes]
        if not generos:
            print(f"Gêneros inválidos: {', '.join(generos_nomes)}")
            return

        filme = Filme(nome, ano, plataforma.nome, [g.nome for g in generos])
        self.filmes.append(filme)
        print(f"Filme {filme.nome} adicionado. Total de filmes: {len(self.filmes)}")  # Debugging
        self.salvar_dados()
        print("Filme cadastrado com sucesso!")

    def cadastrar_genero(self, id, nome):
        if any(g.id == id for g in self.generos):
            print(f"Gênero com identificador '{id}' já cadastrado.")
            return
        genero = Genero(id, nome)
        self.generos.append(genero)
        self.salvar_dados()
        print("Gênero cadastrado com sucesso!")

    def cadastrar_plataforma(self, id, nome):
        if any(p.id == id for p in self.plataformas):
            print(f"Plataforma com identificador '{id}' já cadastrada.")
            return
        plataforma = Plataforma(id, nome)
        self.plataformas.append(plataforma)
        self.salvar_dados()
        print("Plataforma cadastrada com sucesso!")

    def listar_filmes(self):
        return self.filmes

    def listar_generos(self):
        return self.generos

    def listar_plataformas(self):
        return self.plataformas

    def cadastrar_genero_preferido(self, genero):
        if genero in [g.nome for g in self.generos]:
            self.usuario.adicionar_genero_preferido(genero)
            self.salvar_dados()
            print("Gênero preferido cadastrado com sucesso!")
        else:
            print(f"Gênero '{genero}' não encontrado.")

    def recomendar_filme(self):
        filmes_preferidos = [filme for filme in self.filmes if any(genero in self.usuario.generos_preferidos for genero in filme.generos)]
        if filmes_preferidos:
            return random.choice(filmes_preferidos)
        return None

