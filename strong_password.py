from random import choices
import string
from datetime import datetime
from os import system


class Elements():
    # elementos con probabilidad 1, que puede ser elegido
    # al azar por random.choices()
    def __init__(self, elements = []) -> None:
        self.elements = list(elements)
        self.quantity = len(elements)
        self.weight = [1] * self.quantity
    
    def change_weight(self, list, new_weight):
        # cambia la probabilidad de todos los elementos en list
        for item in list:
            index = self.elements.index(item)
            self.weight[index] = new_weight
        
    def reset_wight(self):
        # reinicia las probabilidades de todos los elementos
        self.weight = [1] * self.quantity
    
    def get_elements(self):
        return self.elements
    
    def get_weight(self):
        return self.weight


class Letters(Elements):
    def __init__(self) -> None:
        super().__init__(string.ascii_letters)
    

class Symbols(Elements):
    def __init__(self) -> None:
        super().__init__("!?$%_.@#")


if __name__ == "__main__":

    NUMBER_OF_CARACTERS = 16
    letters = Letters()
    symbols = Symbols()

    if NUMBER_OF_CARACTERS < 8:
        print("Secure password must have 8 characters or longer")

    password = ""
    for i in range(NUMBER_OF_CARACTERS - 4):
        element = choices(letters.get_elements()+
                          symbols.get_elements(),
                          letters.get_weight()+
                          symbols.get_weight(),
                          k=1)
        password += element[0]

        letters.reset_wight()
        symbols.reset_wight()

        if element[0] in "!?$%_.@#":
            symbols.change_weight("!?$%_.@#", 0.2)
        elif element[0].isupper():
            letters.change_weight(string.ascii_uppercase, 0.2)
        elif element[0].islower():
            letters.change_weight(string.ascii_lowercase, 0.2)
    
    password += datetime.now().strftime("%m%y")
            

    system("cls")
    print("Password Generator simplifica la creación de contraseñas seguras, garantizando la integridad de sus cuentas digitales.\nReduce la responsabilidad del usuario al generar contraseñas robustas con algoritmos avanzados, asegurando la resistencia contra ataques.\nOptimice la seguridad de sus cuentas sin complicaciones con Password Generator.\n")
    input("Presione la tecla Enter para generar una contraseña -> ")
    system("cls")
    print("Por favor, recuerde guardar su nueva contraseña de manera segura.\nUtilice un gestor de contraseñas o un lugar seguro.\nEl resguardo de la contraseña es esencial para proteger sus cuentas.\n")
    print(password + "\n")
