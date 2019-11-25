class sortAlgorithm(object):

    def choosesort(self,x):
        N=len(x)
        for i in range(len(x)):
            min=i
            for j in range(i,len(x)):
                if less(x[j],x[min]):
                    min=j
            exch(x,i,min)
    def show(self,x):
        print(x)
    def exch(self,x,i,j):
        x[i],x[j]=x[j],x[i]
    def less(self,a,b):
        return a<b
    def __init__(self,comparelist):
        self.uselist=comparelist
        choosesort(comparelist)
        show(comparelist)

x=[1,9,8,5,7,3,4,2]
y=sortAlgorithm(x)




