import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Endereco:
    numero:str
    cidade:str
    logradura:str

lista_de_endereco = []

@dataclass
class Cliente:
    nome: str
    email: str
    endereco: Endereco

    def mostrar_dados(self):
        print(f"Nome:{self.nome}")
        print(f"E-mail{self.email}")
        print(f"Logradouro:{self.endereco.logradura}")
        print(f"Númeoro:{self.endereco.numero}")
        print(f"Cidade:{self.endereco.cidade}")

cliente1 = Cliente(nome=input("digite seu nome: "), 
                   email=input("digite seu E-mail: "),
                    endereco=Endereco(logradura=input("informe sua logradura:",
                    "\nNúmero da casa: ","\nCidade:")))
lista_de_endereco.append(cliente1, Endereco)

cliente1.mostrar_dados()


