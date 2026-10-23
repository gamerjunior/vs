# x = 10

# if(x<10):
#     print("x<10")
# elif(x==10):
#     print("coca")
# else:
#     print("caca")

# for i in range(10):
#     print(i,end="\n")

# print(list(range(10)))

# contador = 0
# while(contador < 10):
#     print(contador)
#     contador = contador + 1
#     if(contador == 5):
#         print("por el culo te lhinco")

lista = [0,1,2,3,4,5,4,3,0,0,2]
i = 0
contador = 0
# while i < len(lista) :
#     if lista[i] == 0 :
#         contador+= 1
#     i +=1
# print(f"El numero de ceros es {contador}")

# contador = 0
# for i in range(len(lista)):
#     if(lista[i] == 0):
#         contador += 1
# print(f"El numero de ceros es {contador}")

# contador = 0
# contador_iteraciones = 0
# for i in range(len(lista)):
#     if(lista[i] == 0):
#         continue
#         contador+=1
#     contador_iteraciones += 1


# print(f"El numero de ceros es {contador}")


# def suma(a,b):
#     return(a+b)
# print(suma(1,2))

# def suma(*valores):
#     return(sum(valores)),
# print(suma(1,2,3,4,5,6,7,8,9,4,8,7,9))

def operaciones(a,b):
    suma=a+b 
    resta = a-b
    mult=a*b
    div=a/b
    return(suma,resta,mult,div)
print((operaciones(1,2)))


lista = ["a","e","i","o","u"]
print(lista)
lista.append("AEIOU")
print(lista)
lista.extend("AEIOU")
print(lista)
sublista= lista[0:5]
print(sublista)

dict = {"alu1":"juan","alu2":"raul"}
print(len(dict))
print(dict.values())
print(dict.keys())
print(dict.items())
