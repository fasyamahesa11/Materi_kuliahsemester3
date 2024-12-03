# ingin insert nama barang berasal dari tbl_barang
# berasal dari tbl_pengadaan
INSERT INTO tbl_barang(kode_barang,
nama_barang,harga_jual, stok harga_pengadaan)
SELECT tbl_detail_pengadaan.kode_barang,
"Pop Mie Pedas",
tbl_detail_pengadaan.total_harga/
(tbl_detail_pengadaan.jumlah*40),
tbl_detail_pengadaan.jumlah
tbl_detail_pengadaan.total_harga
FROM tbl_detail_pengadaan
WHERE tbl_detail_pengadaan.kode_pengadaan
NOT IN (SELECT kode_barang FROM tbl_barang)