import random

num = random.randint(1, 3)
tebak = None

while tebak != num:
    tebak = input("guess a number between 1 and 3: ")
    tebak = int(tebak)

    if tebak == num:
        print("anjay menang")
        break
    else:
        print("cupu kalah, coba lagi")
