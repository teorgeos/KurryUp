import random

x = random.randint(1, 100)
y = random.randint(1, 100)
print("x=" x, "y=", y)
answer = int(input("x + y ="))
while answer != (x+y):
    print("정답이 아닙니다. 다시 풀어보세요.")
    answer = int(input("x + y ="))
print("정답입니다.")
