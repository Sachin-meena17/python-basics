#while loop with else
i = 0
sum=0
while i<5:
    k=int(input("enter:"))
    sum=sum+k
    i=i+1
else:
    print(sum)
    print("end of while loop")


#Python program to illustrate
# combining else with while
count = 0
while (count < 3):
    count = count + 1
    print("Hello There")
else:
    print("In Else Block")

# for loop
for i in range(9):
  print(i)
for x in range(2, 7):
  print(x)
for x in range(2, 30, 3):
  print(x)
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()



# Prints all letters except 'e' and 's'
for letter in 'chocolatecookies':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

for letter in 'chocolatecookies':
    print(letter)
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break
print('Current Letter :', letter)


# finding greater number
a = int(input("a number "))
b = int(input("b number "))
if b > a:
    print("{} is greater than {}".format(b,a))
elif a > b:
    print("{} is greater than {}".format(a,b))
else:
    print("a is equal to b")