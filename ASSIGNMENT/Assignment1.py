# Assignment 1

#Q1
n=int(input("enter the number:"))
i=1
while(i<=n):
    print(i)
    i=i+1


#Q2
n=int(input("enter the number:"))
i=0
while(i<=n):
    print(i)
    i=i+2


#Q3
n=int(input("enter the number:"))
i=0
sum=0
while(i<=n):
    sum=i+sum
    i+=1
print(sum)


#Q4
n=int(input("enter the number:"))
while(n>=1):
    print(n)
    n=n-1


#Q5
n=int(input("enter the number:"))
i=1
f=1
while(i<=n):
    f=f*i
    i=i+1
print(f)


#Q6
n=int(input("enter the number:"))
i=1
for x in range(n-1,1,-1):
    if(n% x ==0):
        i=0
        print("{} is not prime".format(n))
        break

if(i==1):
    print("{} is prime".format(n))


#Q7
n=int(input("enter the number:"))

if n>=0 and n<=9:
    print("sum of digits is {}".format(n))
else:
    sum=0
    for x in range(len(str(n))):
        k=n%10
        sum=sum+k
        n=(n-k)/10
    sum=sum+n

    print("sum of digits is {}".format(sum))


#Q8
n=int(input("enter the number:"))
sum=1
print(sum)
for x in range(n):
    sum=sum*2
    print(sum)


#Q9
n=int(input("enter the number:"))

for i in range(n):

    for j in range(i+1):
        print(chr(j+65), end=" ")
    print()


#Q10
n=int(input("enter the number:"))

for i in range(n):

    for j in range(i+1):
        print(j+1, end=" ")
    print()
