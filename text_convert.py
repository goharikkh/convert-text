import json

def convertToTitle(columnNumber):
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    x = (columnNumber - 1) % 26
    rest = (columnNumber - 1) // 26

    if rest == 0:
        return digits[x]
    return convertToTitle(rest) + digits[x]



text = open("text", "r")
converted = open("converted", "w")
count = {}
num = 0
for line in text:
    word = line.split(" ")
    for i in word:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

for x in list(count):
    if count[x] == 1:
        del(count[x])

num = 1
for key in count:
    count[key] = convertToTitle(num)
    num += 1

text.seek(0)

for line in text:
    word = line.split(" ")
    for i in word:
        if i in count:
            converted.write(count[i] + ' ')
        else:
            converted.write(i + ' ')
json = json.dumps(count)
f = open("dict.json", "w")
f.write(json)
f.close()