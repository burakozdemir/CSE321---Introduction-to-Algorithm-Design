#3. sorunun aksine burda 2 arrayin maximum
#degeri alınıyor normalde O(logn + logm) olan
#karmasıklık burda log(K) oluyor.
def findarray(arr1, arr2, arr1Len, arr2Len, index):
    index1 = min(arr1Len, int(index / 2))
    index2 = min(arr2Len, int(index / 2))
    ##base case durumları
    if(index>(arr1Len+arr2Len) or index<1):return -1
    if(arr1Len>arr2Len):
        return findarray(arr2, arr1, arr2Len, arr1Len, index)
    if(arr1Len==0):
        return arr2[index - 1]
    if(index==1):
        return min(arr1[0],arr2[0])
    #recursive part
    if(arr1[index1-1]>arr2[index2-1]): return findarray(arr1,arr2[index2:], arr1Len, arr2Len - index2, index - index2)
    else: return findarray(arr1[index1:], arr2, arr1Len - index1, arr2Len, index - index1)

def find_kth_book_2(arr1,arr2,ind):
    return findarray(arr1,arr2,len(arr1),len(arr2),ind)
m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop"]
book = find_kth_book_2(m,n,4)
print(book)
#Output: oop
book = find_kth_book_2(m,n,6)
print(book)
#Output: systemsprogramming
