# isinya cuma nama, hobi, sama deskripsi atau bahkan lebih ke arah curhat soal dunia program daripada deskripsi haha
# coba langsung copas ini ke editor untuk experience maximal. btw aku pake pycharm utk editor python

deskripsi = ["hai, aku wiko laygunata. gabut jadi ngetik gini, lebih ke curhat sih daripada sebutan deskripsi hahaha "
             "kykny udh pda kenal jd gaperlu la ya kenalan kenalan, coba aja itu ada sedikit di fase tebak tebakan. "
             "kenapa si bikin ginian? hm buat seru seruan aja sih ibarat kalau kalian ingin belajar sesuatu mesti "
             "perlu cari sisi serunya dulukan biar semangat. jujur agak aneh kalau kalian liat ini cuma lewat github, "
             "soalnya ga sistematis gitu, dan ga sesuai eksekusi eksekusi yg ada. kalau kalian ngerti sih okay, tapi "
             "kalau belum pasti bakal bingung atau sekedar baca teks stringnya aja hahaha. jadi aku harap kalian copas "
             "ini ke editor baru kalian eksekusi okehh?!. kalau kalian baru, sperti yg aku tau sblmny dan udh aku "
             "rasakan sekarang, coding ini bukan ngetik ngetik aja tapi 70% waktu dipake buat mikir hahahaha. knp aku "
             "coba python sebelum yg lain? hmmm awalnya katanya(google) python bagus untuk pemula sih terutama aku "
             "punya impian di bidang software development. mungkin setelah aku pelajari secara lebih menyeluruh ini "
             "python, aku bakal mulai belajar java. kenapa ga javascript? aku merasa terlalu mainstream la haha. kalau "
             "orang kebanyakan mungkin belajar web development aja udah puas, apalagi krn aku suka beda, jadi pengen "
             "cemplung lebih dalam ke dalam software aja. jujur aku ada ide proyek besar untuk indonesia. tepatnya "
             "untuk naikin sumber daya manusia indo haha, bkn utk cari uang :p. tapi sial 8 tahun lagi lama coox. "
             "btw kopi susu itu benar benar favorit, walau aku ada maag haha. very good present for me lah"]

while True:
    print("Halo, aku Wiko baru belajar")
    print("iseng iseng bikin gini basic aj gatau mau bikin projek gimana\n")
    print("mau aku coba tebak tebak simpel dulu atau lgsg aja deskripsi about me?")
    mulai = input("Ketik 1 jika tebak tebakan, ketik 2 jika deskripsi = ")
    if mulai == "1":

        print("\nokayy, let's start")
        nama = input("pertama, siapa nama panjang aku (huruf kecil)= ")
        if nama == "wiko laygunata":
            print("Wew benar, hahaha pasti udah tau sihh, okey next\n")
        else:
            print("hmmm, belum benar tuh. Jawabannya wiko laygunata ya,next.\n")

        hobi = input("yg mana hobi aku? (bacakomik/belajar)= ")
        if hobi == "bacakomik":
            print("yap benar, baca komik seru pisan tapi tergantung yg dibaca jg sih\n")
        elif hobi == "belajar":
            print("hah belajar? orang elite dari bangsawan mana itu, hahaha. baca komik dong\n")
        else:
            print("milih oy bkn nebak yg laen. tapi kadang main basket atau ml uga si, tapi fav msih baca komik la\n")

        ultah = input("tebak tanggal brp aku ultah (aku rasa ini terlalu sulit dan emg diharuskan salah hahaha) = ")
        if ultah == "25 agustus":
            print("wew, brarti kalian udah kenal aku lama atau mungkin anda stalker.. :o ")
        else:
            print("yup aku ga harep benar krn emg siapa yg bisa nebak njir, tapi jwbnnya 25 agustus.")

        print("bingung mau coba tanya apalagi, main lagi lalu ketik 2 kalau mau coba bagian deskripsi :p\n")

    if mulai == "2":
        print("", deskripsi)
        print("kalau belum coba fase tebak tebakan, coba dulu deh biar lengkap\n")

    cobalagi = input("okey udh selesai, mau coba ulang? (ya/tidak)= ")
    if cobalagi.lower() != "ya":
        break
