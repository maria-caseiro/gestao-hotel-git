# Projeto de Avaliação: Gestor de Reservas de Hotel

## Descrição 
Criação de um aplicativo em Python para gerir reservas de um hotel, organizado com Git e GitHub.

### Funcionalidades
- Gestão de quartos (disponíveis/reservados)
- Registo e listagem de clientes
- Efetuar e cancelar reservas

## Funções principais

#### Cliente
- Criação de variável *clientes* com lista vazia
- Definição da classe através do construtor *__ init__* com os atributos *nome, nif, email, contacto*
- Adição automática de cada novo objeto da classe na lista da variável *clientes*
- Uso do decorador @classmethod para criar um método de classe: *listagem_clientes*
- A função *listagem_clientes* mostra todos os clientes registados

#### Quarto
- Criação de variável *quartos* com lista vazia
- Definição da classe através do construtor *__ init__* com os atributos *numero, tipo*
- Quarto pré definido como disponível com *self.disponivel = True*
- Adição automática de cada novo objeto da classe na lista da variável *quartos*
- Uso do médodo *__ str__* para converter para string e mostrar a disponibilidade do quarto 
- Uso do decorador @classmethod para criar um método de classe: *listagem_quartos*
- A função *listagem_quartos* mostra todos os quartos do hotel e disponibilidade de cada um

#### Reserva
- Definição da classe através do construtor *__ init__* com os atributos *cliente, quarto, check_in, check_out*

#### Gestor
- Definição da classe através do construtor *__ init__*
- Criação de variável *clientes* como atributo da classe, com lista vazia
- Definição da função *criar_reserva* com os mesmos atributos da classe Reserva
    - Através desta função, as reservas são adicionadas à lista *reservas* e os quartos ficam como Reservado
- Definição da função *cancelar_reserva* com os atributos *cancelar_reserva* e *cancelar_reserva*
    - Através desta função, os dados inseridos são procurados na lista *reservas* e removidos da mesma
- A função *ver_reservas* mostra todas as reservas registadas

---
---



**Autora:** Maria Helena Caseiro


**UFCD:** 10789 - Metodologias de Desenvolvimento de Software