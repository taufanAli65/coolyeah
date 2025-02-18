CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  age INT,
  address VARCHAR(100),
  email VARCHAR(50)
);
CREATE TABLE jobs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  job_title VARCHAR(50),
  FOREIGN KEY (user_id) REFERENCES users(id)
);
-- Memasukkan data ke dalam tabel dengan nama orang Indonesia
INSERT INTO Pengguna (nama, usia, alamat, email, pekerjaan)
VALUES
  ('Budi Santoso', 25, 'Jalan Merdeka No. 10', 'budisantoso@example.com', 'Mahasiswa'),
  ('Rina Setiawati', 35, 'Jalan Sudirman No. 15', 'rinasetiawati@example.com', 'Dokter'),
  ('Ahmad Hidayat', 42, 'Jalan Imam Bonjol No. 20', 'ahmadhidayat@example.com', 'Pengusaha'),
  ('Siti Rahayu', 28, 'Jalan Diponegoro No. 8', 'sitirahayu@example.com', 'Desainer Grafis'),
  ('Rizky Pratama', 50, 'Jalan Gatot Subroto No. 5', 'rizkypratama@example.com', 'Akuntan'),
  ('Dewi Puspitasari', 31, 'Jalan Pahlawan No. 12', 'dewipuspitasari@example.com', 'Penulis'),
  ('Eko Sutrisno', 38, 'Jalan Veteran No. 18', 'ekosutrisno@example.com', 'Guru'),
  ('Anita Setyawati', 27, 'Jalan Ahmad Yani No. 25', 'anitasetyawati@example.com', 'Arsitek'),
  ('Yusuf Kurniawan', 45, 'Jalan Hayam Wuruk No. 30', 'yusufkurniawan@example.com', 'Insinyur'),
  ('Ratna Dewi', 33, 'Jalan Asia Afrika No. 7', 'ratnadewi@example.com', 'Pengacara'),
  ('Feri Susanto', 29, 'Jalan MT Haryono No. 14', 'ferisusanto@example.com', 'Peneliti'),
  ('Maya Indah', 41, 'Jalan HR Rasuna Said No. 22', 'mayaindah@example.com', 'Manajer'),
  ('Adi Wijaya', 36, 'Jalan Cikini Raya No. 9', 'adiwijaya@example.com', 'Programmer'),
  ('Dewi Permata', 26, 'Jalan Ahmad Dahlan No. 16', 'dewipermata@example.com', 'Konsultan'),
  ('Arief Santoso', 47, 'Jalan Thamrin No. 28', 'ariefsantoso@example.com', 'Pengusaha'),
  ('Sinta Dewi', 32, 'Jalan Kebon Sirih No. 11', 'sintadewi@example.com', 'Pengajar'),
  ('Andi Pratama', 39, 'Jalan Tebet Barat No. 19', 'andipratama@example.com', 'Dokter'),
  ('Fitriani Putri', 30, 'Jalan Kuningan No. 6', 'fitrianiputri@example.com', 'Blogger'),
  ('Rahmat Widodo', 49, 'Jalan Gatot Subroto No. 17', 'rahmatwidodo@example.com', 'Pengusaha'),
  ('Dewi Wulandari', 34, 'Jalan Thamrin No. 23', 'dewiwulandari@example.com', 'Desainer Interior'),
  ('Budi Setiawan', 37, 'Jalan Asia Afrika No. 13', 'budisetiawan@example.com', 'Arsitek'),
  ('Laras Sekar', 24, 'Jalan Sudirman No. 26', 'larassekar@example.com', 'Penulis'),
  ('Hendro Gunawan', 43, 'Jalan HR Rasuna Said No. 21', 'hendrogunawan@example.com', 'Insinyur'),
  ('Anita Halim', 31, 'Jalan MT Haryono No. 7', 'anitahalim@example.com', 'Pengacara'),
  ('Agus Wijaya', 40, 'Jalan Kebon Sirih No. 14', 'aguswijaya@example.com', 'Peneliti');

-- Memilih hanya kolom nama dan pekerjaan dari tabel Pengguna
SELECT nama, usia, alamat, email, pekerjaan FROM Pengguna;
