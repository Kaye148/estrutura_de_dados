import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: str
    altura: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso {self.peso}")
        print(f"Altura: {self.altura}")

lista_pessoas = []

for i in range(4):
    dados_pessoa = Pessoa(nome=input("digite seu nome: ", 
                    idade=input("digite sua idade",
                    peso=input("digite seu peso: ",
                    altura=input("digite sua altura: ")))))
    lista_pessoas.append(dados_pessoa)
    
for Pessoa in lista_pessoas:
    Pessoa.mostrar_dados()