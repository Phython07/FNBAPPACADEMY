#Control Statements

num = -5

if num > 0:
    print("this number is positive")
elif num ==0:
    print("this number is zero")
else:
    print("this number is negative")

#LoopControlStatement

fruits =["apple","banana","cherry","date"]

for fruit in fruits:
    if fruit == "cherry":
        continue #Skips cherry and moves to the next iteration
    print(fruit)

print()

for fruit in fruits:
    if fruit == "cherry":
        pass #Placeholder, no action is needed for cherry
    print(fruit)

count = 0   

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break #Exits the loop when the count is reached

 
