# menampilkan stok barang yang jumlahnya
# sudah dibawah rata rata 
SELECT nama_barang, stok FROM tbl_barang
WHERE stok <
(SELECT AVG(stok) FROM tbl_barang WHERE)