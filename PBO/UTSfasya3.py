# Kelas-kelas yang sudah didefinisikan sebelumnya (User, BasicUser, PremiumUser, Seller, Admin) diasumsikan sudah ada

# Membuat objek PremiumUser
premium_user = PremiumUser("Buddy-Anduk", "buddy22@example.com", 101)

# Menggunakan metode pada objek PremiumUser
premium_user.viewProduct("P002")
premium_user.addToCart("P002", 1)
premium_user.applyVoucher("DISCOUNT10", 50000)
premium_user.requestPrioritySupport("Tidak bisa checkout pesanan.")

# Membuat objek Seller
seller = Seller("sellerPro", "seller@example.com", 202)

# Menggunakan metode pada objek Seller
seller.addProduct("Smartphone", "Smartphone terbaru dengan kamera 64MP", 7000000, 15)
seller.processOrder("ORD002", "dalam pengiriman")