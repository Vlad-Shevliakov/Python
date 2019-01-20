import pprint
text = input('Enter your text: ')
count = {}
for char in text:
    count.setdefault(char, 0)
    count[char] = count[char] + 1


print(pprint.pprint(count))