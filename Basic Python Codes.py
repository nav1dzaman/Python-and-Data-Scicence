# looping

for s in range(0, 4):  # number of element written in 2nd
    print(69)

# lis=[]_dict={}

print("Hello world")
a = "navid"
s = "my name is {} "
x = s.format(a)
print(x)

xx = "my name is {}".format(a)
print(xx)

boi = a.replace('v', 'Hello')
print(boi)
# __listing
nav = [1, 2, 'navid']
print(nav)
print(nav, nav[0])
nav.append(45.6)
nav[1] = 'zaman'
nav.pop()
print(nav)

nums = list(range(2, 11))
print(nums)

nums[1:3] = [3, 5]
print(nums)
c = 0
for num in nums:
    print(c, 'found')
    c += 1

doc = list(range(1, 10001))

my = [x for x in doc if x % 2 == 0]
print(my)

t = True  # boolean in python

# dictionary kind og map in c++

d = {'fish': 'rui', 'animal': 'bandor'}
print(d['fish'])
d['chagol'] = 'ami'

for animal, name in d.items():
    print(animal, "has ", name)

print('fish' in d)

for idx, a in enumerate(d):
    print(idx, " ", a)


dict = {}

for s in range(2):
    x = input()
    y = input()
    dict[x] = y

print(dict)

# dictuonary endss

dick = {(x, x+1): x for x in range(10)}
t = (1, 2)
print(dick[(1, 2)])

print("fuck")
