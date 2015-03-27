def Dist (Pa,Pb):
    from math import sqrt
    if (len(Pa) != 2) or (len(Pb) != 2):
        print ('Valores de Entrada incompativeis')
    else:
        return float(sqrt(((Pa[0]-Pb[0])**(2))+((Pa[1]-Pb[1])**(2))))


def MaiorDist (LP):
    lista=[]
    for i in LP:
        for j in LP:
            d=Dist(i,j)
            lista.append(d)
            print lista
    return max(lista)

def Pol(Pa,Pb):
    from math import atan2
    from math import pi
    zero=(0,0)
    lista=[]
    if (len(Pa) != 2) or (len(Pb) != 2):
        print ('Valores de Entrada incompativeis')
    else:
        dA = Dist(Pa,zero)
        tetaA=atan2(Pa[1],Pa[0])
        lista.append((dA,tetaA*pi/180))
        dB = Dist(Pb,zero)
        tetaB=atan2(Pb[1],Pb[0])
        lista.append((dB,tetaB*pi/180))             
        return lista
                     
def is_tri_ret():
    from math import atan2
    from math import pi
    A=float(raw_input("digite o valor do primeiro cateto: "))
    B=float(raw_input("digite o valor do segundo cateto: "))
    C=float(raw_input("digite o valor da hipotenusa: "))
    if ((A**2)+(B**2))==(C**2):
        print(A*B/2)
    else:
        print(A,B,C)

def GPS(x,y,z):
    from math import atan
    from math import sqrt
    from math import sin
    from math import cos
    from math import pi
    h=0
    N=1
    a=6378160
    E=0.0066945185
    lamb=atan(y/x)*180/pi
    P=sqrt((x**2)+(y**2))
    for i in range(5):
        teta=atan(z/P*((1-E*N/(N+h)))**(-1))
        N=a/sqrt(1-E*(sin(teta)**(2)))
        h=(P/cos(teta))-N
    print(teta*180/pi,lamb,h)













        
