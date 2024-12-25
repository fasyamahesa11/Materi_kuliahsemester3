CREATE TABLE transaksi_1nf (
    id_transaksi INT,
    nama_pelanggan VARCHAR(100),
    kontak_pelanggan VARCHAR(15),
    produk VARCHAR(100),
    jumlah INT,
    harga_produk DECIMAL(10,2),
    tanggal_transaksi DATE
);

INSERT INTO transaksi_1nf VALUES
(1, 'John Doe', '081234567890', 'Kaos Polos', 2, 75000, '2024-12-25'),
(1, 'John Doe', '081234567890', 'Jaket Denim', 1, 250000, '2024-12-25'),
(2, 'Jane Smith', '089876543210', 'Celana Jeans', 1, 300000, '2024-12-24');
