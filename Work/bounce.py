# bounce.py
#
# Exercise 1.5
bounce = 0
height = 100

while bounce <= 10:
    height = height * (3/5)
    print(1, round(height, 4))
    bounce += 1