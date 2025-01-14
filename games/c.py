
def c():
    """
    Buat program untuk memeriksa apakah sebuah angka merupakan bilangan Armstrong.
    Bilangan Armstrong adalah angka yang sama dengan jumlah pangkat 𝑛-nya, di mana 𝑛 adalah jumlah digit angka tersebut.

    MASUKAN
    n = 153

    KELUARAN
    153 adalah bilangan Armstrong
    """
    
    input_number = int(input("Enter a number: "))

    order = len(str(input_number))

    # initialize sum
    sum = 0

    # find the sum of the cube of each digit
    temp = input_number
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    # display the result
    if input_number == sum:
        print(input_number,"is an Armstrong number")
    else:
        print(input_number,"is not an Armstrong number")


    # write the code solution here
    # print("Mohon maaf, permainan C belum tersedia!")
