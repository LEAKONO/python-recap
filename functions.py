##FUNCTIONS
def greetings(name):
    return (f"Hello {name} welcome to my first python function after a very longtime")
print(greetings("JOHN"))
def Checking(number):
    if number==4:
        print("its 4 guys")
    elif number==5:
        print("I knew it people")
    else:
        print("Its just a random number who even cares")
Checking(4)
Checking(5)
Checking(14)


def add(a, b):
    return a + b

result = add(3, 5)
print(result)  

for num in range(1,5):
    print(num)

for num in range(5):
    if num == 3:
        break     # exit the loop
    print(num)

for num in range(5):
    if num == 3:
        continue   # skip 3
    print(num)
i=0
while i<4:
    print(f"I love you  python")
    i+=1


