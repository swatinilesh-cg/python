#A. input() and print()
#1
name=input("Enter name : ")
print(name)
#2
city=input("Enter yout city : ")
print(city)
#3
user_name=input("Enter name : ")
print(f"user name : {user_name}")
#4
print(f" type of input : {type(name)}")
#5
Name=input("Enter name : ")
print(f"name {Name} , type of input : {type(Name)}")

#B. Multiple Inputs

#6
first_name=input("enter your first name : ")
last_name=input("enter your last name : ")
print(f"first name {first_name} \n last name : {last_name}")

#7
Name,City,College=input("Enter name , city , college : ").split()
print(Name,City,College)

#8
fn,sn=input("Enter 2 names : ").split()
print(fn,sn)

#9
programe,=input("Enter programe : ").split()
print(programe)
print(type(programe))

#10
name1,subject,programe1=input("Enter name,sub,pro : ")
print(f"name :  {name1}, subject: {subject},programe: {programe1} ")

#C. Type Conversion

#11,12,13
x="25"
print(int(x))
y="25.5"
print(float(y))
z=100
print(str(z))
#14
a1=int(input("Enter an interger : "))
print(type(a1))
#15
a2=float(input("Enter an interger : "))
print(type(a2))
#16
a3=input()
a4=input()
print(a3+a4)
#produce string concatenation instead of numeric addition becz a3 and a4 are string datatypes here
# becz input is bydefault string type

#17

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)


#D. Formatted Output and f-Strings

#18
a5="swati"
a6=20
print(f"Name : {a5} and I am {a6} year old")

#19
a7=100
a8=101
print(f"sum : {a7+a8}")

#20
user_Name,age=input("Enter username and age : ")
print(f"userName : {user_Name} and my age is {age}")

#21/22
price=float(input("Enter price : "))
print(f"price in 2 decimal : {price:.2f}")

#23
product_name=input("enter product name : ")
quantiy=int(input("Enter qt : "))
price=float(input("Enter price : "))
print(type(name))
print(f"Name : {name} \nproduct name : {product_name}\nquantity : {quantiy}\nprice:{price}")

#24
print("A", "B", "C")

#25
date= 4
month= 9
year=2026
print(date,month,year,sep=("-"))

#26
print("Hello",end="  ")
print("world")
#27
first_number,sencond_number=map(int,input("Enter 2 no. : ").split())
print(f"No. 1 : {first_number} and No.2 : {sencond_number} \n Sum : {first_number+sencond_number}")
#28
price=float(input("Enter price : "))
quantity=int(input("Enter quantity : "))
Total=price*quantity
print(f"price : {price} , quantity : {quantity} , Total : {Total}")
#29
s_name=input("Enter student name : ")
s_age=int(input("Enter student age : "))
s_marks=float(input("Enter student marks : "))
print(f"name : {s_name} age : {s_age} marks : {s_marks}")
#30
student_name=input("Enter student name : ")
student_age=int(input("Enter student age : "))
student_height=float(input("enter student height : "))
student_city=input("Enter student city : ")
print(f"name {student_name}\nage : {student_age}\nheight : {student_height}\ncity : {student_city}")

#:.2f means format the number as a floating-point value with exactly 2 decimal places.
print(f"{student_height:.2f}")