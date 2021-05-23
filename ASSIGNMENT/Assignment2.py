# Assignment 2

#Q1

p=int(input("enter the percentage: "))

if p>=90:
    print("Excellent performance")
elif p>=80:
    print("very good performance")
elif p>=70:
    print("good performance")
elif p>=60:
    print("average performance")
else:
    print("poor performance")

#Q2

y=int(input("enter the year: "))

if(y%4==0):
    if y%100==0:
        if y%400==0:
            print("{} is leap year".format(y))
        else:
            print("{} is leap year".format(y))
    else:
        print("{} is leap year".format(y))
else:
    print("{} is not leap year".format(y))

#Q3

marriage=input("are you married?[Y/N]")
age=int(input("enter your age: "))
gender=input("are you male or female?")
marriage=marriage.capitalize()
gender=gender.capitalize()
if marriage == "Y":
    print("you are eligible for insurance")
elif gender == "Male" and age > 30:
    print("you are eligible for insurance")
elif gender == "Female" and age > 25:
    print("you are eligible for insurance")
else:
    print("you are not eligible for insurance")


#Q4
s=int(input("Enter your salary: "))
y=int(input("Enter your year of service: "))

if y>5:
    print("your net bonus is ",s/20)
else:
    print("you will not get bonus")

#Q5

s=input("enter the string: ")
digits=0
letter=0
for x in s:
    if x.isdigit():
        digits=digits+1
    else:
        letter=letter+1
print("number of digits in string are {} and letter are {}".format(digits,letter))
#Q6

x,y,z=input("enter the sides of triangle(separate sides with commas)").split(",")

if x==y and y==z:
    print("it is a equilateral triangle")
elif x!=y and y!=z:
    print("it ia a scalene triangle")
else:
    print("it ia a isosceles triangle")

#Q7
b=int(input("enter the unit of electricity used: "))
bill=0
if b>=0 and b<=100:
    print("your electricity bill is {}".format(bill))
elif b>100 and b<=200:
    bill=(b-100)*5
    print("your electricity bill is {}".format(bill))
else:
    bill=(b-200)*10+5*100
    print("your electricity bill is {}".format(bill))

#Q8

b=int(input("enter the cost price of bike: "))

if b>10000:
    print("the road tax to be paid is {}".format(15))
elif b>5000 and b<=10000:
    print("the road tax to be paid is {}".format(10))
else:
    print("the road tax to be paid is {}".format(5))