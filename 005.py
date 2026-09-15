import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m # 같은 나머지의 인덱스를 카운트, C에는 나머지 m=3일 때 기준 0, 1, 2가 들어간다.
answer = 0

S[0] = A[0] # 합배열의 0번째 값 = 원본 배열의 0번째 값
for i in range(1, n):
  S[i] = S[i-1] + A[i] # 합 배열 만들기

for i in range(n):
  remainder = S[i] % m 
  if remainder == 0:
    answer += 1   # remainder = 0 이면 처음부터 그 구간까지가 m으로 나누었을때 나누어 떨어짐
  C[remainder] += 1 # m으로 나눴을 때 0이 몇개, 1이 몇개, 2가 몇개인지 저장

for i in range(m):
  if C[i] > 1:
    answer += (C[i] * (C[i]-1) // 2) # 조합 사용 ex) 3C2 = 3*2 / 2*1
    # / 사용시 float으로 반환되기 때문에 // 사용

print(answer)