SELECT dp.id, dp.nama, dp.usia, dp.alamat, dp.email, dp.pekerjaan FROM data_pengguna dp
WHERE NOT EXISTS (SELECT * FROM data_pekerjaan
WHERE NOT EXISTS (SELECT * FROM data_pengguna WHERE pekerjaan = dp.pekerjaan));