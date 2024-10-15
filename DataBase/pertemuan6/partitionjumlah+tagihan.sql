SELECT 
	a.kode_faktur, 
	a.kode_barang, 
	b.nama_barang,
	b.harga, 
	a.qty, 
	b.harga * a.qty AS Jumlah_harga
	SUM (tbl_barang.harga * tbl_detailtransaksi.qty) OVER
	(PARTITION BY tbl_detailtransaksi.kode_faktur) AS Jumlah_Tagihan
FROM 
	tbl_detailtransaksi a 
INNER JOIN
	tbl_barang b ON b.kode_barang = a.kode_barang
WHERE 
	a.kode_faktur = "KD_002";