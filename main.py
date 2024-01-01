# 100만보다 작고 2이상의 약수를 가지고 있다면 NO!

TC = int(input())

for _ in range(TC):
    number = int(input())

    for i in range(2, 1_000_001):
        if number%i == 0:
            print("NO")
            break
        if i == 1_000_000:
            print("YES")