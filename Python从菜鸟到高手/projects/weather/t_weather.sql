-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: 2018-01-21 14:59:46
-- 服务器版本： 5.6.21
-- PHP Version: 7.1.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `weather`
--

-- --------------------------------------------------------

--
-- 表的结构 `t_weather`
--

CREATE TABLE `t_weather` (
  `_id` int(11) NOT NULL COMMENT '城市编号',
  `cityNumber` varchar(255) DEFAULT NULL,
  `cityName` varchar(255) DEFAULT NULL,
  `cityNameen` varchar(255) DEFAULT NULL COMMENT '拼音',
  `cityWeather` varchar(255) DEFAULT NULL COMMENT '晴 阴....',
  `temp` varchar(255) DEFAULT NULL COMMENT '温度',
  `sd` varchar(255) DEFAULT NULL COMMENT '湿度',
  `njd` varchar(255) DEFAULT NULL COMMENT '能见度',
  `wd` varchar(255) DEFAULT NULL COMMENT '风向',
  `ws` varchar(255) DEFAULT NULL COMMENT '风级',
  `pm25` varchar(255) DEFAULT NULL,
  `limitnumber` varchar(255) DEFAULT NULL COMMENT '限行'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
