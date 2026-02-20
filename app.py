from clientes import Cliente
from quartos import Quarto
from reservas import Gestor

c1 = Cliente("Maria", 111111111, "maria@email.com", "911 111 111")
c2 = Cliente("Guilherme", 222222222, "guilherme@email.com", "912 222 222")
c3 = Cliente("Afonso", 333333333, "afonso@email.com", "913 333 333")

q1 = Quarto(1, "Individual")
q2 = Quarto(2, "Duplo")
q3 = Quarto(3, "Casal")

hotel = Gestor()
hotel.ver_reservas()
Cliente.listagem_clientes()
Quarto.listagem_quartos()

hotel.criar_reserva(c1, q1, "27/02/2026", "03/03/2026")
hotel.ver_reservas()
Quarto.listagem_quartos()

hotel.cancelar_reserva("Maria", 1)
Quarto.listagem_quartos()