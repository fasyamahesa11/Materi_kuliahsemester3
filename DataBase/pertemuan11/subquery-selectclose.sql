# menapilkan total jumlah barang yang suda 
# dilakukan pengadaan
SELECT kode_barang,
(SELECT SUM(jumlah) AS jumlah_brg,
FROM tbl_detail_pengadaan
WHERE
tbl_detail_pengadaan.kode_barang =
tbl_barang.kode_barang) AS  jml_pengadaan
FROM tbl_barang;