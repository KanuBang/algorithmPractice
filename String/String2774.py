str1 = input()
listStr = list(str1)
target = ''
changedStr =[]
for i in listStr:
    comp = ord(i)
    if 65 <= comp and comp <= 90:
        target = i.lower()
    else:
        target = i.upper()
    changedStr.append(target)

print("".join(changedStr))