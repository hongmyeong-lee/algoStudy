# https://www.acmicpc.net/problem/15652
# 문제 : N과 M(3) - 아래 조건 만족하는 M개의 수열 출력
# 조건 : (1) 1부터 N까지 자연수 중에서 M개를 고른 수열 
#        (2) 같은 수를 여러 번 골라도 된다.
#        (3) 고른 수열은 비내림차순이어야 한다. (길이가 K인 수열 A가 A1<A2<A3를 만족) 

def dfs(index,start,N,M):
    if index == M:
        print(' '.join(map(str,result)))
    else:
        for i in range(start,N+1):
            result[index] = i
            dfs(index+1,i,N,M)

def solve():
    global result
    
    N,M = map(int,input().split())
    result = [0]*M
    
    dfs(0,1,N,M)
    
if __name__ == '__main__':
    solve()