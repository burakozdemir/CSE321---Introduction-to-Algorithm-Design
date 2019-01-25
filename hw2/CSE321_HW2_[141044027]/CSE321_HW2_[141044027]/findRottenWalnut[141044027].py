import sys

def compareScales (leftScaleList, rightScaleList):
    result = sum(leftScaleList) - sum(rightScaleList)
    if result < 0:
        return 1
    elif result > 0:
        return -1
    else:
        return 0

#bu helper function internetten alındı
def split_list(a_list):
    half = len(a_list)/2
    return a_list[:int(half)], a_list[int(half):]

#begin ve end indis turunden
def myfind(mylist,begin,end):
    print(mylist)
    ##base case
    if(len(mylist)==1):
        print ("bulunan indis",int(begin))
        return begin
    if (len(mylist)==2):
        B,C = split_list(mylist)
        if(compareScales(B,C)==1):
            print ("sag buyuk")
            print ("bulunan indis:",int(begin))
            return int(begin)
        if(compareScales(B,C)==-1):
            print ("sol buyuk")
            print ("bulunan indis:",int(end))
            return int(end)
        if(compareScales(B,C)==0):
            return 0
    ##uzunlugun 3 oldgu durum
    if (len(mylist)==3):
        B,C = split_list(mylist)
        c1,c2 = split_list(C)
        if(c1==c2):
            if(B!=c1):
                print("bulunan indis:",int(begin))
                return int(begin)
            if(compareScales(c1,c2)==0):
                print ("Farkli bulunamadi")
                return 0
            print ("sag ikiside buyuk list length 3")
            print ("bulunan indis ",int(begin))
            return int(begin)
        if(c1!=c2):
            if(compareScales(B,C)==1):
                print ("sag buyuk list length 3")
                myfind(C,(begin + end)/2,end)
            if(compareScales(B,C)==-1):
                print ("sol buyuk list length 3")
                myfind(B,begin,(begin + end)/2)
    ####listlerin esit sayida bolunmesi
    if (len(mylist)%2==0):
        B,C = split_list(mylist)
        if(compareScales(B,C)==1):
            print ("sag buyuk esit uzunluktaki list")
            myfind(B,begin,((begin+end)/2))
        if(compareScales(B,C)==-1):
            print ("sol buyuk esit uzunluktaki list")
            myfind(C,((begin+end)/2)+1,end)
        if(compareScales(B,C)==0):
            print ("esit scales,farklı bunumadı")
            return 0
    ###listlerin esit uzunlukta bolunememesi
    if (len(mylist)%2==1):
        B,C = split_list(mylist)
        c1,c2 = split_list(C)
        b1,b2 = split_list(B)
        if(len(c1)==len(c2)):#sag tarafin cift olma durumu
            if (c1!=c2):
                print ("c1 c1 basamak esit kendileri degil")
                myfind(C,(begin + end)/2,end)
            if (c1==c2):
                print ("c1 c1 basamak esit kendileri esit")
                myfind(B,begin,((begin+end)/2)-1)
        if(len(c1)!=len(c2)):#sag tarafin tek olma durumu
            if(b1!=b2):
                print ("c1 c1 basamak esit degil b1 b2 esit degil")
                myfind(B,begin,((begin+end)/2)-1)
            if(b1==b2):
                print ("c1 c1 basamak esit degil b1 b2 esit")
                myfind(C,(begin+end)/2,end)
    if(len(mylist)==0):
        print ("Bos list")
def findRotten(mylist):
    length = len(mylist)
    print ("List length:",length)
    myfind(mylist,0,length-1)
    
mylist = [1,1,1,1,1,0.5,1,1,1]
findRotten(mylist)
#print (split_list(mylist))
