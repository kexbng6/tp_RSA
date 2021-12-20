import math
import random

messages = [772942520,1093541194,154481546,876676876,1244840390,1259928347,1334120646,668279513,337542008,
875782511,556980142,927450584,1120552795,505519659,1425707357,561927611,623792775,993148007,284705483,1199652702,
894456779,583558895,1093170977,111276686,1273737639,447732981,1310131429,668279513,86285264,1297393867,63598178,
419642882,266423865,273531321,473923824,425740976,879596200,453134133,821431084,705745131,1242726576,512712067,1044869008,
1244840390,56468763,332825514,99331635,168593283,1077633623,1407939334,915256493,480148132,874550905,63981534,329372146,
725466080,815059584,1026780342,549262958,168593283,1152472931,246166200,672699349,434176708,332639250,1120552795,647161589,
813987580]

clePub=1452848381
e=6991

def trouverNbPremier(n):
    moitie = int(math.sqrt(n))
    for q in range(3, moitie):
        if q%2!=0:
            if n%q==0:
                p= n//q
                return p,q

def euclide_etendu(a,b):
    if (b==0):
        return a,1,0
    else:
        (pgcd,u,v)= euclide_etendu(b, a%b)
        return (pgcd,v,u-(a//b)*v)

def modinv(a, m):
    g, x, y = euclide_etendu(a, m)
    if g != 1:
        raise Exception('L\'inverse modulaire n\'existe pas')
    else:
        return x % m

def exporapide(a,n):
    if n==0:
        return 1
    b=exporapide(a,n//2)
    if (n%2)==1:
        return b*b*a
    else:
        return b*b

p,q=trouverNbPremier(clePub)

z=(p-1)*(q-1)

pgcd,x,y=euclide_etendu(6991,z)

d=x%z

def parcoursListe(liste, exposant, clePublique):
    messageFinal= ""
    for i in liste:
        m = pow(i, exposant, clePublique)
        # code = m.to_bytes(4, 'little')
        # mess = code.decode("UTF-8")
        messageFinal+=intToUtf8(m)
    print(messageFinal)

def intToUtf8(m):
    m = str(hex(m)[2:]) # Prendre à partir du deuxiÃ¨me caractÃ¨re (aprÃ¨s le 0x)
    m = "".join(reversed([m[i:i+2] for i in range(0, len(m), 2)])) # Inversion des octets 0x20654A ==> 0x4A6520
    m = codecs.decode(m,"hex").decode('utf-8') # DÃ©codage
    return m

parcoursListe(messages,d,clePub)