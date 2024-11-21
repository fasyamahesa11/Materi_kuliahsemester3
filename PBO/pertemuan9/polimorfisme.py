# tampa implementasi polimorfisme
class jumlah:
    def tambah1(n1, n2):
        print(f"hasilnya {n1+n2}")
objek3 = jumlah
objek3.tambah1(1,2) #menghasilkan error karena jumlah parameter strict wajib 2

# implementasi polimorfisme
class penjumlahan:
    def tambah(*num):
        return sum(num)
objek1 = penjumlahan
print(objek1.tambah(2,3,5,10))

# menggunakan default parameter
class default:
    def tambah2( a, b=0,c=0,d=0,e=0):
        print (f"hasilnya {a+b+c+d+e}")
objek2 = default
objek2.tambah2(2,4,2)