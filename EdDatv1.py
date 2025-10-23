import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email:str
    telefone:str
    endereco:str

    def mostar_dadaos(self):
        print(f"Nome:{cliente1.nome}")
        print(f"E-mail:{cliente1.email}")
        print(f"Telefone:{cliente1.telefone}")
        print(f"Endereço:{cliente1.endereco}")

print("===Solicitendo Dados===")
cliente1 = Cliente(nome=(input("informe seu nome: ")),
                   email=(input("informe seu E-mail: ")),
                   telefone=(input("informe seu número de telefone: "))
                   ,endereco=(input("informe seu endereço: "))
                   )

print("\n==Exibindo Dados==")
cliente1.mostar_dadaos

print(f"Nome:{cliente1.nome}\nE-mail:{cliente1.email}\nTelefone:{cliente1.telefone}\nEndereço:{cliente1.endereco}")