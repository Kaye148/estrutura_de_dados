import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class All:
    nome:str
    email:str
    endereco:str

    def mostar_dados(self):
        print(f"Nome:{self.nome}")
        print(f"E-Mail:{self.email}")

    def marketing (self):
        print(f"Nome:{self.nome}")
        print(f"Endereço:{self.endereco}")

print("===Entrada de Dados===")

cliente1=All(nome=input("informe seu nome: "),
                email=(input("informe seu E-mail: ")),
                endereco=(input("informe seu Endereço: ")))

cliente2=All(nome=input("informe seu nome: "),
                email=(input("informe seu E-mail: ")),
                endereco=(input("informe seu Endereço: ")))



print("===Exibeindo dados===")

cliente1.mostar_dados()
cliente1.marketing()
cliente2.mostar_dados()
cliente2.marketing()