# This is a comment
# Python doesn't read
# what goes here.
# Only for Humans!

# prints hello world
print("Hello World!")

answer = input("What is your name?")
print("Hello", answer+"!")

i = -1
while True:
    i += 1

    if(i > 20):
        break

    # i is odd
    if(i % 2 != 0):
        continue

    print(i)
