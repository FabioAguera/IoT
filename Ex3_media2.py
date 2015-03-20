def media2():
    lista=[]
    s = 0
    v = True
    i=0
    while v:
        a = float(raw_input("digite a nota: "))
        lista.append(a)
        v = a > 0
    for i in lista:
        s += i
    media = s/len(lista)
    return media
print media2()
