x=[]
n=int(input("enter number of ele in first vec:"))
for i in range(0,n,1):
	a=int(input("enter ele:"))
	x.append(a)
y=[]
print("Now for second vec:")
for i in range(0,n,1):
        a=int(input("enter ele:"))
        y.append(a)
d=0
for i in range(0,n,1):
        d+=x[i]*y[i]
print(d)
print(d)


