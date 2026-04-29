# if/else 
age = 12
if age >= 18:
    print("Adult")
else:
    print("Minor")

# elif
a = 33
b = 33
if a > b:
    print("A is greater then B")
elif a==b:
    print("A and B are equal")

# short hand if
a = 7
b = 8
if b > a : print("True")

# And operators    if both conditions are true
a = 200
b = 300
c = 100
if a<b and a>c:
    print("A is lesser then B but greater then C")

# OR operator     if one of the cionditions are true
a = 200
b = 300
c = 100
if a==b or a>c:
    print( " A greater then C")

# Not operators   reverse the result
a = 200
b = 300
if not a > b:
    print("A is not greater then b")

# problem example
age = 20
if age <=13:
    print("Child")
elif age>13 and age < 18:
    print("Teenager")
else:
    print("Adult")


# Loops and iterations 
# for loop
fruits = ["Apple" ,"Banana" , "Cherry"]
for x in fruits:
    print(x)
    if x=="Banana":
        break


# Example Qustion
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


# nested for loop
adj=["Red","big","tasty"]
fruits= ["Apple", "Banana", "cherry"]
for x in adj:
   for y in fruits:
      print(x , y)


# Example problem
fruits = ["Apple" , "Banana","Cherry"]
for x in fruits:
    print (x)
    if x == "Banana":
        break


# While loops 
i = 1
while i < 6:
    print(i)
    i +=1

# break
i = 1
while i < 6:
    print(i)
    if i == 4:
        break
    i+=1
    
# continous
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Example problem
i = 0
while i < 6:
    i = i+1
    if i ==3:
        continue
    print(i)

# Example problem    Multiplication Table
num = int(input("Enter a Number"))
for x in range(1 , 11):
    print(num , "x" , x , "=" , num*x)

# Mini Quiz
num = int(input("Enter any Number"))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 ==0:
    print("Buzz")
else:
    print("Not divisble by 3 and 5")