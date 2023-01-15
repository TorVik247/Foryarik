import math
x=[]
n=8
x1x2=[]
on=0
six=0
pi=[]
n2=[]
y=[]
xyi=[]
xui=[]

i=1
j=0

while i<(n+1):
    x.append(i)
    i=i+1

i=0
while i<n:#створення таблички 1
    while  j<n:
        po=(x[six]**2)+(2*x[on])
        x1x2.append(po)
        on =on +1
        j=j+1
    on = on - n
    six =six + 1
    j=0
    i=i+1

i=0
#for j in x1x2:   #вивод
 #   if i>n-1:
  #      print()
   #     i=0
    #if j<10:
     #   print(j, end="  ")
    #else:
     #   print(j, end=" ")
    #i=i+1

t=x1x2[0]
while t<=po:                    #y
    y.append(t)
    t=t+1

i=y[0]
while i<=po:                    #n
    n2.append(x1x2.count(i))
    i=i+1

i=0
while i<len(y):                 #pi
    j=n2[i]
    if j==0:
        pi.append(j)
        i = i + 1
    else:
        pit=j/(n*n)
        pi.append(pit)
        i=i+1
#print()
#print()
#print('y =',y)
#print('pi=',pi)
#print('n =', n2)


do=0
i=0
while n>do:
    do=do+1
    i=0
    doo = 0
    while i<len(y):
        if (( ((y[doo]-(do**2))/2) >= 1 ) and ( ((y[doo]-(do**2))/2) <= n ) and ( ((y[doo]-(do**2))/2-int(((y[doo]-(do**2))/2))) == 0 )):
            xyi.append(1/64)
        else:
            xyi.append(0)
        doo=doo+1
        i=i+1
i=0
for j in xyi:   #вивод
    if i>len(y)-1:
        print()
        i=0
    else:
        print(j, end=" ")
    i=i+1

do=0
i=0
while n>do:
    do=do+1
    i=0
    doo = 0
    while i<len(y):
        if (( ((y[doo]-(do**2))/2) >= 1 ) and ( ((y[doo]-(do**2))/2) <= n ) and ( ((y[doo]-(do**2))/2-int(((y[doo]-(do**2))/2))) == 0 )):
            porn=math.log10((y[doo]-(do**2))/2)
            xui.append(porn)
        else:
            xui.append(0)
        doo=doo+1
        i=i+1
print()
for j in xui:   #вивод
    if i>len(y)-1:
        print()
        i=0
    else:
        print(j, end=" ")
    i=i+1