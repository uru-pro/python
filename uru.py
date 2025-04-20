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
#factorial
def fac(n):
  if n==1 or n==0:
    return 1
  else:
    return n*fac(n-1)
print(fac(7))
#prime number
#not running
def prime(n):
  if n<2:
    return False
  for i in range(2, int(n**0.5)+1):
    if n%i==0:
      return False
  return True
num =int(input("enter: "))
if prime(num):
  print("prime")
else:
  print("not prime")
#loops
for i in range(1,10):
    print(i)
for r in range(1,10,2):
    print(r)
sub=["hi","hello","bye"]
for ab in sub:
    print(ab)
#nested loop
for i in range(1,4):
  for j in range(1,4):
    print(i,j)
    print(" ")
#loop1
n=5
for i in range(n):
  for j in range(i+1):
    print(chr(97+j), end=" ")
  print()
#loop2
n=5
for i in range(5):
    for j in range(i+1):
        print(" ",end = "")
    for j in range(i,n):
        print("*",end = "")
    print()
#loop3
rows = 7
for i in range(rows, 0, -2):
    print(" " * (rows - i), end="")

    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(3, rows + 1, 2):
    print(" " * (rows - i), end="")

    for j in range(1, i + 1):
        print(j, end=" ")

    print()
#stack
class Stack:
  def __init__(self):
    self.stack=[]
  def push(self,item):
    self.stack.append(item)
  def pop(self):
    return self.stack.pop() if self.stack else none
  def peek(self):
    return self.stack[-1] if self.stack else none
  def is_empty(self):
    return len(self.stack)==0

s=Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())
print(s.pop())
print(s.peek())
print(s.is_empty())
#password
password=" "
while password!="secret":
  password=input("enter the password: ")
print("access granted")
#semester marksheet program
def input_marks(sem):
    print(f"\nEnter marks for Semester {sem} (5 subjects):")
    marks = []
    for i in range(1, 6):
        while True:
            try:
                mark = int(input(f"  Subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("    Please enter marks between 0 and 100.")
            except ValueError:
                print("    Invalid input. Enter a number.")
    return marks

# Simulate switch-case using dictionary
def display_sem_marks(student, sem):
    key = f"Semester {sem}"
    if key in student["marks"]:
        print("\n" + "="*40)
        print(f"      MARKSHEET - {key}")
        print("="*40)
        for i, mark in enumerate(student["marks"][key], 1):
            print(f"  Subject {i}: {mark}")
        print("="*40)
    else:
        print("Invalid semester!")

def display_all_marks(student):
    total_marks = 0
    print("\n" + "="*40)
    print("        COMPLETE MARKSHEET")
    print("="*40)
    for sem, marks in student["marks"].items():
        print(f"\n{sem}:")
        for i, mark in enumerate(marks, 1):
            print(f"  Subject {i}: {mark}")
            total_marks += mark
    percentage = total_marks / (6 * 5)
    print("\n" + "="*40)
    print(f"Total Marks   : {total_marks} / {6 * 5 * 100}")
    print(f"Percentage    : {percentage:.2f}%")
    print("="*40)

# Collect student info
student = {
    "name": input("Enter student name: "),
    "roll_no": input("Enter roll number: "),
    "branch": input("Enter branch: "),
    "marks": {}
}

# Input marks for 6 semesters
for sem in range(1, 7):
    student["marks"][f"Semester {sem}"] = input_marks(sem)

# Menu-driven interface
while True:
    print("\n" + "-"*30)
    print("1. View Semester Marksheet")
    print("2. View Complete Marksheet")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        try:
            sem = int(input("Enter semester number (1-6): "))
            display_sem_marks(student, sem)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "2":
        display_all_marks(student)
    elif choice == "3":
        print("Exiting... Have a nice day!")
        break
    else:
        print("Invalid choice. Please try again.")
#bill generation program
def get_item_details(item_code):
    match item_code:
        case 1:
            return "Pen", 10
        case 2:
            return "Notebook", 50
        case 3:
            return "Pencil", 5
        case 4:
            return "Eraser", 3
        case 5:
            return "Marker", 25
        case _:
            return None, 0

def print_bill(items):
    print(f"\n{'Item':<12}{'Qty':<10}{'Unit Price':<15}{'Total'}")
    print("-" * 50)
    grand_total = 0

    for item_code, quantity in items:
        item_name, price = get_item_details(item_code)
        if item_name:
            total = price * quantity
            grand_total += total
            print(f"{item_name:<12}{quantity:<10}{price:<15}{total}")
        else:
            print(f"Invalid item code: {item_code}")

    print("-" * 50)
    print(f"{'Grand Total':<37}{grand_total}")

# Menu
print("Available Items:")
print("1. Pen      - ₹10")
print("2. Notebook - ₹50")
print("3. Pencil   - ₹5")
print("4. Eraser   - ₹3")
print("5. Marker   - ₹25")

# Input section
items = []

while True:
    try:
        code = int(input("\nEnter item code (or 0 to finish): "))
        if code == 0:
            break
        qty = int(input("Enter quantity: "))
        items.append((code, qty))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

# Print the final bill
if items:
    print_bill(items)
else:
    print("No items entered.")
#end