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
        print(f"Endereço:{self.endereco}")

    def marketing (self):
        print(f"Nome:{self.nome}")
        print(f"E-Mail:{self.email}")
        print(f"Endereço:{self.endereco}")

    def mostra_nome(self):
        print(f"Nome:{self.nome}")

print("===Entrada de Dados===")

cliente1=All(nome=input("informe seu nome: "),
                email=(input("informe seu E-mail: ")),
                endereco=(input("informe seu Endereço: ")))
print("==============================================")
cliente2=All(nome=(input("informe seu Nome: ")),
            email=(input("informe seu E-mail: ")),
            endereco=(input("informe seu Endereço: ")))

print("===Exibeindo dados===")

cliente1.mostar_dados()
cliente1.marketing()
cliente1.mostra_nome()
print("===============")
cliente2.mostar_dados()
cliente2.marketing()
cliente2.mostra_nome
