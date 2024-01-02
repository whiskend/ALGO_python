case = 0
candy = int(input())

candy+=1
for A in range (candy):
    for B in range (candy):
        for C in range(candy):
            if A+B+C == 6:
                if A >= B+2:
                    if A>0 and B>0 and C>0:
                        if C % 2 == 0:
                            case += 1

print(case)