print ##### Assignment: Coin Tosses

import random

def coin_toss(t):
  head=0; tail=0; toss=''
  m1='Attempt #'; m2=": Throwing a coin... It's a"
  m3='! ... Got '; m4='head(s) so far and '; m5='tail(s) so far'
  for i in range(1,t+1):
    r=round(random.random())
    #---- for testing
    # print 'r=',str(r)
    #----------------
    if r==1.0:
      head+=1; toss='head'
    else:
      tail+=1; toss='tail'
    print m1,str(i),m2,toss,m3,str(head),m4,str(tail),m5

coin_toss(10)

