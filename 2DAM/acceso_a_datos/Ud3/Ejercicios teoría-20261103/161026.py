#PARÁMETROS DE FUNCIÓN POR REFERENCIA
# a = "Hola"
# b = "Mundo"

# def suma(elem1,elem2):
#     #elem1+=elem2
#     elem3 = elem1+elem2
#     return elem3

# a = [1,2,3]
# b = [4,5]
# c = suma(a,b)
# print(c, id(c))
# print(a, id(a))
# print(b, id(b))

# #ARGUMENTOS POSICIONALES EN FUNCIÓN OBLIGATORIAMENTE
# def suma(a,b,/): #poner /
#     return a+b

# print(suma(a=1,b=2))

#PALABRAS RESERVADAS *args, **kwargs
#EJEMPLO1
# def funcion(*args,**kwargs):
#     print(f'args: {args} kwargs: {kwargs}')

# funcion()
# funcion(1)
# funcion(1,"Manuel",a="ok",b="ko")

#EJEMPLO2
# def calculo_general(*args,**kwargs):
#     r_suma = suma(**kwargs)
#     r_division = division(**kwargs)
#     r_potencia = potencia(**kwargs)
#     return r_suma * r_division * r_potencia

# def suma(op1,op2,**kwargs):
#     return op1+op2
# def division(op3,op4,**kwargs):
#     return op3/op4
# def potencia(op5,op6,**kwargs):
#     return op5**op6

# print(calculo_general(op1=1,op2=2,op3=3,op4=3,op5=1,op6=1))