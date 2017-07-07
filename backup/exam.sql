CREATE DATABASE IF NOT EXISTS `exam`;
USE `exam`;

CREATE TABLE `alresult` (
  `exam` varchar(50) DEFAULT NULL,
  `year` varchar(5) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `indexNo` varchar(10) NOT NULL,
  `districtRank` varchar(5) DEFAULT NULL,
  `islandRank` varchar(6) DEFAULT NULL,
  `zScore` varchar(10) DEFAULT NULL,
  `subjectStream` varchar(50) DEFAULT NULL,
  `subject1` varchar(50) DEFAULT NULL,
  `result1` varchar(10) DEFAULT NULL,
  `subject2` varchar(50) DEFAULT NULL,
  `result2` varchar(10) DEFAULT NULL,
  `subject3` varchar(50) DEFAULT NULL,
  `result3` varchar(10) DEFAULT NULL,
  `subject4` varchar(50) DEFAULT NULL,
  `result4` varchar(10) DEFAULT NULL,
  `subject5` varchar(50) DEFAULT NULL,
  `result5` varchar(10) DEFAULT NULL
);

CREATE TABLE `gvresult` (
  `exam` varchar(40) DEFAULT NULL,
  `year` varchar(4) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `indexNo` varchar(10) NOT NULL,
  `marks` varchar(6) DEFAULT NULL,
  `districtRank` varchar(20) DEFAULT NULL
);

CREATE TABLE `olresult` (
  `exam` varchar(50) DEFAULT NULL,
  `year` varchar(5) DEFAULT NULL,
  `syllabus` varchar(30) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `indexNo` varchar(15) NOT NULL,
  `subject1` varchar(50) DEFAULT NULL,
  `result1` varchar(10) DEFAULT NULL,
  `subject2` varchar(50) DEFAULT NULL,
  `result2` varchar(10) DEFAULT NULL,
  `subject3` varchar(50) DEFAULT NULL,
  `result3` varchar(10) DEFAULT NULL,
  `subject4` varchar(50) DEFAULT NULL,
  `result4` varchar(10) DEFAULT NULL,
  `subject5` varchar(50) DEFAULT NULL,
  `result5` varchar(10) DEFAULT NULL,
  `subject6` varchar(50) DEFAULT NULL,
  `result6` varchar(10) DEFAULT NULL,
  `subject7` varchar(50) DEFAULT NULL,
  `result7` varchar(10) DEFAULT NULL,
  `subject8` varchar(50) DEFAULT NULL,
  `result8` varchar(10) DEFAULT NULL,
  `subject9` varchar(50) DEFAULT NULL,
  `result9` varchar(10) DEFAULT NULL
);


ALTER TABLE `alresult`
  ADD PRIMARY KEY (`indexNo`);

ALTER TABLE `gvresult`
  ADD PRIMARY KEY (`indexNo`);

ALTER TABLE `olresult`
  ADD PRIMARY KEY (`indexNo`);
