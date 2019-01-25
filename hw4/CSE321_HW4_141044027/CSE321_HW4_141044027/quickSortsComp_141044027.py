#Daha az swap yapmaya yardımcı olur bu teknikle ve
# quick sort ile etkili calısırlar
#Ama en sona kadar taramak dezavantaj olur.

def lamutoScheme(arr,low,high):
    piv=arr[high]
    i=(low-1)
    index=low
    while(index<high):
        if(arr[index]<=piv):
            i+=1
            arr[i],arr[index]=arr[index],arr[i]
            index+=1
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)
def quickSortLomuto(arr):
    return myquickSortl(arr,0,len(arr)-1)
def myquickSortl(arr,lowIndex,highIndex):
    if(lowIndex<highIndex):
        pivot=lamutoScheme(arr,lowIndex,highIndex)
        myquickSortl(arr,lowIndex,pivot-1)
        myquickSortl(arr,pivot+1,highIndex)
    return arr
###############################
def hoareScheme(arr,low,high):
    i=low-1
    j=high+1
    piv=arr[low]
    flag=True
    while(flag):
        i+=1
        while(arr[i]<piv): i+=1
        j-=1
        while(arr[j]>piv): j-=1
        if(i>=j):
            flag=False
        if(not(i>=j)):
            arr[i],arr[j]=arr[j],arr[i]
    return j
def quickSortHoare(arr):
    return myquickSorth(arr,0,len(arr)-1)
def myquickSorth(arr,lowIndex,highIndex):
    if(lowIndex<highIndex):
        pivot=hoareScheme(arr,lowIndex,highIndex)
        myquickSorth(arr,lowIndex,pivot)
        myquickSorth(arr,pivot+1,highIndex)
    return arr
        
    
arr = [4, 15, 16, 24, 42, 68, 75]
qsh = quickSortHoare(arr)
print(qsh)
#Output: [4, 15, 16, 24, 42, 68, 75]
qsl = quickSortLomuto(arr)
print(qsl)
#Output: [4, 15, 16, 24, 42, 68, 75]