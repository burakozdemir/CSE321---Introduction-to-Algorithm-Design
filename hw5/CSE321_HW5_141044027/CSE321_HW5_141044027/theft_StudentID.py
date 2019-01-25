#Algoritmada listenin icindeki ilk listenin her elemanına baslangıc oldgu ıcın bakıyor
#Daha sonra alttakı elemanlara duruma gore secım yapıyor.
#WorstCase:O(n'2) . Ic ice donguler oldgu ıcın n^2

def theft(amountOfMoneyInLand):
    x = list(zip(*amountOfMoneyInLand))
    currentIndex=0
    result=0

    for i in range(0,len(x[0])):
        currentIndex=i
        genelIndis = 1
        resultTemp=x[0][i]
        for m in range(genelIndis,len(x)):
            t1 = currentIndex-1
            t2 = currentIndex
            t3 = currentIndex+1
            max1 = 0
            max2 = 0
            max3 = 0
            if( t1>=0 and t1<len(x[0]) ):
                max1 = x[m][t1]
            if(t2 >= 0 and t2 < len(x[0]) ):
                max2 = x[m][t2]
            if(t3 >= 0 and t3 < len(x[0]) ):
                max3 = x[m][t3]

            t=max(max1,max2,max3)
            resultTemp+=t

            if(t==max1):
                currentIndex = t1
            if (t == max2):
                currentIndex = t2
            if (t == max3):
                currentIndex = t3

        if(resultTemp>result):
            result=resultTemp

    return result

amountOfMoneyInLand= [[1,3,1,5], [2,2,4,1], [5,0,2,3], [0,6,1,2]]
res = theft(amountOfMoneyInLand)
print(res)
#Output: 16
amountOfMoneyInLand= [[10,33,13,15], [22,21,4,1], [5,0,2,3], [0,6,14,2]]
res = theft(amountOfMoneyInLand)
print(res)
#Output: 83