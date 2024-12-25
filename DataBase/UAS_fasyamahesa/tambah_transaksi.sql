DELIMITER //
CREATE PROCEDURE tambah_transaksi(
    IN id_pel INT, 
    IN total DECIMAL(10,2), 
    IN tanggal DATE
)
BEGIN
    INSERT INTO transaksi (id_pelanggan, total_harga, tanggal_transaksi)
    VALUES (id_pel, total, tanggal);
END //
DELIMITER ;
