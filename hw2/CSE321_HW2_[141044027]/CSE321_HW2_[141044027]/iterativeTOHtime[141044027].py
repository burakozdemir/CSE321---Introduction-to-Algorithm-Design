import sys

mylist = []
def Towers(A,B,C,n):
    if (A==1):
        source = "SRC"
    if (A==2):
        source = "AUX"
    if (A==3):
        source = "DST"
    if (C==1):
        dest = "SRC"
    if (C==2):
        dest = "AUX"
    if (C==3):
        dest = "DST"
    if n==1:
        print ("disk ",n,":",source," to ",dest)
        mylist[n-1] += n * abs(A-C)
    else:
        mylist[n-1] += n * abs(A-C)
        Towers(A,C,B,n-1)
        print ("disk ",n,":",source," to ",dest)
        Towers(B,A,C,n-1)

def TOHtime():
    length = input("Enter input size:")
    print ("Input size is ",length)
    global mylist 
    mylist = [0] * int(length)
    Towers(1,2,3,int(length))
    for i in range(0,int(length)):
        print ("Elapsed time for disk ",i+1,": ",mylist[i])
        
TOHtime()
