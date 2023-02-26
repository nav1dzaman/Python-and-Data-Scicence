d = {'fish': 'rui', 'animal': 'bandor'}
print(d['fish'])
d['chagol'] = 'ami'

for animal, name in d.items():
    print(animal, "has ", name)

print('fish' in d)

for idx, a in enumerate(d):
    print(idx, " ", a)

for s in range(0, 4):
    print(69)


doc = []


doc.append(('a', 'b', 'c'))  # tupling in the dictionary
