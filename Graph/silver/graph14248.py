import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().split())
v = [False] * (n+1)
bridge = list(map(int, input().split()))
s= int(input().rstrip())
cnt = 1

