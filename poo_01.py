from pessoa import Pessoa

p1 = Pessoa("Luiz", 29)
p2 = Pessoa("João", 32)

p1.comer("maçã")
p2.comer("sorvete")
p1.falar("POO")
p1.parar_comer()
p1.falar("POO")
p1.comer("alimento")
p1.parar_falar()
p1.falar("assunto")

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())