class Piramide():
    def __init__(self,tamanho=0):
        self.tamanho = tamanho
    

    def mostra_piramide(self):
        for x in range(self.tamanho):
            print(' '*(self.tamanho-x),'X '*(x+1))
    
    def separar(self):
        print('\n\n\n\n\n\n\n\n\n\n')
    

piramide_1 = Piramide(int(input('Tamanho da piramide:')))




print(f'Tamanho da piramide é : {piramide_1.tamanho} andares')
piramide_1.mostra_piramide()


