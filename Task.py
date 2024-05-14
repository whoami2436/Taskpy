import random
import time

def Coders():
    randnum = random.randint(1, 40)
    shans = 6

    print("1-40 arasında bir nomre seçildi. Bu nomreni tapmaga calisin!")
    time.sleep(2)

    while shans > 0:
        guess = int(input("Texmininizi girin (1-40 arası bir sayı): "))
        time.sleep(2)

        if guess < randnum:
            print("Duzgun deyil, random nomre daha boyükdür.")
        elif guess > randnum:
            print("Duzgun deyil, random nomre daha kicikdir.")
        else:
            print("Tebrikler! Duzgun cavab:", randnum)
            return

        shans -= 1
        if shans > 0:
            print(shans, "shansiniz qaldı.")
            time.sleep(1)
        else:
            print("shansiniz qalmadı. Duzgun cavab:", randnum, "Game over")
            return

if __name__ == "__main__":
    Coders()
