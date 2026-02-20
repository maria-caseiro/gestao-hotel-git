class Cliente:
    def __init__(self, nome, nif, email, contacto):
        self.nome = nome
        self.nif = nif
        self.email = email
        self.contacto = contacto

    def registar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def listagem_clientes(self):
        for c in self.clientes:
            print(f"-------- LISTA DE CLIENTES --------\nNome: {c.nome}\nNIF: {c.nif}\nEmail: {c.email}\nContacto: {c.contacto}")
    
cliente1 = Cliente("Maria", 111111111, "maria@email.com", "911 111 111")
cliente2 = Cliente("Guilherme", 222222222, "guilherme@email.com", "912 222 222")
cliente3 = Cliente("Afonso", 333333333, "afonso@email.com", "913 333 333")