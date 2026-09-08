import sys
input = sys.stdin.readline # 그냥 input()보다 sys.stdin.readline()이 훨신 빠름

# input()으로 한 줄을 문자열로 받고, split()으로 공백 기준 쪼개서 문자열 리스트로 만든 다음,
# map(int, ...)으로 각 원소를 정수로 변환해서 n, m에 순서대로 나눠 담음(.split을 하면 리스트로 담아짐)
n, m = map(int, input().split())

A = [[0] * (n + 1)] # 0번째 행: 전부 0인 더미 행
D = [[0] * (n+1) for _ in range(n + 1)] #  0행0열부터 n행n열의 행렬을 만듦

for i in range(n):
  A_row = [0] + [int(x) for x in input().split()] # 0번째 열은 0으로 고정
  A.append(A_row)

# 1행1열을 따로 구하지 않아됨 -> 0행 0열은 다 0으로 고정되어있기 때문에
# 기존 구간 합 공식과 동일한 방식으로 구할 수 있음

#누적합 = 사각형 전체의 합 -> (0,0)부터 특정 지점까지의 총합
for i in range(1, n+1):
  for j in range(1, n+1):
    D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

#구간합 = 임의의 두 지점 사이의 부분합
for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
  print(result)