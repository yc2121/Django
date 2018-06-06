class MathDojo(object):
    def __init__(self,*x):
        self.result=0
        print 'Start with =',str(self.result)

    def add(self,*x):
        for i in x:
            print "+",i
            self.result+=i
        return self
    def subtract(self,*x):
        for i in x:
            print "-",i
            self.result-=i
        return self
    def resetIt (self):
        self.result=0

print '*** Assignment: MathDojo'
md=MathDojo()
print str( md.add(2).add(2,3).result ); md.resetIt()
print str( md.add([1],3,4).add([3,5,7,8],[]).result ); md.resetIt()


# print str( md.add(2).add(2,5).subtract(3,2).result )
