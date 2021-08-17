import random

while True:
    anda = input("Pilih (Batu, Gunting, Kertas) : ")
    pilihanbot = ["Batu", "Gunting", "Kertas"]
    computer = random.choice(pilihanbot)
    print(f"\nAnda pilih {anda}, bot pilih {computer}.\n")

    if anda == computer:
        print(f"Anda dan computer memilih {anda}, Hasilnya seri bos!")
    elif anda == "Batu":
        if computer == "Gunting":
            print("Anjay anda menang!")
        else:
            print("Aowkowkwkwo cupu kalah lawan bot.")
    elif anda == "Gunting":
        if computer == "Kertas":
            print("Anjay anda menang!")
        else:
            print("Aowkowkwkwo cupu kalah lawan bot.")
    elif anda == "Kertas":
        if computer == "Batu":
            print("Anjay anda menang!")
        else:
            print("Aowkowkwkwo cupu kalah lawan bot.")
    main_lagi = input("Main lagi? (ya/tidak) = ")
    if main_lagi.lower() != "ya":
        break
