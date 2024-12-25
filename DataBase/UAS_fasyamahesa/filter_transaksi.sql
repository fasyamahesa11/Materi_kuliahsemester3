SELECT 
    id_transaksi, total_harga, tanggal_transaksi
FROM transaksi
WHERE total_harga > (SELECT AVG(total_harga) FROM transaksi);
