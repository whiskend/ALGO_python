# hint의 갯수 입력 받기
n = int(input())

# hint 입력
# [[123, 1, 1], [356, 1, 0], ... ]
hint = [list(map(int, input().split())) for _ in range(4)]

for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            if (a==b or a==c or c==b):
                continue

            cnt = 0
            for arr in hint:
                number = hint[0]
                ball = hint[1]
                strike = hint[2]

                # {abc와 number를 자릿수를 나눠서 비교해서 strike ball을 측정한다}

                ball_count = 0
                strike_count = 0

                if ball == ball_count and strike == strike_count:
                    cnt += 1

            if cnt == n:
                answer += 1
print(answer)