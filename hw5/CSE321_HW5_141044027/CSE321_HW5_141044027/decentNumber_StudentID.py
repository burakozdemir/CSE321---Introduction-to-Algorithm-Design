#Algoritmada önce beslerin kac tane olabilecegine bakılıyor
#kalan kısımlada 3 lerin kac tane olabilecegıne bakılıyor.
#Daha sonra resulta uc ve besın degerlerıne gore strıng eklenıypr

def decentNumber(val):
    result = ""
    uc,bes = 0,0
    x = val
    #
    while(x > 0):
        if(x % 3 == 0):
            bes = x
            break
        x -=5
    uc = (val-x)
    if((x < 0)or(uc % 5 !=0)):
        return str(-1)
    while(bes > 0):
        bes -= 1
        result+=(str(5))
    while(uc > 0):
        uc -= 1
        result+=(str(3))
    return result

dn = decentNumber(1)
print(dn)
#Output: -1
dn = decentNumber(3)
print(dn)
#Output: 555
dn = decentNumber(5)
print(dn)
#Output: 33333
dn = decentNumber(11)
print(dn)
#Output: 55555533333