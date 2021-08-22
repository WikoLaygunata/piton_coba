import random

persen = ["-1000%", "0%", "30%", "70%", "1000%"]

while True:
    print("Tes seberapa kerenkah anda\n")
    nama = input("Masukkan nama anda = ")
    persentase = random.choice(persen)
    
    if nama = "wiko":
        persentase = "1000%"
    
    print(f"\nPersentase keren anda adalah {persentase}!")
    
    if persentase == "-1000%":
        print(f"Anda/{nama} sangat sangat tidak keren.")
    elif persentase == "0%":
        print(f"Anda/{nama} tidak keren.")
    elif persentase == "30%":
        print(f"Anda/{nama} sedikit keren.")
    elif persentase == "70%":
        print(f"Anda/{nama} lumayan keren.")
    else:
        print(f"Anda/{nama} sangat sangat keren!")
    cobalagi = input("\ncoba lagi? (ya/tidak) = ")
    if cobalagi.lower() != "ya":
        break
