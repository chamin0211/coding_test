# 현재 값보다 오른쪽에 있는 큰 값 중에서 가장 왼쪽에 위치한 값을 구하기
# 앞부분에서 큰 값이 있고 뒤쪽에 이 값보다 큰 값이 없으면 1,000,000개를 계속 찾게됨 = 런타임 에러 발생

# 알고리즘: 선택된 값이 왼쪽에 있는 값의 오큰수가 될 수 있는지 확인하기
# 위의 내용대로만 하면 여전히 런타임 오류 발생 -> 스택을 사용

# ex) 3 5 2 7 이 들어갔다고 치면 스택에 값이 아닌 인덱스를 넣음
# -> 5이 3보다 크기 때문에 인덱스 1을 스택에 넣고 0은 빼버림
# -> 2는 5보다 작기 때문에 스택에 인덱스를 넣기만함
# -> 7은 2보다도 크고 5보다도 크기 때문에 스택에 인덱스를 넣고 7로 결과를 채워줌(5 7 7), 5와 2의 인덱스는 pop해버림
n = int(input())
ans = [0] * n
A = list(map(int, input().split()))
myStack = []

for i in range(n):
  while myStack and A[myStack[-1]] <A[i]: # 오큰수 조건
    ans[myStack.pop()] = A[i] # 정답 리스트에 오큰수 저장
  myStack.append(i)

while myStack:
  ans[myStack.pop()] = -1

result = ""
for i in range(n):
  result += str(ans[i])+" "

print(result)