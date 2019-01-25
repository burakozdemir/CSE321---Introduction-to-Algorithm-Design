#binary searchteki gibi fonksyonlara
#yarısı göndererek log zamanda index aranıyor .
#Lakin 2 farklı array oldgundan karmasıklık log(n+m) oluyor
#Algoritmada sürekli arrayların ortanca deger ile kesilip parcalanması ile
#yeni arraylar olusturuluyor . Base case durumunda 0 ve 1 elemanlı 2 array kalıyor
def findIndex(arr1, arr2, index):
    if (len(arr1)== 0):
        return arr2[index]
    if (len(arr2)== 0):
        return arr1[index]
    orta1 = int(len(arr1) / 2)
    orta2 = int(len(arr2) / 2)
    if(orta1+orta2<index):
        if( arr1[orta1] > arr2[orta2] ):
            return findIndex(arr1, arr2[orta2 + 1:], index - orta2 - 1)
        else:
            return findIndex(arr1[orta1 + 1:], arr2, index - orta1 - 1)
    else:
        if( arr1[orta1] > arr2[orta2] ):
            return findIndex(arr1[:orta1], arr2, index)
        else:
            return findIndex(arr1, arr2[:orta2], index)

def find_kth_book_1(array1,array2,index):
    return findIndex(array1, array2, index - 1)

m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop"]
book = find_kth_book_1(m,n,4)
print(book)
#Output: oop
book = find_kth_book_1(m,n,6)
print(book)
#Output: systemsprogramming


