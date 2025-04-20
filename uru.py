#print function
print("hello world") #double quote
print('hii') #single quote
print("hello\nmorning") #\n for new line
print("hii\tbye") #\t for tab
#variables
is_active = True
a=2 
b="hello"
c='hello'
print(a) #int
print(b) #string double quote
print(c) #string single quote
print(is_active) #boolean
print(type(a)) #variable type
print(type(b))
print(type(is_active))
#string
A='HEL'
B='LO'
print(A+B)
print(b*a)
d="hi I am Ranja"
print(d.replace("Ranja","cr"))
print(d.upper())
print(d.lower())
print(d.find("i"))
print(d.count("m"))
print(len(d))
print(d[:5])
print(d[6:])
print(d[3:6])
#swapping without third variable with user input
x=int(input("enter the 1st number: "))
y=int(input("enter the 2nd number: "))
print(f"value before swapping {x} and {y}")
x=x+y
y=x-y
x=x-y
print(f"value after swapping {x} and {y}")
#swapping with third variable with user input
x=int(input("enter the 1st number: "))
y=int(input("enter the 2nd number: 33"))
print(f"value before swapping {x} and {y}")
temp=x
x=y
y=temp
print(f"value after swapping {x} and {y}")
#check if a number is positive,negative or zero
num=float(input("enter the number: "))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")
#if a number is even or odd
if num%2==0:
    print("even")
else:
    print("odd")
#to find the sum of 2 digits
n=int(input("enter a two digit number: "))
r=n%10
r2=n//10
add=r+r2
print(f"results: {add}")
#palindrome number
palnum=int(input("enter the number: "))
cal1=palnum%10
cal2=palnum//10
rev=(cal1*10)+cal2
if palnum==rev:
    print("palindrome")
else:
    print("not")
#if a person is eligible to vote or not
age=int(input("enter yout age: "))
if age>18:
    print("you are eligible to vote")
else:
    print("go back to school")
#attendence status
attend=int(input("enter the percentage of attendance: "))
if attend>100:
    print("invalid attendance")
elif attend>=75:
    print("you are eligible to sit in exam")
elif attend<60:
    print("You have to pay a fine of 6000")
else:
    print("you are not eligible to sit in exam")
#grade calcualtion
g= float(input("enter percentage: "))
if g>100:
  print("not valid")
elif g>= 95:
  print("Grade: O")
elif g>= 90:
  print("Grade: A+")
elif g>= 80:
  print("Grade: A")
elif g>= 75:
  print("Grade: B+")
elif g>= 70:
   print("Grade: B")
elif g>= 60:
   print("Grade: C+")
elif g>= 50:
   print("Grade: C")
elif g>= 40:
  print("Grade: D")
else :
  print("Grade: F")
#leap year
year=int(input("enter the year: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("leap year")
else:   
    print("not a leap year")
#fibonacci series
n=int(input("enter the number of terms: "))
term1,term2=0,1
for i in range(n):
    print(term1, end=" ")
    term1,term2=term2,term1+term2
#calculator with match case
print("Calculator.")

num1= float(input("enter the number: "))
num2= float(input("enter the number: "))

print("A= Addition.")
print("B= Division.")
print("C= Multiplication.")
print("D= Substraction.")

c=input("enter choice: ")

match c:

  case "A":
    print(num1+num2)
  case "B":
    while True:
            try:
                result = num1 / num2
                print("Result:", result)
                break
            except ZeroDivisionError:
                print("Cannot divide by zero.")
                num2 = float(input("Enter a non-zero second number: "))
  case "C":
    print(num1*num2)
  case "D":
    print(num1-num2)
  case _:
    print("invalid")
#calculator with if else
print("Calculator.")

num1= float(input("enter the number: "))
num2= float(input("enter the number: "))

print("A= Addition.")
print("B= Division.")
print("C= Multiplication.")
print("D= Substraction.")

c=input("enter choice: ")

if c == "A":
    print("Result:", num1 + num2)

elif c == "B":
    while True:
        try:
            result = num1 / num2
            print("Result:", result)
            break
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            num2 = float(input("Enter a non-zero second number: "))

elif c == "C":
    print("Result:", num1 * num2)

elif c == "D":
    print("Result:", num1 - num2)

else:
    print("Invalid choice.")
#anagram with sort
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
#resursive function for exponential
def power(base, exponent):
  if exponent ==0:
    return 1
  elif exponent <0:
    return 1/power (base, -exponent)
  else:
    return base*power(base, exponent -1)
base= float(input("enter the base: "))
exponent= int(input("enter the exponent: "))
result= power(base, exponent)
print(f"{base} ^ {exponent} : {result}")
