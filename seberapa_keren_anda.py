import random

persen = ["-1000%", "0%", "30%", "70%", "1000%"]

while True:
    print("Tes seberapa kerenkah anda\n")
    nama = input("Masukkan nama anda = ")
    persentase = random.choice(persen)
    
   #hahahaha ini lucu sih aku baru tau bisa gini, lumayan curang tapi seru. (selain nama yg aku if sendiri hasilnya bakal random yah)
   #aku coba ini agak kampret supaya agak konsisten nama dgn persennya, mungkin butuh database tapi aku blm tau dan ribet. (setelah 1x gacha di nama itu hasilny bakal permanen)
    if nama == "wiko":
        persentase = "1000%"
    if nama == "clara":
        persentase = "1000000000%"
    if nama == "jesslyn":
        persentase = "-1000%"
    
    print(f"\nPersentase keren anda adalah {persentase}!")
    
    if persentase == "-1000%":
        print(f"Anda/{nama} sangat sangat tidak keren.")
    elif persentase == "0%":
        print(f"Anda/{nama} tidak keren.")
    elif persentase == "30%":
        print(f"Anda/{nama} sedikit keren.")
    elif persentase == "70%":
        print(f"Anda/{nama} lumayan keren.")
    elif persentase == "1000000000%":
        print(f"Anda/{nama} Terlalu OP, persennya kebanyakan woi")
    else:
        print(f"Anda/{nama} sangat sangat keren!")
    cobalagi = input("\ncoba lagi? (ya/tidak) = ")
    if cobalagi.lower() != "ya":
        break
