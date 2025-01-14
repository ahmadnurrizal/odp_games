def b():
    """
    Diberikan sebuah list angka, cari pasangan angka dengan selisih terkecil.

    MASUKAN
    data = [4, 8, 15, 16, 23, 42] 

    KELUARAN
    15 16
    """
    # Input dari user
    data = input("Masukkan angka-angka dipisahkan dengan spasi: ")
    
    # Convert ke list
    data = list(map(int, data.split()))

    # Urutkan data
    data.sort()

    # Inisiasi
    min_diff = float('inf')
    num_pair = []

    # Cari pasangan angka dengan selisih terkecil
    for i in range(len(data) - 1):
        diff = data[i + 1] - data[i]
        if diff < min_diff:
            min_diff = diff
            num_pair = [data[i], data[i + 1]]
    
    # Print hasil
    print(num_pair[0], num_pair[1])
