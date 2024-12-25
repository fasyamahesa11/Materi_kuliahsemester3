DELIMITER //
CREATE EVENT hapus_transaksi_lama
ON SCHEDULE EVERY 1 DAY
DO
DELETE FROM transaksi WHERE tanggal_transaksi < CURDATE() - INTERVAL 30 DAY;
//
DELIMITER ;
