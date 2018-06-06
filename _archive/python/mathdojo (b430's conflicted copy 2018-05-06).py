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

