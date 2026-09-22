# N이 12고 L이 3일 때 A(i-2) ~ A(i) 이므로 A(i-2), A(i-1), A(i) 이렇게 3개가 들어가게 됨
# 즉 L의 값만큼의 범위 내에서 최솟값 D(i)를 구하는 문제임
# 시간복잡도에서 문제가 발생하기 때문에 상당히 어려운 문제임


# 최소값 가능성 없는 데이터 삭제 
# --> 가장 마지막에 들어온 값이랑 이전 값들 비교 후 이전 값들 중 마지막 값보다 작거나 같은 값은 삭제
# window 크기 밖 데이터 삭제
# --> 마지막 인덱스 - L 의 값과 같거나 작은 인덱스는 삭제

from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
mydeque = deque();
now = list(map(int, input().split()))

for i in range(N):
  # 아이디어1. 나보다 큰 데이터 삭제하기
  # 제일 끝에 있는 값이 현재 있는 값보다 크면 pop 해줌
  while mydeque and mydeque[-1][0] > now[i]:
    mydeque.pop()
  mydeque.append((now[i], i))
  # 제일 앞에 있는 인덱스가 i-L(윈도우 범위)보다 작거나 같으면 pop 해줌
  if mydeque[0][1] <= i - L:
    mydeque.popleft()
  # 가장 앞에 있는 값이 최소값이기 때문에 앞에 있는 값을 출력함
  print(mydeque[0][0], end=' ')