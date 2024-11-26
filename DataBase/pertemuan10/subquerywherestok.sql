SELECT * FROM tbl_barang WHERE stok >
(SELECT MAX(tbl_barang) FROM tbl_detailtransaksi)
