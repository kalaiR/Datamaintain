CREATE DATABASE  IF NOT EXISTS `datamaintain` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `datamaintain`;
-- MySQL dump 10.13  Distrib 5.5.41, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: datamaintain
-- ------------------------------------------------------
-- Server version	5.5.41-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add degree',8,'add_degree'),(23,'Can change degree',8,'change_degree'),(24,'Can delete degree',8,'delete_degree'),(25,'Can add specialization',9,'add_specialization'),(26,'Can change specialization',9,'change_specialization'),(27,'Can delete specialization',9,'delete_specialization'),(28,'Can add department',10,'add_department'),(29,'Can change department',10,'change_department'),(30,'Can delete department',10,'delete_department'),(31,'Can add year',11,'add_year'),(32,'Can change year',11,'change_year'),(33,'Can delete year',11,'delete_year'),(34,'Can add student_ admission',12,'add_student_admission'),(35,'Can change student_ admission',12,'change_student_admission'),(36,'Can delete student_ admission',12,'delete_student_admission'),(37,'Can add staff_ details',13,'add_staff_details'),(38,'Can change staff_ details',13,'change_staff_details'),(39,'Can delete staff_ details',13,'delete_staff_details'),(40,'Can add create_ attendance_ list',14,'add_create_attendance_list'),(41,'Can change create_ attendance_ list',14,'change_create_attendance_list'),(42,'Can delete create_ attendance_ list',14,'delete_create_attendance_list'),(43,'Can add absent list_ details',15,'add_absentlist_details'),(44,'Can change absent list_ details',15,'change_absentlist_details'),(45,'Can delete absent list_ details',15,'delete_absentlist_details'),(46,'Can add absent list',16,'add_absentlist'),(47,'Can change absent list',16,'change_absentlist'),(48,'Can delete absent list',16,'delete_absentlist'),(49,'Can add parent_ details',17,'add_parent_details'),(50,'Can change parent_ details',17,'change_parent_details'),(51,'Can delete parent_ details',17,'delete_parent_details'),(52,'Can add action',18,'add_action'),(53,'Can change action',18,'change_action'),(54,'Can delete action',18,'delete_action'),(55,'Can add client',19,'add_client'),(56,'Can change client',19,'change_client'),(57,'Can delete client',19,'delete_client'),(58,'Can add queue',20,'add_queue'),(59,'Can change queue',20,'change_queue'),(60,'Can delete queue',20,'delete_queue'),(61,'Can add message',21,'add_message'),(62,'Can change message',21,'change_message'),(63,'Can delete message',21,'delete_message'),(64,'Can add task state',22,'add_taskmeta'),(65,'Can change task state',22,'change_taskmeta'),(66,'Can delete task state',22,'delete_taskmeta'),(67,'Can add saved group result',23,'add_tasksetmeta'),(68,'Can change saved group result',23,'change_tasksetmeta'),(69,'Can delete saved group result',23,'delete_tasksetmeta'),(70,'Can add interval',24,'add_intervalschedule'),(71,'Can change interval',24,'change_intervalschedule'),(72,'Can delete interval',24,'delete_intervalschedule'),(73,'Can add crontab',25,'add_crontabschedule'),(74,'Can change crontab',25,'change_crontabschedule'),(75,'Can delete crontab',25,'delete_crontabschedule'),(76,'Can add periodic tasks',26,'add_periodictasks'),(77,'Can change periodic tasks',26,'change_periodictasks'),(78,'Can delete periodic tasks',26,'delete_periodictasks'),(79,'Can add periodic task',27,'add_periodictask'),(80,'Can change periodic task',27,'change_periodictask'),(81,'Can delete periodic task',27,'delete_periodictask'),(82,'Can add worker',28,'add_workerstate'),(83,'Can change worker',28,'change_workerstate'),(84,'Can delete worker',28,'delete_workerstate'),(85,'Can add task',29,'add_taskstate'),(86,'Can change task',29,'change_taskstate'),(87,'Can delete task',29,'delete_taskstate');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'admin','','','admin@fixido.com','pbkdf2_sha256$10000$ZbYSkEsc9f8M$cxgA67MI/rG6gv9q0lrLeHH4H9kOdrg1OiKVbF1m0YY=',1,1,1,'2015-05-12 13:07:15','2015-05-08 10:21:56'),(2,'kalai','kalai','r','kalai@gmail.com','pbkdf2_sha256$10000$o8bsAygHjZtc$HsISM3XpWe5Pk4hT9O2tS8X6e8hWlr2gW40LBz+Xa0w=',1,1,0,'2015-05-12 12:42:11','2015-05-08 10:30:06'),(3,'vani','vani','a','vanikjpd@gmail.com','pbkdf2_sha256$10000$8gnsMa4AY79h$MEZf3eIfB4RDKpl+H87gstQNBLTlJmXOfFUhxRynJ+4=',1,1,0,'2015-05-08 11:55:37','2015-05-08 10:30:35'),(4,'geetha','geetha','v','geetha@gmail.com','pbkdf2_sha256$10000$tD8vo5nFMWTe$ur8ECXHoyxbGsBBL8vpnPHxQsAGihQj4cEQJcq2E6dg=',1,1,0,'2015-05-12 13:16:00','2015-05-08 10:55:54');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`),
  CONSTRAINT `group_id_refs_id_f0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=400 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (343,2,1),(344,2,2),(345,2,3),(346,2,4),(347,2,5),(348,2,6),(349,2,7),(350,2,8),(351,2,9),(352,2,10),(353,2,11),(354,2,12),(355,2,13),(356,2,14),(357,2,15),(358,2,16),(359,2,17),(360,2,18),(361,2,19),(362,2,20),(363,2,21),(364,2,22),(365,2,23),(366,2,24),(367,2,25),(368,2,26),(369,2,27),(370,2,28),(371,2,29),(372,2,30),(373,2,31),(374,2,32),(375,2,33),(376,2,34),(377,2,35),(378,2,36),(379,2,37),(380,2,38),(381,2,39),(382,2,40),(383,2,41),(384,2,42),(385,2,43),(386,2,44),(387,2,45),(388,2,46),(389,2,47),(390,2,48),(391,2,49),(392,2,50),(393,2,51),(394,2,52),(395,2,53),(396,2,54),(397,2,55),(398,2,56),(399,2,57),(58,3,1),(59,3,2),(60,3,3),(61,3,4),(62,3,5),(63,3,6),(64,3,7),(65,3,8),(66,3,9),(67,3,10),(68,3,11),(69,3,12),(70,3,13),(71,3,14),(72,3,15),(73,3,16),(74,3,17),(75,3,18),(76,3,19),(77,3,20),(78,3,21),(79,3,22),(80,3,23),(81,3,24),(82,3,25),(83,3,26),(84,3,27),(85,3,28),(86,3,29),(87,3,30),(88,3,31),(89,3,32),(90,3,33),(91,3,34),(92,3,35),(93,3,36),(94,3,37),(95,3,38),(96,3,39),(97,3,40),(98,3,41),(99,3,42),(100,3,43),(101,3,44),(102,3,45),(103,3,46),(104,3,47),(105,3,48),(106,3,49),(107,3,50),(108,3,51),(109,3,52),(110,3,53),(111,3,54),(112,3,55),(113,3,56),(114,3,57),(286,4,1),(287,4,2),(288,4,3),(289,4,4),(290,4,5),(291,4,6),(292,4,7),(293,4,8),(294,4,9),(295,4,10),(296,4,11),(297,4,12),(298,4,13),(299,4,14),(300,4,15),(301,4,16),(302,4,17),(303,4,18),(304,4,19),(305,4,20),(306,4,21),(307,4,22),(308,4,23),(309,4,24),(310,4,25),(311,4,26),(312,4,27),(313,4,28),(314,4,29),(315,4,30),(316,4,31),(317,4,32),(318,4,33),(319,4,34),(320,4,35),(321,4,36),(322,4,37),(323,4,38),(324,4,39),(325,4,40),(326,4,41),(327,4,42),(328,4,43),(329,4,44),(330,4,45),(331,4,46),(332,4,47),(333,4,48),(334,4,49),(335,4,50),(336,4,51),(337,4,52),(338,4,53),(339,4,54),(340,4,55),(341,4,56),(342,4,57);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `celery_taskmeta`
--

DROP TABLE IF EXISTS `celery_taskmeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `celery_taskmeta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` varchar(255) NOT NULL,
  `status` varchar(50) NOT NULL,
  `result` longtext,
  `date_done` datetime NOT NULL,
  `traceback` longtext,
  `hidden` tinyint(1) NOT NULL,
  `meta` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  KEY `celery_taskmeta_c91f1bf` (`hidden`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `celery_taskmeta`
--

LOCK TABLES `celery_taskmeta` WRITE;
/*!40000 ALTER TABLE `celery_taskmeta` DISABLE KEYS */;
/*!40000 ALTER TABLE `celery_taskmeta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `celery_tasksetmeta`
--

DROP TABLE IF EXISTS `celery_tasksetmeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `celery_tasksetmeta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `taskset_id` varchar(255) NOT NULL,
  `result` longtext NOT NULL,
  `date_done` datetime NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `taskset_id` (`taskset_id`),
  KEY `celery_tasksetmeta_c91f1bf` (`hidden`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `celery_tasksetmeta`
--

LOCK TABLES `celery_tasksetmeta` WRITE;
/*!40000 ALTER TABLE `celery_tasksetmeta` DISABLE KEYS */;
/*!40000 ALTER TABLE `celery_tasksetmeta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datamaintain_absentlist`
--

DROP TABLE IF EXISTS `datamaintain_absentlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datamaintain_absentlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `absent_id` int(11) NOT NULL,
  `staff_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `absent_id` (`absent_id`),
  KEY `datamaintain_absentlist_a2044c77` (`staff_id`),
  CONSTRAINT `absent_id_refs_id_6f1e1cae` FOREIGN KEY (`absent_id`) REFERENCES `datamaintain_absentlist_details` (`id`),
  CONSTRAINT `staff_id_refs_id_51f5e4f6` FOREIGN KEY (`staff_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datamaintain_absentlist`
--

LOCK TABLES `datamaintain_absentlist` WRITE;
/*!40000 ALTER TABLE `datamaintain_absentlist` DISABLE KEYS */;
/*!40000 ALTER TABLE `datamaintain_absentlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datamaintain_absentlist_details`
--

DROP TABLE IF EXISTS `datamaintain_absentlist_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datamaintain_absentlist_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `absent_regno` varchar(200) NOT NULL,
  `absent_name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datamaintain_absentlist_details`
--

LOCK TABLES `datamaintain_absentlist_details` WRITE;
/*!40000 ALTER TABLE `datamaintain_absentlist_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `datamaintain_absentlist_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datamaintain_create_attendance_list`
--

DROP TABLE IF EXISTS `datamaintain_create_attendance_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datamaintain_create_attendance_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `department_id` int(11) NOT NULL,
  `year_id` int(11) NOT NULL,
  `staff_id` int(11) NOT NULL,
  `staff_status` tinyint(1) NOT NULL,
  `admin_status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `datamaintain_create_attendance_list_2ae7390` (`department_id`),
  KEY `datamaintain_create_attendance_list_15a19819` (`year_id`),
  KEY `datamaintain_create_attendance_list_a2044c77` (`staff_id`),
  CONSTRAINT `department_id_refs_id_306e3fb2` FOREIGN KEY (`department_id`) REFERENCES `datamaintain_department` (`id`),
  CONSTRAINT `staff_id_refs_id_d49877e8` FOREIGN KEY (`staff_id`) REFERENCES `datamaintain_staff_details` (`id`),
  CONSTRAINT `year_id_refs_id_9ec6f843` FOREIGN KEY (`year_id`) REFERENCES `datamaintain_year` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datamaintain_create_attendance_list`
--

LOCK TABLES `datamaintain_create_attendance_list` WRITE;
/*!40000 ALTER TABLE `datamaintain_create_attendance_list` DISABLE KEYS */;
INSERT INTO `datamaintain_create_attendance_list` VALUES (1,'2015-05-12',2,2,8,0,0),(2,'2015-05-11',1,1,5,0,1),(3,'2015-05-13',2,2,8,1,1),(4,'2015-05-09',2,2,8,0,0),(5,'2015-05-10',2,2,8,0,0),(6,'2015-05-08',2,2,8,0,0),(7,'2015-05-07',2,2,8,0,0);
/*!40000 ALTER TABLE `datamaintain_create_attendance_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datamaintain_create_attendance_list_student`
--

DROP TABLE IF EXISTS `datamaintain_create_attendance_list_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datamaintain_create_attendance_list_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_attendance_list_id` int(11) NOT NULL,
  `student_admission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `create_attendance_list_id` (`create_attendance_list_id`,`student_admission_id`),
  KEY `datamaintain_create_attendance_list_student_d92c288f` (`create_attendance_list_id`),
  KEY `datamaintain_create_attendance_list_student_48a336fe` (`student_admission_id`),
  CONSTRAINT `create_attendance_list_id_refs_id_9b60c97d` FOREIGN KEY (`create_attendance_list_id`) REFERENCES `datamaintain_create_attendance_list` (`id`),
  CONSTRAINT `student_admission_id_refs_id_2db0678e` FOREIGN KEY (`student_admission_id`) REFERENCES `datamaintain_student_admission` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datamaintain_create_attendance_list_student`
--

LOCK TABLES `datamaintain_create_attendance_list_student` WRITE;
/*!40000 ALTER TABLE `datamaintain_create_attendance_list_student` DISABLE KEYS */;
INSERT INTO `datamaintain_create_attendance_list_student` VALUES (1,1,3),(2,1,4),(3,2,3),(4,2,4),(5,3,3),(6,3,4),(7,4,3),(8,4,4),(9,5,4),(10,6,3),(11,6,4),(12,7,4);
/*!40000 ALTER TABLE `datamaintain_create_attendance_list_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datamaintain_degree`
--

DROP TABLE IF EXISTS `datamaintain_degree`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datamaintain_degree` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `degree` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datamaintain_degree`
--

LOCK TABLES `datamaintain_degree` WRITE;
/*!40000 ALTER TABLE `datamaintain_degree` DISABLE KEYS */;
INSERT INTO `datamaintain_degree` VALUES (1,'UG'),(2,'PG');
/*!40000 ALTER TABLE `datamaintain_degree` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datamaintain_department`
--

DROP TABLE IF EXISTS `datamaintain_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datamaintain_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `degree_id` int(11) NOT NULL,
  `department` varchar(50) DEFAULT NULL,
  `specialization_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `datamaintain_department_b5221ea` (`degree_id`),
  KEY `datamaintain_department_41ddfe09` (`specialization_id`),
  CONSTRAINT `degree_id_refs_id_ed0f83d` FOREIGN KEY (`degree_id`) REFERENCES `datamaintain_degree` (`id`),
  CONSTRAINT `specialization_id_refs_id_40b5e63a` FOREIGN KEY (`specialization_id`) REFERENCES `datamaintain_specialization` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datamaintain_department`
--

LOCK TABLES `datamaintain_department` WRITE;
/*!40000 ALTER TABLE `datamaintain_department` DISABLE KEYS */;
INSERT INTO `datamaintain_department` VALUES (1,1,'Bsc',1),(2,1,'BCA',3);
/*!40000 ALTER TABLE `datamaintain_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datamaintain_parent_details`
--

DROP TABLE IF EXISTS `datamaintain_parent_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datamaintain_parent_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fathername` varchar(50) DEFAULT NULL,
  `mothername` varchar(50) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_no` varchar(50) DEFAULT NULL,
  `student_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `datamaintain_parent_details_8fc74db5` (`student_id_id`),
  CONSTRAINT `student_id_id_refs_id_df6fc171` FOREIGN KEY (`student_id_id`) REFERENCES `datamaintain_year` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datamaintain_parent_details`
--

LOCK TABLES `datamaintain_parent_details` WRITE;
/*!40000 ALTER TABLE `datamaintain_parent_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `datamaintain_parent_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datamaintain_specialization`
--

DROP TABLE IF EXISTS `datamaintain_specialization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datamaintain_specialization` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `specialization` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datamaintain_specialization`
--

LOCK TABLES `datamaintain_specialization` WRITE;
/*!40000 ALTER TABLE `datamaintain_specialization` DISABLE KEYS */;
INSERT INTO `datamaintain_specialization` VALUES (1,'Computer Science'),(2,'Information Technology'),(3,'Computer Applications');
/*!40000 ALTER TABLE `datamaintain_specialization` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datamaintain_staff_details`
--

DROP TABLE IF EXISTS `datamaintain_staff_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datamaintain_staff_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username_id` int(11) NOT NULL,
  `department_id` int(11) NOT NULL,
  `specialization_id` int(11) NOT NULL,
  `year_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `datamaintain_staff_details_a1190b5c` (`username_id`),
  KEY `datamaintain_staff_details_2ae7390` (`department_id`),
  KEY `datamaintain_staff_details_41ddfe09` (`specialization_id`),
  KEY `datamaintain_staff_details_15a19819` (`year_id`),
  CONSTRAINT `department_id_refs_id_6d5504db` FOREIGN KEY (`department_id`) REFERENCES `datamaintain_department` (`id`),
  CONSTRAINT `specialization_id_refs_id_ecf44428` FOREIGN KEY (`specialization_id`) REFERENCES `datamaintain_specialization` (`id`),
  CONSTRAINT `username_id_refs_id_921a3049` FOREIGN KEY (`username_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `year_id_refs_id_b209331a` FOREIGN KEY (`year_id`) REFERENCES `datamaintain_year` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datamaintain_staff_details`
--

LOCK TABLES `datamaintain_staff_details` WRITE;
/*!40000 ALTER TABLE `datamaintain_staff_details` DISABLE KEYS */;
INSERT INTO `datamaintain_staff_details` VALUES (5,2,1,1,1),(6,3,1,1,2),(8,4,2,3,2);
/*!40000 ALTER TABLE `datamaintain_staff_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datamaintain_student_admission`
--

DROP TABLE IF EXISTS `datamaintain_student_admission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datamaintain_student_admission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reg_no` varchar(20) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `telephone_no` varchar(20) DEFAULT NULL,
  `e_mail` varchar(30) DEFAULT NULL,
  `department_id` int(11) NOT NULL,
  `specialization_id` int(11) NOT NULL,
  `year_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `reg_no` (`reg_no`),
  KEY `datamaintain_student_admission_2ae7390` (`department_id`),
  KEY `datamaintain_student_admission_41ddfe09` (`specialization_id`),
  KEY `datamaintain_student_admission_15a19819` (`year_id`),
  CONSTRAINT `department_id_refs_id_5afbb109` FOREIGN KEY (`department_id`) REFERENCES `datamaintain_department` (`id`),
  CONSTRAINT `specialization_id_refs_id_64d62406` FOREIGN KEY (`specialization_id`) REFERENCES `datamaintain_specialization` (`id`),
  CONSTRAINT `year_id_refs_id_5492042c` FOREIGN KEY (`year_id`) REFERENCES `datamaintain_year` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datamaintain_student_admission`
--

LOCK TABLES `datamaintain_student_admission` WRITE;
/*!40000 ALTER TABLE `datamaintain_student_admission` DISABLE KEYS */;
INSERT INTO `datamaintain_student_admission` VALUES (3,'101','student1','2/5/1990','bsc','9876543210','student1@gmail.com',1,1,1),(4,'102','student2','2/5/1991','hsc','9876543210','student2@gmail.com',2,3,2);
/*!40000 ALTER TABLE `datamaintain_student_admission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datamaintain_year`
--

DROP TABLE IF EXISTS `datamaintain_year`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datamaintain_year` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datamaintain_year`
--

LOCK TABLES `datamaintain_year` WRITE;
/*!40000 ALTER TABLE `datamaintain_year` DISABLE KEYS */;
INSERT INTO `datamaintain_year` VALUES (1,'I'),(2,'II'),(3,'III'),(4,'IV');
/*!40000 ALTER TABLE `datamaintain_year` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-05-08 10:26:04',1,8,'1','UG',1,''),(2,'2015-05-08 10:26:08',1,8,'2','PG',1,''),(3,'2015-05-08 10:27:17',1,9,'1','Specialization object',1,''),(4,'2015-05-08 10:28:19',1,9,'2','Specialization object',1,''),(5,'2015-05-08 10:28:57',1,10,'1','Bsc',1,''),(6,'2015-05-08 10:29:31',1,9,'3','Computer Applications',1,''),(7,'2015-05-08 10:29:33',1,10,'2','BCA',1,''),(8,'2015-05-08 10:30:06',1,3,'2','kalai',1,''),(9,'2015-05-08 10:30:24',1,3,'2','kalai',2,'Changed password, first_name, last_name, email, is_staff and user_permissions.'),(10,'2015-05-08 10:30:35',1,3,'3','vani',1,''),(11,'2015-05-08 10:30:48',1,3,'3','vani',2,'Changed password, first_name, last_name, email, is_staff and user_permissions.'),(12,'2015-05-08 10:31:14',1,11,'1','I',1,''),(13,'2015-05-08 10:31:18',1,11,'2','II',1,''),(14,'2015-05-08 10:31:21',1,11,'3','III',1,''),(15,'2015-05-08 10:31:25',1,11,'4','IV',1,''),(16,'2015-05-08 10:32:33',1,13,'5','Staff_Details object',1,''),(17,'2015-05-08 10:32:50',1,13,'6','Staff_Details object',1,''),(18,'2015-05-08 10:33:38',1,12,'1','student1',1,''),(19,'2015-05-08 10:34:07',1,12,'2','student2',1,''),(20,'2015-05-08 10:55:55',1,3,'4','geetha',1,''),(21,'2015-05-08 10:56:01',1,13,'7','Staff_Details object',1,''),(22,'2015-05-08 11:05:41',1,3,'4','geetha',2,'Changed password, is_staff and user_permissions.'),(23,'2015-05-08 11:05:53',1,13,'7','Staff_Details object',2,'No fields changed.'),(24,'2015-05-08 11:06:09',1,13,'7','Staff_Details object',3,''),(25,'2015-05-08 11:06:24',1,13,'8','Staff_Details object',1,''),(26,'2015-05-09 04:48:57',1,3,'1','admin',2,'Changed password and is_staff.'),(27,'2015-05-09 04:50:24',2,3,'1','admin',2,'Changed password and is_staff.'),(28,'2015-05-09 04:50:31',2,3,'4','geetha',2,'Changed password and is_staff.'),(29,'2015-05-09 04:50:37',2,3,'2','kalai',2,'Changed password and is_staff.'),(30,'2015-05-09 04:51:04',1,3,'4','geetha',2,'Changed password and is_staff.'),(31,'2015-05-09 04:51:11',1,3,'2','kalai',2,'Changed password and is_staff.'),(32,'2015-05-12 09:10:06',1,12,'3','student1',1,''),(33,'2015-05-12 09:10:33',1,12,'4','student2',1,''),(34,'2015-05-12 09:11:08',1,12,'5','student3',1,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'log entry','admin','logentry'),(8,'degree','datamaintain','degree'),(9,'specialization','datamaintain','specialization'),(10,'department','datamaintain','department'),(11,'year','datamaintain','year'),(12,'student_ admission','datamaintain','student_admission'),(13,'staff_ details','datamaintain','staff_details'),(14,'create_ attendance_ list','datamaintain','create_attendance_list'),(15,'absent list_ details','datamaintain','absentlist_details'),(16,'absent list','datamaintain','absentlist'),(17,'parent_ details','datamaintain','parent_details'),(18,'action','fxapi','action'),(19,'client','fxapi','client'),(20,'queue','django','queue'),(21,'message','django','message'),(22,'task state','djcelery','taskmeta'),(23,'saved group result','djcelery','tasksetmeta'),(24,'interval','djcelery','intervalschedule'),(25,'crontab','djcelery','crontabschedule'),(26,'periodic tasks','djcelery','periodictasks'),(27,'periodic task','djcelery','periodictask'),(28,'worker','djcelery','workerstate'),(29,'task','djcelery','taskstate');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3f96133487428fd42bcc3fb68eb5e574','ZGY1OGY2ZjFjNGU1M2M0MTAxYTNiNWMzM2Y1NTgyM2Y2ZDY4MzA0ZjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2015-05-22 12:57:58'),('67757dd385a849c3a546c8bafbf7e6d4','OGJiYjFjZmQ0MGI3MmE2NzU4ZGE2NjllNzJiOWZmZTFhOTBhMjE5YjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQR1Lg==\n','2015-05-25 05:44:31'),('b859a0a5ccccfc3847340fbd373fea65','OGJiYjFjZmQ0MGI3MmE2NzU4ZGE2NjllNzJiOWZmZTFhOTBhMjE5YjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQR1Lg==\n','2015-05-23 06:49:34'),('cc2328767f16883c03ae6f86ea364c0e','OGJiYjFjZmQ0MGI3MmE2NzU4ZGE2NjllNzJiOWZmZTFhOTBhMjE5YjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQR1Lg==\n','2015-05-26 13:16:00');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `djcelery_crontabschedule`
--

DROP TABLE IF EXISTS `djcelery_crontabschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `djcelery_crontabschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `minute` varchar(64) NOT NULL,
  `hour` varchar(64) NOT NULL,
  `day_of_week` varchar(64) NOT NULL,
  `day_of_month` varchar(64) NOT NULL,
  `month_of_year` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `djcelery_crontabschedule`
--

LOCK TABLES `djcelery_crontabschedule` WRITE;
/*!40000 ALTER TABLE `djcelery_crontabschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `djcelery_crontabschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `djcelery_intervalschedule`
--

DROP TABLE IF EXISTS `djcelery_intervalschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `djcelery_intervalschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `every` int(11) NOT NULL,
  `period` varchar(24) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `djcelery_intervalschedule`
--

LOCK TABLES `djcelery_intervalschedule` WRITE;
/*!40000 ALTER TABLE `djcelery_intervalschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `djcelery_intervalschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `djcelery_periodictask`
--

DROP TABLE IF EXISTS `djcelery_periodictask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `djcelery_periodictask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `task` varchar(200) NOT NULL,
  `interval_id` int(11) DEFAULT NULL,
  `crontab_id` int(11) DEFAULT NULL,
  `args` longtext NOT NULL,
  `kwargs` longtext NOT NULL,
  `queue` varchar(200) DEFAULT NULL,
  `exchange` varchar(200) DEFAULT NULL,
  `routing_key` varchar(200) DEFAULT NULL,
  `expires` datetime DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime DEFAULT NULL,
  `total_run_count` int(10) unsigned NOT NULL,
  `date_changed` datetime NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `djcelery_periodictask_17d2d99d` (`interval_id`),
  KEY `djcelery_periodictask_7aa5fda` (`crontab_id`),
  CONSTRAINT `crontab_id_refs_id_ebff5e74` FOREIGN KEY (`crontab_id`) REFERENCES `djcelery_crontabschedule` (`id`),
  CONSTRAINT `interval_id_refs_id_f2054349` FOREIGN KEY (`interval_id`) REFERENCES `djcelery_intervalschedule` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `djcelery_periodictask`
--

LOCK TABLES `djcelery_periodictask` WRITE;
/*!40000 ALTER TABLE `djcelery_periodictask` DISABLE KEYS */;
/*!40000 ALTER TABLE `djcelery_periodictask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `djcelery_periodictasks`
--

DROP TABLE IF EXISTS `djcelery_periodictasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `djcelery_periodictasks` (
  `ident` smallint(6) NOT NULL,
  `last_update` datetime NOT NULL,
  PRIMARY KEY (`ident`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `djcelery_periodictasks`
--

LOCK TABLES `djcelery_periodictasks` WRITE;
/*!40000 ALTER TABLE `djcelery_periodictasks` DISABLE KEYS */;
/*!40000 ALTER TABLE `djcelery_periodictasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `djcelery_taskstate`
--

DROP TABLE IF EXISTS `djcelery_taskstate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `djcelery_taskstate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state` varchar(64) NOT NULL,
  `task_id` varchar(36) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `tstamp` datetime NOT NULL,
  `args` longtext,
  `kwargs` longtext,
  `eta` datetime DEFAULT NULL,
  `expires` datetime DEFAULT NULL,
  `result` longtext,
  `traceback` longtext,
  `runtime` double DEFAULT NULL,
  `retries` int(11) NOT NULL,
  `worker_id` int(11) DEFAULT NULL,
  `hidden` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  KEY `djcelery_taskstate_355bfc27` (`state`),
  KEY `djcelery_taskstate_52094d6e` (`name`),
  KEY `djcelery_taskstate_f0ba6500` (`tstamp`),
  KEY `djcelery_taskstate_20fc5b84` (`worker_id`),
  KEY `djcelery_taskstate_c91f1bf` (`hidden`),
  CONSTRAINT `worker_id_refs_id_4e3453a` FOREIGN KEY (`worker_id`) REFERENCES `djcelery_workerstate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `djcelery_taskstate`
--

LOCK TABLES `djcelery_taskstate` WRITE;
/*!40000 ALTER TABLE `djcelery_taskstate` DISABLE KEYS */;
/*!40000 ALTER TABLE `djcelery_taskstate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `djcelery_workerstate`
--

DROP TABLE IF EXISTS `djcelery_workerstate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `djcelery_workerstate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(255) NOT NULL,
  `last_heartbeat` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname` (`hostname`),
  KEY `djcelery_workerstate_eb8ac7e4` (`last_heartbeat`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `djcelery_workerstate`
--

LOCK TABLES `djcelery_workerstate` WRITE;
/*!40000 ALTER TABLE `djcelery_workerstate` DISABLE KEYS */;
/*!40000 ALTER TABLE `djcelery_workerstate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `djkombu_message`
--

DROP TABLE IF EXISTS `djkombu_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `djkombu_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `visible` tinyint(1) NOT NULL,
  `sent_at` datetime DEFAULT NULL,
  `payload` longtext NOT NULL,
  `queue_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djkombu_message_e94d8f76` (`visible`),
  KEY `djkombu_message_88b78e52` (`sent_at`),
  KEY `djkombu_message_e18d2948` (`queue_id`),
  CONSTRAINT `queue_id_refs_id_13f7812d` FOREIGN KEY (`queue_id`) REFERENCES `djkombu_queue` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `djkombu_message`
--

LOCK TABLES `djkombu_message` WRITE;
/*!40000 ALTER TABLE `djkombu_message` DISABLE KEYS */;
INSERT INTO `djkombu_message` VALUES (51,0,'2015-05-12 12:44:00','{\"body\": \"gAJ9cQEoVQdleHBpcmVzcQJOVQN1dGNxA4hVBGFyZ3NxBF1xBVUFY2hvcmRxBk5VCWNhbGxiYWNrc3EHTlUIZXJyYmFja3NxCE5VB3Rhc2tzZXRxCU5VAmlkcQpVJDgyYjc3N2E5LWVmMmEtNDZlZi04OGE0LWIwZTFlZmNlMWYxZnELVQdyZXRyaWVzcQxLAFUEdGFza3ENVRdkYXRhbWFpbnRhaW4udGFza3MudGVzdHEOVQl0aW1lbGltaXRxD05OhlUDZXRhcRBOVQZrd2FyZ3NxEX1xEnUu\", \"headers\": {}, \"content-type\": \"application/x-python-serialize\", \"properties\": {\"body_encoding\": \"base64\", \"correlation_id\": \"82b777a9-ef2a-46ef-88a4-b0e1efce1f1f\", \"reply_to\": \"cf9de9d7-6293-3fdf-8aa5-3aa028ddfc2e\", \"delivery_info\": {\"priority\": 0, \"routing_key\": \"celery\", \"exchange\": \"celery\"}, \"delivery_mode\": 2, \"delivery_tag\": \"38b316a6-4430-49bf-9fde-a4c0a7a97aea\"}, \"content-encoding\": \"binary\"}',1);
/*!40000 ALTER TABLE `djkombu_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `djkombu_queue`
--

DROP TABLE IF EXISTS `djkombu_queue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `djkombu_queue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `djkombu_queue`
--

LOCK TABLES `djkombu_queue` WRITE;
/*!40000 ALTER TABLE `djkombu_queue` DISABLE KEYS */;
INSERT INTO `djkombu_queue` VALUES (1,'celery'),(2,'celery@gssd1.celery.pidbox');
/*!40000 ALTER TABLE `djkombu_queue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fxapi_action`
--

DROP TABLE IF EXISTS `fxapi_action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fxapi_action` (
  `key` varchar(64) NOT NULL,
  `name` varchar(128) DEFAULT NULL,
  `action_path` varchar(512) NOT NULL,
  `action_permission` varchar(20) NOT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fxapi_action`
--

LOCK TABLES `fxapi_action` WRITE;
/*!40000 ALTER TABLE `fxapi_action` DISABLE KEYS */;
INSERT INTO `fxapi_action` VALUES ('absentlist-list','Absent list','/api/absentlist/list/','Internal');
/*!40000 ALTER TABLE `fxapi_action` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fxapi_client`
--

DROP TABLE IF EXISTS `fxapi_client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fxapi_client` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `user_id` int(11) NOT NULL,
  `domain` varchar(128) DEFAULT NULL,
  `description` varchar(512) DEFAULT NULL,
  `access_key` varchar(265) DEFAULT NULL,
  `access_secret` varchar(256) DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fxapi_client_fbfc09f1` (`user_id`),
  CONSTRAINT `user_id_refs_id_8f2bcb94` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fxapi_client`
--

LOCK TABLES `fxapi_client` WRITE;
/*!40000 ALTER TABLE `fxapi_client` DISABLE KEYS */;
/*!40000 ALTER TABLE `fxapi_client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fxapi_client_actions`
--

DROP TABLE IF EXISTS `fxapi_client_actions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fxapi_client_actions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` int(11) NOT NULL,
  `action_id` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `client_id` (`client_id`,`action_id`),
  KEY `fxapi_client_actions_4a4e8ffb` (`client_id`),
  KEY `fxapi_client_actions_df94c0f0` (`action_id`),
  CONSTRAINT `action_id_refs_key_ab48d85e` FOREIGN KEY (`action_id`) REFERENCES `fxapi_action` (`key`),
  CONSTRAINT `client_id_refs_id_8791451` FOREIGN KEY (`client_id`) REFERENCES `fxapi_client` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fxapi_client_actions`
--

LOCK TABLES `fxapi_client_actions` WRITE;
/*!40000 ALTER TABLE `fxapi_client_actions` DISABLE KEYS */;
/*!40000 ALTER TABLE `fxapi_client_actions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-05-12 18:57:59
