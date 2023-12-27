n = int(input())

arr = list(input().split())

ch=""

for i in arr:
    ch += i

for i in range(0,len(ch),5):
    print(ch[i:i+5])