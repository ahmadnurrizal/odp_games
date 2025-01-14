
def a():
    """
    Buatlah fungsi Python yang mengonversi angka menjadi format teks
    bahasa Indonesia untuk angka 1 hingga 999999999


    MASUKAN
    n= 345

    KELUARAN
    Tiga ratus empat puluh lima
    """

    try:
        n = int(input("Enter Number: "))
        def number_to_text(n):
            digit_1 = ["", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", "Delapan", "Sembilan"]
            digit_2 = ["Sepuluh", "Sebelas", "Dua belas", "Tiga belas", "Empat belas", "Lima belas", "Enam belas", "Tujuh belas", "Delapan belas", "Sembilan belas"]
            digit_3 = ["", "", "Dua puluh", "Tiga puluh", "Empat puluh", "Lima puluh", "Enam puluh", "Tujuh puluh", "Delapan puluh", "Sembilan puluh"]

            if n >= 1000000000:
                return "Maaf Melebihi batas digit 999999999 atau 9 digit"
            elif n >= 1000000:
                juta = number_to_text(n // 1000000) + " juta"
                sisa = number_to_text(n % 1000000)
                return juta + (" " + sisa if sisa else "")
            elif n >= 1000:
                ribu = "Seribu" if n // 1000 == 1 else number_to_text(n // 1000) + " ribu"
                sisa = number_to_text(n % 1000)
                return ribu + (" " + sisa if sisa else "")
            elif n >= 100:
                ratus = "Seratus" if n // 100 == 1 else number_to_text(n // 100) + " ratus"
                sisa = number_to_text(n % 100)
                return ratus + (" " + sisa if sisa else "")
            elif n >= 20:
                puluh = digit_3[n // 10]
                sisa = digit_1[n % 10]
                return puluh + (" " + sisa if sisa else "")
            elif n >= 10:
                return digit_2[n - 10]
            else:
                return digit_1[n]
        
        print(number_to_text(n))

    except ValueError:
        print("Mohon maaf, permainan A belum tersedia!")


a()


