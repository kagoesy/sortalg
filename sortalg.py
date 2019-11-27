import time
import random

def choosesort(x):
    N = len(x)
    for i in range(len(x)):
        min = i
        for j in range(i,len(x)):
            if less(x[j],x[min]):
                min = j
        exch(x,i,min)
    return x

def show(x):
    print(x)

def exch(x,i,j):
    x[i],x[j] = x[j],x[i]

def less(a,b):
    return a < b

def insertsort(x):
    N = len(x)
    for i in range(N):
        j=i
        while j>0 and less(x[j],x[j-1]):
            exch(x,j,j-1)
            j-=1
    return x
def shell(x):
    N=len(x)
    h=1
    while h<N/3:
        h=3*h+1
    while h>=1:
        #print(h)
        for i in range(h,N):
            j=i
            while j>=h and less(x[j],x[j-h]):
                exch(x,j,j-h)
                j-=h
        h=h//3
    return x
def sortTime(alg,x):
    t0=time.process_time()
    if alg=="shell":
        shell(x)
    elif alg=="choosesort":
        choosesort(x)
    elif alg=="insertsort":
        insertsort(x)
    t1=time.process_time()
    return t1-t0

def randominputsort(alg,N,T):
    total=0
    for i in range(T):
        randomlist=[]
        for j in range(N):
            randomlist.append(random.uniform(0,1000))
        total+=sortTime(alg,randomlist)
    return total

a=randominputsort("shell",1000,10)
b=randominputsort("insertsort",1000,10)
print("shell:{}".format(a))
print("insertsort:{}".format(b))
def procedure():
    a=0
    for i in range(100000000):
        a+=1
#a=time.process_time()
#procedure()
#c=time.process_time()
#print(a-c)


