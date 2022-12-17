n=8
x=[]
x1x2=[]
on=0
six=0
i=1
j=0

while i<(n+1):
    x.append(i)
    i=i+1

i=0
while i<n:
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

