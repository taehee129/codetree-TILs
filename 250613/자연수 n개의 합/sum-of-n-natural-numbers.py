MAX_S = 2*10**9

s = int(input())

left = 1                             # 가장 작은 숫자 값을 설정합니다.
right = MAX_S                        # 가장 큰 숫자 값을 설정합니다.
max_num = 0                          # 최대이므로, 답이 될 수 있는 값보다 더 작은 값으로 설정합니다.

while left <= right:                 # [left, right]가 유효한 구간이면 계속 수행합니다.
    mid = (left + right) // 2        # 가운데 위치를 선택합니다.
    if mid * (mid + 1) // 2 <= s:    # 1부터 n까지의 합이 s보다 같거나 작다면
        left = mid + 1               # 오른쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 left를 바꿔줍니다.
        max_num = max(max_num, mid)  # 답의 후보들 중 최댓값을 계속 갱신해줍니다.
    else:
        right = mid - 1              # s보다 큰 경우라면 right를 바꿔줍니다.

print(max_num)   