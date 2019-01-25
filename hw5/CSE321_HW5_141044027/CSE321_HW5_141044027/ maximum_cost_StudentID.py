#result liste olarak 1'lerden olusan bır lıste tutluyor.
#daha sonra bu listeye kucukten buyuge sıralanmıs orjinal listenin elemanları
#sırası ıle koyuluyor . Kontroller yapılıp gereklı yerlere 1 koyulduktan sonra
#sıralı lıstenın sonuna kadar gıdılıyor.Sort yaparken otomatık fonksıyon kullanıldı.
#Worst Case:O(n^2) ana dongunun ıcınde yardmcı fonksıyonlar cagırıldgında onlarında
#ıcınde dongu oldgu ıcın n'2 karmasıklıgındadır .


#Bu fonksiyon internetten alındı
def frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
#######
def findInd(value,arr,isaretci):
    tempIsaretci=0
    for i in range(0,len(arr)):
        if(value==arr[i]):
            if(tempIsaretci==isaretci):
                return i
            tempIsaretci+=1
def sumOfList(liste):
    res = 0

    for i in range(0,len(liste)):
        if(i+1<len(liste)):
            res += abs(liste[i] - liste[i + 1])

    return res
def coz(orjinal,resList):
    resultMax = 0
    sirali=sorted(orjinal)
    isaretciDict = frequency(orjinal)
    tempisaretciDict = isaretciDict
    for i in orjinal:
        tempisaretciDict[i]=0

    siraliIndis=0

    for i in range(0,len(orjinal)):
        tempVal=sirali[siraliIndis]

        orjInds=findInd(sirali[siraliIndis],orjinal,tempisaretciDict[sirali[siraliIndis]])
        tempisaretciDict[sirali[siraliIndis]]+=1

        resList[orjInds]=sirali[siraliIndis]
        tempresList=resList.copy()
        tempresList2=resList.copy()

        if (orjInds + 1 <= len(resList)):

            tempresList[orjInds]=1
            if(sumOfList(tempresList)>resultMax):
                resList=tempresList.copy()
                resultMax= sumOfList(tempresList)

            if(orjInds+1<=len(resList)):

                if (orjInds - 1 == 0):
                    tempresList2[orjInds] = 1
                    t2 = resList.copy()
                    if (sumOfList(tempresList2) > resultMax):
                        resList = tempresList2.copy()
                        resultMax = sumOfList(tempresList2)

                    if (sumOfList(t2) > resultMax):
                        resList = t2.copy()
                        resultMax = sumOfList(t2)

                if(orjInds+1==len(tempresList2)):
                    tempresList2[orjInds] = 1
                    t2=resList.copy()
                    if (sumOfList(tempresList2) > resultMax):
                        resList = tempresList2.copy()
                        resultMax = sumOfList(tempresList2)

                    if (sumOfList(t2) > resultMax):
                        resList = t2.copy()
                        resultMax = sumOfList(t2)



                else:

                    tempresList2[orjInds+1] = 1
                    if (sumOfList(tempresList2) > resultMax):
                        resList=tempresList2.copy()
                        resultMax = sumOfList(tempresList2)

                    tempresList2[orjInds - 1] = 1
                    if (sumOfList(tempresList2) > resultMax):
                        resList = tempresList2.copy()
                        resultMax = sumOfList(tempresList2)


        siraliIndis+=1


    return resultMax
def find_maximum_cost(mylist):
    length = len(mylist)

    res = []
    for i in mylist:
       res.append(1)

    result = coz(mylist,res)
    return result

Y = [2,8,9,1,1,20,21]
cost = find_maximum_cost(Y)
print(cost)
#Output: 55
Y = [14,1,14,1,14]
cost = find_maximum_cost(Y)
print(cost)
#Output: 52
Y = [1,9,11,7,3]
cost = find_maximum_cost(Y)
print(cost)
#Output: 28
Y = [50,28,1,1,13,7]
cost = find_maximum_cost(Y)
print(cost)
#Output: 78