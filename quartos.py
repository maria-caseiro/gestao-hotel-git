class Quarto:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.disponivel = True

    def listagem_quartos(self):
        for q in self.quartos:
            print(f"-------- LISTA DE QUARTOS --------\nNúmero: {q.numero}\nTipo: {q.tipo}")
    
quarto1 = Quarto(1, "Individual")
quarto2 = Quarto(2, "Duplo")
quarto3 = Quarto(3, "Casal")