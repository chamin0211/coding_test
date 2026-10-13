def dfs(x, computers, visited):
  visited[x] = True
  for a, b in enumerate(computers[x]):
    if b == 1 and (not visited[a]):
      dfs(a, computers, visited)
# computers[0] = [1, 1, 0]일 경우 (dfs(0) 시작 시 visited = [T, F, F])
# a=0, b=1 -> b==1 True, not visited[0] False -> 조건 불성립, 패스
# a=1, b=1 -> b==1 True, not visited[1] True  -> 조건 성립, dfs(1) 호출
#             (dfs(1) 첫 줄에서 visited[1] = True)
# a=2, b=0 -> b==1 False -> 뒤는 평가 안 함, 패스 (visited[2]는 False 유지)
def solution(n, computers):
  visited = [False] * n # 컴퓨터 번호 = 인덱스. 처음엔 전부 안 가본 상태
  cnt = 0  # 네트워크(덩어리) 개수

  for i in range(n):   # 0번부터 n-1번까지 전부 확인
    if not visited[i]: # 아직 안 간 컴퓨터 = 새 네트워크의 시작
      dfs(i, computers, visited)  # 닿을 수 있는 컴퓨터를 전부 방문 처리
      cnt += 1  # 덩어리 하나 끝났으니 +1

  return cnt

# "첫 번째는 visited[0]이 False라서 안으로 들어가 cnt에 1 더하고, 
# visited[2]도 False라서 한 번 더 더해 return이 2. 
# 두 번째는 visited[0]이 False라서 cnt에 1 더하고, 
# dfs가 다 True로 만들기 때문에 return이 1에서 멈춘다."