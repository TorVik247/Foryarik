n=8
x=[]
x1x2=[]
pi=[]
y=[]
on=0
six=0
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
for j in x1x2:   #вивод
    if i>n-1:
        print()
        i=0
    print(j, end=" ")
    i=i+1

t=x1x2[0]
while t<=po:
    y.append(t)
    t=t+1
print()
print('y =',y)

i=y[0]
while i<=len(y):#неправильно
    pit=i/len(y)
    pi.append(pit)
    i=i+1

print()
print(pi)
