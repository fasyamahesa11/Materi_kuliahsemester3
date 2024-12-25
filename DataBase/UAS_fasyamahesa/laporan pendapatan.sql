CREATE VIEW laporan_pendapatan AS
SELECT 
    t.id_transaksi, 
    p.nama_pelanggan, 
    t.total_harga, 
    t.tanggal_transaksi
FROM transaksi t
JOIN pelanggan p ON t.id_pelanggan = p.id_pelanggan;
