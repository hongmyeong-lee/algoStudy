#https://www.acmicpc.net/problem/1931
import sys

input = sys.stdin.readline
#방법 1

T = int(input())
a = []
b = []
timechk = []
for i in range(T):
    [a, b] = map(int,input().split())
    timechk.append([a,b])

timechk = sorted(timechk, key = lambda x: (x[1],x[0]))

pre_chk = timechk[0][1]
count = 1
for i in timechk[1:]:
    if pre_chk <= i[0]:
        count = count +1 
        pre_chk = i[1]

print(count)

#방법2 퀵소트로 풀어봤는데 메모리 초과가 떠버림..
'''
T = int(input())
a = []
b = []
timechk = []

def quick_sort(a):  #퀵소트
    n = len(a)
    if n <=1:
        return a
    
    pivot = a[-1] #pivot 값 임시 지정
    s1 = []
    s2 = []

    for i in range(0, n-1):
        if a[i]<pivot:
            s1.append(a[i])
        else:
            s2.append(a[i])

    return quick_sort(s1)+[pivot]+quick_sort(s2)


for i in range(T):
    [a, b] = map(int,input().split())
    timechk.append([b,a])   #끝나는 시간 기준으로 sort 하고 싶기 때문

timechk = quick_sort(timechk)

for i in range(len(timechk)):
    timechk[i][0] , timechk[i][1] = timechk[i][1] , timechk[i][0] #시작시간, 끝나는 시간 원복

pre_chk = timechk[0][1]
count = 1
for i in timechk[1:]:
    if pre_chk <= i[0]:
        count = count +1 
        pre_chk = i[1]

print(count)


'''

