def odd_even():
  x='odd'
  for i in range(1,10):
    print 'Number is ',i,'. This is an ',x,' number.'
    if x=='odd':
      x='even'
    else:
      x='odd'

print '***** Function Odd_Even(), show 10 sample points'
odd_even()
###########################
def multiply(L,x):
  aList=[]
  for i in L:
    aList.append(i*x)
  return aList

print '\n***** Function multiply()'
a=[2,4,10,16]; print 'input: ',a
b=multiply(a,5)
print b

######################
def layered_multiples(arr):
  new_array=[]
  for i in arr:
    z =[]
    for j in range(1,i+1):
      z+='1'
    new_array.append(z)
  return new_array

print '\n***** Function layered_multiples()'
print '\ntest: layered_multiples(multiply([2,4,5],3))'
x = layered_multiples(multiply([2,4,5],3))
for i in x:
  print '\n',str(i)
