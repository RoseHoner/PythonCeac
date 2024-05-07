def bucle():
    i=0
    while i!=10:
        yield "el valor de i es: " +str(i)
        i+=1
print(bucle())
iterador=bucle()
'''
print(next(bucle()))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
'''
for item in iterador:
    print(item)
print("-----------------")
for item in iterador:
    print(item)
print("-----------------")