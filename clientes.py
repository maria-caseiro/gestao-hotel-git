class Cliente:
    clientes = []
    def __init__(self, nome, nif, email, contacto):
        self.nome = nome
        self.nif = nif
        self.email = email
        self.contacto = contacto
        Cliente.clientes.append(self)
    
    @classmethod
    def listagem_clientes(cls):
        print("\n-------- LISTAGEM DE CLIENTES --------")
        for c in cls.clientes:
            print(f"\nNome: {c.nome}\nNIF: {c.nif}\nEmail: {c.email}\nContacto: {c.contacto}")
        print("\n--------------------------------------")
    
cliente1 = Cliente("Maria", 111111111, "maria@email.com", "911 111 111")
cliente2 = Cliente("Guilherme", 222222222, "guilherme@email.com", "912 222 222")
cliente3 = Cliente("Afonso", 333333333, "afonso@email.com", "913 333 333")