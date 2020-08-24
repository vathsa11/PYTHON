n1=0
n2=1
l=int(input("Enter the number of terms: "))
if l==1:
    print(n1)
elif l==2:
    print(n1,", ",n2)
else:
    i=3
    print(n1,',',n2, end = ", ")
    while i<=l:
        n=n1+n2
        n1=n2
        n2=n
        print(n, end = ", ")
        i+=1
