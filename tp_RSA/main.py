import codecs
import math

messages = [772942520,1093541194,154481546,876676876,1244840390,1259928347,1334120646,668279513,337542008,
875782511,556980142,927450584,1120552795,505519659,1425707357,561927611,623792775,993148007,284705483,1199652702,
894456779,583558895,1093170977,111276686,1273737639,447732981,1310131429,668279513,86285264,1297393867,63598178,
419642882,266423865,273531321,473923824,425740976,879596200,453134133,821431084,705745131,1242726576,512712067,1044869008,
1244840390,56468763,332825514,99331635,168593283,1077633623,1407939334,915256493,480148132,874550905,63981534,329372146,
725466080,815059584,1026780342,549262958,168593283,1152472931,246166200,672699349,434176708,332639250,1120552795,647161589,
813987580]

#var clePub,e correspondent à la clé publique (clePub=n)
clePub=1452848381
e=6991

def trouverNbPremier(n):
    """
    Fonction retournant deux nb prem dont le produit est n
    :param n -> clé publique
    :var racineCarre -> racine carrée du paramètre de la fonction n
    :return les 2 nb prem
    """
    racineCarre = int(math.sqrt(n))
    for q in range(3, racineCarre):
        if q%2!=0:
            if n%q==0:
                p= n//q
                return p,q

def euclide_etendu(a,b):
    """
    Fonction retournant le pgcd et les coef de Bézout de 2 nb entier relatif
    :param a -> 1er entier relatif:
    :param b -> 2ème entier relatif:
    :return 3 var->le pgcd et les 2 coef de Bézout
    """
    if (b==0):
        return a,1,0
    else:
        (pgcd,u,v)= euclide_etendu(b, a%b)
        return (pgcd,v,u-(a//b)*v)

def modinv(a, m):
    """
    Fonction qui calcule l'inv modulaire de 2 entiers
    :param a -> 1er entier relatif :
    :param m -> 2ème entier relatif :
    :var pgcd-> pgcd(a,m) retourné par la fct euclide_etendu()
    :var x -> coef de Bézout de a retourné par la fct euclide_etendu()
    :var y -> coef de Bézout de m retourné par la fct euclide_etendu()
    :return le coef de Bézout de a mod m
    """
    pgcd, x, y = euclide_etendu(a, m)
    if pgcd != 1:
        raise Exception('L\'inverse modulaire n\'existe pas')#les 2 nb ne sont pas premiers entre eux
    else:
        return x % m

def exporapide(a,x,n):
    """
    Fonction permettant le calcul de puissance modulo un nombre n
    -code inspiré du cours du Dr.Eggenberg->maths 1 S1 Crypto
    :param a -> base
    :param x -> exposant
    :param n -> modulo
    :var y -> exposant mod 2
    :var b -> la base mod n au carré mod n
    :return r -> résultat de l'opération soit le mod de m**e%n
    """
    if a == 0:
        r = 0
        return r
    elif x == 0:
        r = 1
        return r
    r = 1
    b = a % n
    while (x>0):
        y = x % 2
        r = (r*b**y)%n
        b = (b*b)%n
        x = x//2
    return r

def expoRapide(m, e, n):
    """
    Fonction permettant le calcul de puissance modulo un nombre n basée sur l'algo d'exponentiation rapide
    -code inspiré de stackoverflow-> https://stackoverflow.com/questions/5246856/how-did-python-implement-the-built-in-function-pow
    :param m -> base
    :param e -> exposant
    :param n -> modulo
    :return r -> reste de l'opération soit le mod de m**e%n
    """
    reste = 1
    while e:
        if e & 1:
            reste = reste * m % n
        e >>= 1
        m = m * m % n
    return reste

def calculClePrivee():
    """
    Fonction calculant la clé privé à partir d'un couple de nb prem d'une cle publique
    :var -> p,q = les 2 nb prem
    :var z -> indicatrice d'Euler (phi de (n))
    :return -> clé privée
    """
    p, q = trouverNbPremier(clePub)
    z = (p - 1) * (q - 1)
    ##variante 1->on utilise le coef de Bézout de l'exposant mod l'indicatrice d'Euler pour trouver la clé privée:
    #pgcd, x, y = euclide_etendu(e, z)
    #d = x % z
    ##variante 2->on utilise l'inv mod de l'exposant et de l'indicatrice d'Euler pour trouver la clé privée
    d = modinv(e, z)
    return d

def intToUtf8(m):
    m = str(hex(m)[2:]) # Prendre à partir du deuxiÃ¨me caractÃ¨re (aprÃ¨s le 0x)
    m = "".join(reversed([m[i:i+2] for i in range(0, len(m), 2)])) # Inversion des octets 0x20654A ==> 0x4A6520
    m = codecs.decode(m,"hex").decode('utf-8') # DÃ©codage
    return m

def parcoursListe(liste, exposant, clePublique):
    messageFinal= ""
    for i in liste:
        m = exporapide(i,exposant,clePub)
        #m = expoRapide(i,exposant,clePublique)
        #m = pow(i, exposant, clePublique)
        # code = m.to_bytes(4, 'little')
        # mess = code.decode("UTF-8")
        messageFinal+=intToUtf8(m)
    print(messageFinal)

if __name__ == '__main__':
    parcoursListe(messages,calculClePrivee(),clePub)
