print(f'El tipo de "3" es {type(3)}')
print(f'El tipo de "-3" es {type(-3)}')
print(f'El tipo de "3.1" es {type(3.1)}')
print(f'El tipo de "True" es {type(True)}')


a1 = 'hola'
a2 = 'mundo'

print (a1,a2, sep= "-")

print(24 and 89 and 2)

print(24 or 89 or 2)

print(False or 89 or 2)

list=[1,"ya",True]
print(list)
list[0]=8
print(list)
tupla={1,"ya",True}
print(tupla)


entrada=input("Introduce tu nombre: ")
edad=int(input("introduce tu edad: "))
print(f'te quedan {99-edad} años de vida')
print("te quedan %d" %{99-edad})
print("Te quedan {}".format(99-edad))
print("Te quedan",99-edad,"años para morir")