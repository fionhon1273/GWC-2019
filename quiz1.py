#Number 1
i = 0
for x in range(10):
    if x % 2 != 0:
        i += x
        print(x)
print(i)

#Number 2
def function1():
    answer1 = int(input("Give me a number"))
    answer2 = int(input("Give me another number"))
    print(answer1+answer2)

#Number 3
def greetings():
    print("Hello, world")

greetings()
display = ""
while True:
    i = 0
    i += 1
    if 1 > 10:
        display += "?"
    else:
        display += "@"
print(display)

#NUmber 4
str1 = "fireflies"
str2 = "another"
display = ""
temp = ""
for letter in str1:
    if letter not in str2:
        display += letter
        temp += letter
    else:
        temp += letter
        print(temp)
print(display)

#Number 5
x = 10
y = 15
z = 20
while x > y:
    print(f"x:{x} y:{y}")
    x -= 1
    y += 1
if x > y:
    print("Hello")
else:
    if z > y and z > x:
        print("Wow")
        if y < x:
            print("Yes")
        else:
            print("No")
    else:
        print("Okay")
