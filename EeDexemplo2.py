from dataclasses import dataclass

import os 
os.system("cls")

@dataclass
class All:
    nome:str
    email:str
    endereco:str

    def mostar_dados(self):
        print(f"Nome:{self.nome}")
        print(f"E-Mail:{self.email}")
        print(f"Endereço:{self.endereco}")

    def marketing (self):
        print(f"Nome:{self.nome}")
        print(f"E-Mail:{self.email}")
        print(f"Endereço:{self.endereco}")

    def mostra_nome(self):
        print(f"Nome:{self.nome}")

print("===Entrada de Dados===")
lista_pessoas = []

for i in range(2):
    cliente=All(nome=input("informe seu nome: "),
                    email=(input("informe seu E-mail: ")),
                    endereco=(input("informe seu Endereço: ")))
    lista_pessoas.append(cliente)


print("===Exibeindo dados===")
for clientes in lista_pessoas:
    cliente.mostar_dados()
    cliente.marketing()

for cliente in lista_pessoas:
    cliente.mostar_dados()
    cliente.marketing()

print("===somente nomes===")
for cliente in lista_pessoas:
    cliente.mostra_nome