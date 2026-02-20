class Reserva:
    def __init__(self, cliente, quarto, check_in, check_out):
        self.cliente = cliente
        self.quarto = quarto
        self.check_in = check_in
        self.check_out = check_out

class Gestor:
    def __init__(self):
        self.reservas = []

    def criar_reserva(self, cliente, quarto, check_in, check_out):
        nova_reserva = Reserva(cliente, quarto, check_in, check_out)
        self.reservas.append(nova_reserva)
        return nova_reserva

    def ver_reservas(self):
        if not self.reservas:
            print("Nenhuma reserva encontrada.")
            return
        for reserva in self.reservas:
            print(f"-------- LISTA DE RESERVAS -------- \nCliente: {reserva.cliente}\nQuarto: {reserva.quarto}\nCheck-in: {reserva.check_in}\nCheck-out: {reserva.check_out}")