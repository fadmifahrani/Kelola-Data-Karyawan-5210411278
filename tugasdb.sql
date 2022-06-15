-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 15, 2022 at 07:29 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tugasdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `db_karyawan`
--

CREATE TABLE `db_karyawan` (
  `nik` int(10) NOT NULL,
  `nama` varchar(40) NOT NULL,
  `jenis_kelamin` char(1) NOT NULL,
  `tglMasuk` date NOT NULL,
  `jabatan` varchar(50) NOT NULL,
  `divisi` varchar(15) NOT NULL,
  `gaji` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `db_karyawan`
--

INSERT INTO `db_karyawan` (`nik`, `nama`, `jenis_kelamin`, `tglMasuk`, `jabatan`, `divisi`, `gaji`) VALUES
(111, 'Novi', 'P', '2019-05-11', 'Software Developer', 'Staf', 6000000),
(114, 'Armansyah', 'L', '2021-02-16', 'Web Developer', 'Staf', 5000000),
(115, 'David', 'L', '2018-09-17', 'Hardware Engineer', 'Umum', 7000000);

-- --------------------------------------------------------

--
-- Table structure for table `db_user`
--

CREATE TABLE `db_user` (
  `nama` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `pasword` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `db_user`
--

INSERT INTO `db_user` (`nama`, `email`, `pasword`) VALUES
('fadmi', 'fadmi@gmail.com', 123),
('alif', 'alif@gmail.com', 12345);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `db_karyawan`
--
ALTER TABLE `db_karyawan`
  ADD PRIMARY KEY (`nik`);

--
-- Indexes for table `db_user`
--
ALTER TABLE `db_user`
  ADD PRIMARY KEY (`pasword`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
