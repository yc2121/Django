print ##### Assignment: Score-n-Grade
def grade(arr):
  for i in arr:
    if i>=60 and i<=69:
      grade='D'
    elif i>=70 and i<=79:
      grade='C'
    elif i>=80 and i<=89:
      grade='B'
    elif i>=90 and i<=100:
      grade='A'
    else:
      print "Score not in grade range! "
    print 'Score:',i,'; Your grade is ',grade
  print 'End of the program. Bye.'

s=[87,67,95,100,75,90,89,72,60,98]
print 'Test data = ', s
grade(s)
