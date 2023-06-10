import sys
input = sys.stdin.readline
gnomes = [list(map(int, input().rstrip().split())) for i in range(int(input().rstrip())) ]
print("Gnomes: ")
for j in [ print("Ordered") if i == sorted(i) or i == list(reversed(sorted(i))) else print("Unordered") for i in gnomes]:
    continue