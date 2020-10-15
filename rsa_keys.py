import base64

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def divider(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return(a+b)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

print("Введите простое число p: ")
p = input()
p_int = int(p)
    
while(not isPrime(p_int)):
    print("Введите простое число p: ")
    p = input()
    p_int = int(p)
    
print("Введите простое число q: ")
q = input()
q_int = int(q)

while(not isPrime(q_int)):
    if (p != q):
        print("Введите простое число q: ")
        q = input()
        q_int = int(q)
    else:
        print("Число p не должно равняться q")
n = abs(p_int * q_int)
print("Коэффициент n = " + str(n))
print("Введите коэффициент e такой, что n и e не имеет общих делителей(кроме 1) и e - простое число")
e = input()
e_int = int(e)  

while(not isPrime(e_int)):
    if (not divider(e_int,n)):
        print("n и e имеют общие делители: ")
    print("Введите простое число e: ")
    e = input()
    e_int = int(e)
    
phi = (p_int - 1)*(q_int - 1)
d = modinv(e_int, phi)

print("Пара сгенерированного открытого ключа ("+str(e_int)+","+str(n)+")")
print("Пара сгенерированного закрытого ключа ("+str(d)+","+str(n)+")")

print("Введите сообщение, состоящее из латинских букв и цифр: ")
letter = input()
b = letter.encode("UTF-8")
e = base64.b64encode(b)
m = e.decode("UTF-8")
print("Закодированное сообщение "+letter+" : ",m)

b1 = m.encode("UTF-8")
d = base64.b64decode(b1)
s = d.decode("UTF-8")
print("Раскодированное сообщение "+letter+" : ",s)
