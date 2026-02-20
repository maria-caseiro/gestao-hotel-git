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