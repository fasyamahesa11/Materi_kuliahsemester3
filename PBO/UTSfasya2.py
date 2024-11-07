# Kelas dasar User
class User:
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId

    def login(self, username, email):
        if self.username == username and self.email == email:
            print(f"Pengguna {self.username} berhasil login.")
        else:
            print("Login gagal.")

    def logout(self):
        print(f"Pengguna {self.username} berhasil logout.")

# Kelas turunan pertama Seller
class Seller(User):
    def addProduct(self, productName, description, price, stock):
        print(f"Menambahkan produk baru: {productName}")
        print(f"Deskripsi: {description}, Harga: {price}, Stok Awal: {stock}")

    def processOrder(self, orderId, status):
        print(f"Memproses pesanan ID: {orderId} dengan status: {status}")

# Kelas turunan kedua Admin
class Admin(User):
    def removeUser(self, userId):
        print(f"Menghapus akun pengguna dengan ID: {userId}")

    def generateReport(self, reportType, startDate, endDate):
        print(f"Menghasilkan laporan {reportType} dari tanggal {startDate} hingga {endDate}")

# Contoh penggunaan kelas-kelas di atas
# Membuat objek Seller
seller = Seller("alice_seller", "alice@example.com", "seller123")
seller.login("alice_seller", "alice@example.com")
seller.addProduct("Laptop", "Laptop gaming dengan RAM 16GB", 15000000, 10)
seller.processOrder("ORD001", "dalam pengiriman")
seller.logout()

# Membuat objek Admin
admin = Admin("bob_admin", "bob@example.com", "admin001")
admin.login("bob_admin", "bob@example.com")
admin.removeUser("user123")
admin.generateReport("transaksi", "2024-01-01", "2024-12-31")
admin.logout()