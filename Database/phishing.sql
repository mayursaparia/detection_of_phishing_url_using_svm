-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Oct 05, 2020 at 09:52 AM
-- Server version: 5.6.21
-- PHP Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `phishing`
--

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE IF NOT EXISTS `registration` (
`id` int(11) NOT NULL,
  `fullname` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `phone` int(11) NOT NULL,
  `email` varchar(30) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `country` varchar(20) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`id`, `fullname`, `password`, `phone`, `email`, `gender`, `country`) VALUES
(1, 'mayur', '12345', 1234567890, 'mayur@gmail.com', 'Male', 'India'),
(2, 'rachita', '1234', 1234567899, 'rachi@gmail.com', 'Female', 'India'),
(7, 'Shirin', '123456', 1234567887, 'shirin@gmail.com', 'Female', 'USA'),
(8, 'xyz', '123', 2147483647, 'xyz@gmail.com', 'Male', 'China'),
(9, 'abc', '123', 1234567898, 'abc@gmail.com', 'Female', 'USA'),
(10, 'mm', '12', 234567899, 'xxx@gmail.com', 'Male', 'Germany'),
(11, 'we', '1', 2147483647, 'asdf@gmail.com', 'Female', 'India'),
(12, 'zzz', '111', 1111111111, 'zzz@gmail.com', 'Male', 'China'),
(13, 'xyz', '123456', 2147483647, 'xyz@gmail.com', 'Male', 'India'),
(14, 'qqq', '1234', 1234567890, 'qqq@gmail.com', 'Male', 'UK');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
 ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `registration`
--
ALTER TABLE `registration`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=15;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
