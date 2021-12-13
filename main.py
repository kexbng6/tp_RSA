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