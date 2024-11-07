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

# Kelas turunan pertama BasicUser
class BasicUser(User):
    def viewProduct(self, productId):
        print(f"Menampilkan informasi produk dengan ID: {productId}")

    def addToCart(self, productId, quantity):
        print(f"Menambahkan produk dengan ID: {productId} sebanyak {quantity} ke keranjang.")

# Kelas turunan kedua dari BasicUser, yaitu PremiumUser
class PremiumUser(BasicUser):
    def applyVoucher(self, voucherCode, cartTotal):
        print(f"Menggunakan voucher {voucherCode} pada total keranjang {cartTotal}")

    def requestPrioritySupport(self, issueDescription):
        print(f"Meminta dukungan prioritas untuk masalah: {issueDescription}")

# Contoh penggunaan kelas-kelas di atas
# Membuat objek PremiumUser
premium_user = PremiumUser("Rarasybila", "Rarasyabila@example.com", "111224")

# Menggunakan metode yang ada di kelas User
premium_user.login("Rarasybila", "Rarasyabila@example.com")
premium_user.logout()

# Menggunakan metode dari BasicUser
premium_user.viewProduct("P001")
premium_user.addToCart("P001", 2)

# Menggunakan metode dari PremiumUser
premium_user.applyVoucher("VOUCHER50", 100000)
premium_user.requestPrioritySupport("Produk tidak dapat ditambahkan ke keranjang.")