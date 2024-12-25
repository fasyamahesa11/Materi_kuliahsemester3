DELIMITER //
CREATE TRIGGER hitung_subtotal
BEFORE INSERT ON detail_transaksi
FOR EACH ROW
BEGIN
    SET NEW.subtotal = NEW.jumlah * (SELECT harga_produk FROM produk WHERE id_produk = NEW.id_produk);
END //
DELIMITER ;
