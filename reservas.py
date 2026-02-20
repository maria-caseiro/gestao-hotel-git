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
        quarto.disponivel = False
        return nova_reserva
    
    def cancelar_reserva(self, cliente_nome, numero_quarto):
        print("\n------- CANCELAMENTO DE RESERVAS -------")
        for reserva in self.reservas:
            if reserva.cliente.nome == cliente_nome and reserva.quarto.numero == numero_quarto:
                reserva.quarto.disponivel = True
                self.reservas.remove(reserva)
                print(f"\nReserva cancelada: {cliente_nome} (Quarto {numero_quarto}).")
                return True
        print("\nErro: Reserva não encontrada.")
        return False

    def ver_reservas(self):
        print("\n-------- LISTAGEM DE RESERVAS --------")
        if not self.reservas:
            print("\nNenhuma reserva encontrada.")
            return
        for reserva in self.reservas:
            print(f"\nCliente: {reserva.cliente.nome}\nQuarto: {reserva.quarto.numero}\nCheck-in: {reserva.check_in}\nCheck-out: {reserva.check_out}")