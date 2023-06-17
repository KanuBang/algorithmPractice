import sys
input = sys.stdin.readline

myDict = {"Paper":57.99, "Printer":120.50, "Planners":31.25, "Binders":22.50, "Calendar":10.95, "Notebooks": 11.20, "Ink":66.95}
sum = 0
s = ""

while True:
    s = input().rstrip()
    if s == "EOI":
        break
    sum += myDict[s]

print("$"+str(sum))