-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: 2018-01-22 08:14:11
-- 服务器版本： 5.7.17
-- PHP Version: 7.1.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `58`
--

-- --------------------------------------------------------

--
-- 表的结构 `apply`
--

CREATE TABLE `apply` (
  `id` int(11) NOT NULL,
  `rec_id` int(11) NOT NULL COMMENT '招聘id',
  `username` varchar(255) NOT NULL COMMENT '用户'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `apply`
--

INSERT INTO `apply` (`id`, `rec_id`, `username`) VALUES
(1, 1, '去去去12'),
(2, 2, '去去去12'),
(3, 3, '去去去12');

-- --------------------------------------------------------

--
-- 表的结构 `car`
--

CREATE TABLE `car` (
  `id` int(11) NOT NULL,
  `type_id` int(11) NOT NULL COMMENT '类型',
  `brand_id` int(11) NOT NULL COMMENT '品牌',
  `title` varchar(255) NOT NULL,
  `rush` tinyint(255) NOT NULL DEFAULT '0' COMMENT '0不紧急 1紧急',
  `time` int(11) DEFAULT NULL COMMENT '购买时间',
  `journey` varchar(255) DEFAULT NULL COMMENT '行程',
  `cc` varchar(255) DEFAULT NULL COMMENT '排量',
  `gear` varchar(255) DEFAULT NULL COMMENT '挡类型',
  `price` varchar(255) DEFAULT NULL COMMENT '价格',
  `hy` varchar(255) DEFAULT NULL COMMENT '会员...年(没用)',
  `img` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `car`
--

INSERT INTO `car` (`id`, `type_id`, `brand_id`, `title`, `rush`, `time`, `journey`, `cc`, `gear`, `price`, `hy`, `img`) VALUES
(1, 1, 1, '大众 景逸 2012款 LV 1.5 手动 尊贵型-车好省油无事故有质保可分期 急\n', 1, 2013, '6.5万', '1.5', '手动', '2.88', '1', 'http://pic1.58cdn.com.cn/p2/big/n_v2631032fb71ce42aa8ce85e79e5c7410b_a680eb480d27e5ea.jpg?w=200&h=150&crop=1'),
(2, 1, 2, '本田 新宝来 2016款 1.4T 自动 230TSI 25周年纪念版-准新车 急\n', 0, 2016, '3万', '1.4', '自动', '11.1', '2', 'http://pic1.58cdn.com.cn/p2/big/n_v24747ca3230ff43e8947f7c4f60c7e01b_ad3b776cd3ee8d86.jpg?w=200&h=150&crop=1'),
(3, 4, 4, '丰田 汉兰达 2012款 2.7 手自一体 两驱豪华导航版-保证车况精品 可议价 急\n', 1, 2014, '5万', '1.6', '自动', '13.5', '1', 'http://pic1.58cdn.com.cn/p2/big/n_v22383472212524a1c93b86efb3dc64623_29d076ad88ce329c.jpg?w=200&h=150&crop=1'),
(4, 1, 3, '别克 揽胜 2015款 3.0 自动 V6 SC Vogue-准新车 全车车衣 超高性价比 急\n', 1, 2015, '3万', '1.5', '自动', '100', '2', 'http://pic1.58cdn.com.cn/p2/big/n_v288a5116a6add401f89ec460748e3ab8b_d3396e912cce8426.jpg?w=200&h=150&crop=1'),
(5, 2, 1, '起亚 狮跑 2013款 2.0 自动 GLS两驱 急\n', 0, 2015, '3万', '2.0', '自动', '10.3', '1', 'http://pic1.58cdn.com.cn/p2/big/n_v2d54eacfdee9247cbaafbe3929611cbf8_874a0721d8b50826.jpg?w=200&h=150&crop=1'),
(6, 3, 4, '保时捷 卡宴 2011款 3.6 手自一体 美规-一手车 4.6万公里 急\n', 0, 2014, '5万', '3.6', '自动', '60.5', '3', 'http://pic1.58cdn.com.cn/p1/big/n_v201eb9f07504f45b5bf9d4436c0a2d87e_c5ef7da6f519bae9.jpg?w=200&h=150&crop=1');

-- --------------------------------------------------------

--
-- 表的结构 `car_brand`
--

CREATE TABLE `car_brand` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL COMMENT '品牌名'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `car_brand`
--

INSERT INTO `car_brand` (`id`, `name`) VALUES
(1, '大众'),
(2, '本田'),
(3, '别克'),
(4, '丰田'),
(5, '福特'),
(6, '日产'),
(7, '奇瑞'),
(8, '宝马'),
(9, '现代'),
(10, '奥迪'),
(11, '马自达'),
(12, '比亚迪'),
(13, '铃木'),
(14, '雪铁龙'),
(15, '吉利'),
(16, '奔驰');

-- --------------------------------------------------------

--
-- 表的结构 `car_type`
--

CREATE TABLE `car_type` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL COMMENT '类别名'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `car_type`
--

INSERT INTO `car_type` (`id`, `name`) VALUES
(1, '轿车'),
(2, 'suv'),
(3, '面包车'),
(4, 'MPV'),
(5, '跑车'),
(6, '皮卡'),
(7, '新能源'),
(8, '工程车'),
(9, '货车'),
(10, '客车'),
(11, '三轮'),
(12, '老年车'),
(13, '平行进口车');

-- --------------------------------------------------------

--
-- 表的结构 `company`
--

CREATE TABLE `company` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL COMMENT '公司名'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `company`
--

INSERT INTO `company` (`id`, `name`) VALUES
(1, '沈阳翊木歆阿敖德萨贸有限公司'),
(2, '天福假期'),
(3, '大连新季源商贸有限公司'),
(4, '沈阳市皇姑区千晟二手车信息'),
(5, '沈阳市森园家具厂'),
(6, '沈阳道乐商务信息咨询有限公司'),
(7, '沈阳嘉茂科技有限公司'),
(8, '沈阳威仕顿体育发展有限公司'),
(9, '武汉优大蚂蚁信息科技'),
(10, '芒果不动产多福店'),
(11, '麟龙科技股份 '),
(12, '中国平安'),
(13, '太平人寿保险有限公司辽宁分公司'),
(14, '沈阳我来了网络科技有限公司 ');

-- --------------------------------------------------------

--
-- 表的结构 `company_welfare`
--

CREATE TABLE `company_welfare` (
  `id` int(11) NOT NULL,
  `cid` int(11) DEFAULT NULL COMMENT '公司id',
  `wid` int(11) DEFAULT NULL COMMENT '福利id'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `company_welfare`
--

INSERT INTO `company_welfare` (`id`, `cid`, `wid`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 5),
(5, 2, 2),
(6, 2, 5),
(7, 2, 6),
(8, 2, 7),
(9, 3, 7),
(10, 3, 9),
(11, 3, 2),
(12, 5, 1),
(13, 5, 10),
(14, 5, 5),
(15, 6, 3);

-- --------------------------------------------------------

--
-- 表的结构 `index_list`
--

CREATE TABLE `index_list` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `value` int(255) DEFAULT NULL,
  `red` tinyint(1) NOT NULL DEFAULT '0' COMMENT '0 不显示红色 1 显示红色',
  `state` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `index_list`
--

INSERT INTO `index_list` (`id`, `name`, `value`, `red`, `state`) VALUES
(1, '58APP', 1, 1, 0),
(2, '商家APP', 2, 1, 0),
(3, '58公众号', 3, 1, 0),
(4, '小程序', 4, 1, 0),
(5, '金融', 5, 1, 0),
(6, '安居客', 6, 0, 0),
(7, '中华英才', 7, 0, 0),
(8, '58车', 8, 0, 0),
(9, '58同镇', 9, 0, 0);

-- --------------------------------------------------------

--
-- 表的结构 `rec_list`
--

CREATE TABLE `rec_list` (
  `id` int(11) NOT NULL,
  `type` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `money` varchar(255) DEFAULT NULL,
  `title` varchar(255) NOT NULL,
  `job_name` varchar(255) NOT NULL COMMENT '工作名称',
  `edu` varchar(255) NOT NULL DEFAULT '不限',
  `exp` varchar(255) DEFAULT '不限'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `rec_list`
--

INSERT INTO `rec_list` (`id`, `type`, `company_id`, `money`, `title`, `job_name`, `edu`, `exp`) VALUES
(1, 1, 1, '5000-5000', '和平区  | 综合金融理财顾问+双休', '销售代表', '不限', '不限'),
(2, 1, 2, '3000-4500', '沈河区  | 百万月薪俱乐部急招销售', '销售代表', '不限', '不限'),
(3, 1, 3, '2000-3000', '沈阳  | 电话销售入职双休五险一金', '电话销售', '不限', '不限'),
(4, 22, 5, '8000-12000', '铁西区  | 沈阳送餐员送餐员', '送餐员', '大专', '不限'),
(5, 22, 6, '2000-5000', 'asadsdasd', 'sdasd', '不限', '不限');

-- --------------------------------------------------------

--
-- 表的结构 `rec_type`
--

CREATE TABLE `rec_type` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `hot` tinyint(1) NOT NULL DEFAULT '0' COMMENT '1 hot',
  `value` int(255) DEFAULT NULL COMMENT '排序'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `rec_type`
--

INSERT INTO `rec_type` (`id`, `name`, `hot`, `value`) VALUES
(1, '销售', 1, 1),
(2, '配菜/打荷', 0, 2),
(3, '技工', 0, 3),
(4, '服务员', 1, 4),
(5, '导购员', 0, 5),
(6, '保洁', 0, 6),
(7, '发型师', 0, 7),
(8, '客服', 0, 8),
(9, '接待', 0, 9),
(10, '司机', 0, 10),
(11, '收银员', 0, 11),
(12, '营业员', 1, 12),
(13, '保姆', 0, 13),
(14, '美容师', 0, 14),
(15, '文员', 0, 15),
(16, '杂工', 0, 16),
(17, '汽车', 0, 17),
(18, '厨师', 0, 18),
(19, '保安', 1, 19),
(20, '网管', 0, 20),
(21, '大堂经理', 0, 21),
(22, '外卖小哥', 1, 1),
(23, '电工', 0, 22);

-- --------------------------------------------------------

--
-- 表的结构 `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL DEFAULT '0',
  `create_time` char(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `state`, `create_time`) VALUES
(6, '去去去', 'b2ca678b4c936f905fb82f2733f5297f', '0', NULL),
(7, 'aaa', 'c4ca4238a0b923820dcc509a6f75849b', '0', NULL),
(8, '去去去12', '7694f4a66316e53c8cdd9d9954bd611d', '0', NULL),
(9, '1', 'b59c67bf196a4758191e42f76670ceba', '0', NULL);

-- --------------------------------------------------------

--
-- 替换视图以便查看 `v_all_rec_list`
-- (See below for the actual view)
--
CREATE TABLE `v_all_rec_list` (
`id` int(11)
,`type` int(11)
,`company_id` int(11)
,`money` varchar(255)
,`title` varchar(255)
,`job_name` varchar(255)
,`edu` varchar(255)
,`exp` varchar(255)
,`cname` varchar(255)
,`wid_list` text
,`mname_list` text
,`wid` int(11)
);

-- --------------------------------------------------------

--
-- 替换视图以便查看 `v_company`
-- (See below for the actual view)
--
CREATE TABLE `v_company` (
`id` int(11)
,`cid` int(11)
,`wid` int(11)
,`mname` varchar(255)
,`cname` varchar(255)
);

-- --------------------------------------------------------

--
-- 替换视图以便查看 `v_rec_list`
-- (See below for the actual view)
--
CREATE TABLE `v_rec_list` (
`id` int(11)
,`type` int(11)
,`company_id` int(11)
,`money` varchar(255)
,`title` varchar(255)
,`job_name` varchar(255)
,`edu` varchar(255)
,`exp` varchar(255)
,`cname` varchar(255)
,`wid_list` text
,`mname_list` text
);

-- --------------------------------------------------------

--
-- 表的结构 `welfare`
--

CREATE TABLE `welfare` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `welfare`
--

INSERT INTO `welfare` (`id`, `name`) VALUES
(1, '五险一金'),
(2, '包住'),
(3, '包吃'),
(4, '年底双薪'),
(5, '周末双休'),
(6, '交通补助'),
(7, '加班补助'),
(8, '饭补'),
(9, '话补'),
(10, '房补');

-- --------------------------------------------------------

--
-- 视图结构 `v_all_rec_list`
--
DROP TABLE IF EXISTS `v_all_rec_list`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_all_rec_list`  AS  select `t1`.`id` AS `id`,`t1`.`type` AS `type`,`t1`.`company_id` AS `company_id`,`t1`.`money` AS `money`,`t1`.`title` AS `title`,`t1`.`job_name` AS `job_name`,`t1`.`edu` AS `edu`,`t1`.`exp` AS `exp`,`t1`.`cname` AS `cname`,`t1`.`wid_list` AS `wid_list`,`t1`.`mname_list` AS `mname_list`,`t2`.`wid` AS `wid` from (`v_rec_list` `t1` join `company_welfare` `t2` on((`t1`.`company_id` = `t2`.`cid`))) ;

-- --------------------------------------------------------

--
-- 视图结构 `v_company`
--
DROP TABLE IF EXISTS `v_company`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_company`  AS  select `t1`.`id` AS `id`,`t1`.`cid` AS `cid`,`t1`.`wid` AS `wid`,`t2`.`name` AS `mname`,`t3`.`name` AS `cname` from ((`company_welfare` `t1` join `welfare` `t2` on((`t1`.`wid` = `t2`.`id`))) join `company` `t3` on((`t1`.`cid` = `t3`.`id`))) ;

-- --------------------------------------------------------

--
-- 视图结构 `v_rec_list`
--
DROP TABLE IF EXISTS `v_rec_list`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_rec_list`  AS  select `t1`.`id` AS `id`,`t1`.`type` AS `type`,`t1`.`company_id` AS `company_id`,`t1`.`money` AS `money`,`t1`.`title` AS `title`,`t1`.`job_name` AS `job_name`,`t1`.`edu` AS `edu`,`t1`.`exp` AS `exp`,`t2`.`name` AS `cname`,group_concat(`t3`.`wid` separator ',') AS `wid_list`,group_concat(`t3`.`mname` separator ',') AS `mname_list` from ((`rec_list` `t1` join `company` `t2` on((`t1`.`company_id` = `t2`.`id`))) join `v_company` `t3` on((`t2`.`id` = `t3`.`cid`))) group by `t1`.`id` ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `apply`
--
ALTER TABLE `apply`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `car`
--
ALTER TABLE `car`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `car_brand`
--
ALTER TABLE `car_brand`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `car_type`
--
ALTER TABLE `car_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `company_welfare`
--
ALTER TABLE `company_welfare`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `index_list`
--
ALTER TABLE `index_list`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rec_list`
--
ALTER TABLE `rec_list`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rec_type`
--
ALTER TABLE `rec_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `welfare`
--
ALTER TABLE `welfare`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `apply`
--
ALTER TABLE `apply`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- 使用表AUTO_INCREMENT `car`
--
ALTER TABLE `car`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- 使用表AUTO_INCREMENT `car_brand`
--
ALTER TABLE `car_brand`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- 使用表AUTO_INCREMENT `car_type`
--
ALTER TABLE `car_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- 使用表AUTO_INCREMENT `company`
--
ALTER TABLE `company`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- 使用表AUTO_INCREMENT `company_welfare`
--
ALTER TABLE `company_welfare`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- 使用表AUTO_INCREMENT `index_list`
--
ALTER TABLE `index_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- 使用表AUTO_INCREMENT `rec_list`
--
ALTER TABLE `rec_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- 使用表AUTO_INCREMENT `rec_type`
--
ALTER TABLE `rec_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
--
-- 使用表AUTO_INCREMENT `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- 使用表AUTO_INCREMENT `welfare`
--
ALTER TABLE `welfare`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
