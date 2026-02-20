class Quarto:
    quartos = []
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.disponivel = True
        Quarto.quartos.append(self)

    @classmethod
    def listagem_quartos(cls):
        print("\n-------- LISTAGEM DE QUARTOS --------")
        for q in cls.quartos:
            print(f"\nNúmero: {q.numero}\nTipo: {q.tipo}")