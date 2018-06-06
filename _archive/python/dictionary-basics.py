
import random

def draw_stars(L):
  s=''
  for i in L:
    for j in range(1,i+1):
      s+='*'
    print s; s=''

print '\n##### Assignment: Draw Stars\n'
x=[4,6,1,3,5,7,25]
print 'Test Data: x=',x,'\n'
draw_stars(x)

#---------------------------

def draw_stars_part_2(L):
  s=''
  for i in L:
    if type(i)==type('string'):
      marker=i[0].lower()
      start=0;end=len(i)
    else:
      start=0;end=i
      marker='*'
    for j in range(start,end):
      s+=marker
    print s; s=''

print '\n##### Assignment: Draw Stars Part II\n'

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
print 'Test Data: x=',x,'\n'
draw_stars_part_2(x)
