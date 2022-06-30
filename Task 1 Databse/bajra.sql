-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 30, 2022 at 01:10 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bajra`
--

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `DeptID` int(11) NOT NULL,
  `DeptName` varchar(255) NOT NULL,
  `DeptCode` varchar(100) DEFAULT NULL,
  `ParentDeptID` int(11) NOT NULL,
  `ManagerId` int(11) NOT NULL,
  `Description` text NOT NULL,
  `Active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`DeptID`, `DeptName`, `DeptCode`, `ParentDeptID`, `ManagerId`, `Description`, `Active`) VALUES
(1, 'Sales', '01', 1, 1, 'Sales Department', 1),
(2, 'Marketing', '02', 2, 2, 'Marketing Department', 1),
(3, 'Designing', '03', 3, 3, 'Designing Department', 1);

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `EmployeeID` int(11) NOT NULL,
  `FirstName` varchar(255) NOT NULL,
  `MiddleName` varchar(255) DEFAULT NULL,
  `LastName` varchar(255) NOT NULL,
  `JoinDATE` datetime DEFAULT NULL,
  `MonthlySalary` decimal(10,5) DEFAULT NULL,
  `DeptID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`EmployeeID`, `FirstName`, `MiddleName`, `LastName`, `JoinDATE`, `MonthlySalary`, `DeptID`) VALUES
(1, 'Aashish', NULL, 'Thapa', '2022-01-18 11:34:26', '70000.00000', 1),
(2, 'Ashok', NULL, 'Thapa', '2022-04-10 11:34:26', '50000.00000', 2),
(3, 'Sandesh', NULL, 'Baral', '2021-01-18 11:34:26', '90000.00000', 1),
(4, 'Rahul', NULL, 'singh', '2022-06-18 11:34:26', '40000.00000', 3),
(5, 'Himal', NULL, 'Rana', '2022-06-18 11:34:26', '99999.99999', 1),
(6, 'Suman', NULL, 'Nepal', '2022-06-18 11:34:26', '80000.00000', 2),
(7, 'Adhikar', NULL, 'Chaudhary', '2022-06-18 11:34:26', '50000.00000', 2),
(8, 'Bijay', NULL, 'Rajali', '2022-06-18 11:34:26', '60000.00000', 3);

-- --------------------------------------------------------

--
-- Table structure for table `manager`
--

CREATE TABLE `manager` (
  `ManagerID` int(11) NOT NULL,
  `ManagerName` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `manager`
--

INSERT INTO `manager` (`ManagerID`, `ManagerName`) VALUES
(1, 'Shyam Shreatha'),
(2, 'Hari Karki'),
(3, 'Rajesh Hamal'),
(4, 'Ajay Lama');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`DeptID`),
  ADD KEY `FK_Manager` (`ManagerId`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`EmployeeID`),
  ADD KEY `FK_Dept` (`DeptID`);

--
-- Indexes for table `manager`
--
ALTER TABLE `manager`
  ADD PRIMARY KEY (`ManagerID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `department`
--
ALTER TABLE `department`
  MODIFY `DeptID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `EmployeeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `manager`
--
ALTER TABLE `manager`
  MODIFY `ManagerID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `department`
--
ALTER TABLE `department`
  ADD CONSTRAINT `FK_Manager` FOREIGN KEY (`ManagerId`) REFERENCES `manager` (`ManagerID`);

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `FK_Dept` FOREIGN KEY (`DeptID`) REFERENCES `department` (`DeptID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
