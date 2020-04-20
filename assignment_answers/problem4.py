mutsa_scores = [90, 77, 40, 55, 90, 100, 88]

total = 0
for score in mutsa_scores:
    total = total + score

mean = total / 7

# 반올림해서 소수점 2번째 자리까지 표현
print(round(mean, 2))
