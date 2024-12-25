SELECT 
    t.id_transaksi AS "ID Transaksi",
    p.nama_pelanggan AS "Nama Pelanggan",
    pr.nama_produk AS "Nama Produk",
    dt.jumlah AS "Jumlah",
    dt.subtotal AS "Subtotal",
    t.total_harga AS "Total Harga",
    t.tanggal_transaksi AS "Tanggal Transaksi"
FROM transaksi t
JOIN pelanggan p ON t.id_pelanggan = p.id_pelanggan
JOIN detail_transaksi dt ON t.id_transaksi = dt.id_transaksi
JOIN produk pr ON dt.id_produk = pr.id_produk;
