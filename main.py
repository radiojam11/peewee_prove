# Prove di funzionamento di PeeWee con Gabrio
# Il sistema  serve per capire il funzionamento di peewee 
# e in particolare  ForeignKeyField
# per agganciare due o piu tabelle 
# poi  fatta una classe per costruire oggetti  class PersonaFactory():
# testato anche la funzionalita:
# backref
#  categoria = peewee.ForeignKeyField(Categoria, backref="persone") #

import peewee

db = peewee.SqliteDatabase('database_test.db')

class Categoria(peewee.Model):
    nome = peewee.CharField(unique=True)
    class  Meta():
        database = db

class Persona(peewee.Model):
    nome = peewee.CharField()
    eta = peewee.IntegerField()
    salario = peewee.IntegerField()
    categoria = peewee.ForeignKeyField(Categoria, backref="persone")
    class  Meta():
        database = db

class PersonaFactory():
    @staticmethod
    def create_persona(nome, eta, salario):
        if salario > 50000:
            categoria = Categoria.select().where(Categoria.nome == "Ricco").get()
        else:
            categoria = Categoria.select().where(Categoria.nome == "Povero").get()
        persona = Persona(nome = nome, eta = eta, salario = salario, categoria = categoria)
        persona.save()


db.connect()

db.create_tables([Persona, Categoria])

#Categoria(nome="Ricco").save()
#Categoria(nome="Povero").save()

ricchi = Categoria.select().where(Categoria.nome == "Ricco").get()
for user in ricchi.persone:
    print(user.nome, user.eta)


