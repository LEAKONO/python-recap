x=4
print(x)
print(type(x))
y="Hello"
print(type(y))

print(y)
z=True
print(z)
print(type(z))

T=4.5
print(type(T))

print(T)
arr=[1,2,3,4,5,6]
print(arr)
print(type(arr))

Tu=(1,2,3,5,6)
print(Tu)
print(type(Tu))

Se={1,5,6,7,8,0}
print(type(Se))

Di={
    "name":"Mercedz",
    "age":12
}
print(type(Di))
print(Di)

#Modify a List
fruits=["Apple","Mango","Pineapple","Orange","Avocado"]
print(fruits)
fruits.append("Tomatoes")
print(fruits)
fruits.insert(3,"Banana")
print(fruits)
fruits.reverse()
print(fruits)
print(fruits.count("Banana"))
fruits.sort()
print(fruits)
print(len(fruits))


##  2. Sets and Its Methods
Num={1,5,6,7,9,19}
Num.add(10)
print(Num)

Num.remove(10)
print(Num)

xy=Num.copy()
print(xy)

Num.update([4,2])
print(Num)
Num.discard(7)
print(Num)
Num.clear()
print(Num)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))   # {1, 2, 3, 4, 5, 6}
print(a | b)        # same result

print(a.intersection(b))  # {3, 4}
print(a & b)              # same result

print(a.difference(b))  # {1, 2}
print(a - b)

a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))  # ✅ True: all items in `a` are in `b`
print(b.issubset(a))  # ❌ False: `b` has more stuff

a = {1, 2, 3, 4}
b = {2, 3}

print(a.issuperset(b))  # ✅ True: `a` has all items in `b`
print(b.issuperset(a))  # ❌ False

x = {1, 2}
y = {2, 3}

print(x.isdisjoint(y))  # ❌ False: they both have 2

##creating Tuples
t1 = (1, 2, 3)
t2 = ("apple", "banana")
t3 = ()               # Empty tuple
t4 = (5,)             # Single element? Comma needed!

print(t1[0])  # 1
print(t1[-1]) # 3

for item in t2:
    print(item)

t = (1, 2, 2, 3, 4)

print(t.count(2))     # How many times 2 appears → 2
print(t.index(3))     

