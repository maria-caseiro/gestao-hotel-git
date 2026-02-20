class Quarto:
    quartos = []
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.disponivel = True
        Quarto.quartos.append(self)

    def __str__(self):
        estado = "Disponível" if self.disponivel else "Reservado"
        return f"Quarto {self.numero} ({self.tipo}) - {estado}"

    @classmethod
    def listagem_quartos(cls):
        print("\n-------- LISTAGEM DE QUARTOS --------")
        for q in cls.quartos:
            estado = "Disponível" if q.disponivel else "Reservado"
            print(f"\nNúmero: {q.numero}\nTipo: {q.tipo}\nEstado: {estado}")