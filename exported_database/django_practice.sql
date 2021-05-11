-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 11, 2021 at 10:36 AM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `django_practice`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add musician', 7, 'add_musician'),
(26, 'Can change musician', 7, 'change_musician'),
(27, 'Can delete musician', 7, 'delete_musician'),
(28, 'Can view musician', 7, 'view_musician'),
(29, 'Can add album', 8, 'add_album'),
(30, 'Can change album', 8, 'change_album'),
(31, 'Can delete album', 8, 'delete_album'),
(32, 'Can view album', 8, 'view_album');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$pV6XAup9DiGxoBzm3aj9VK$cAhJZDyaLxw/jp3iiKtkBBKY/4D1LsWEUHOjeBzXSzc=', '2021-05-10 09:44:35.452248', 1, 'sumona', '', '', 'snsbauet04@gmail.com', 1, 1, '2021-05-10 09:43:18.559283');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-05-10 09:45:36.697742', '1', 'Eric Clapton', 1, '[{\"added\": {}}]', 7, 1),
(2, '2021-05-10 09:48:24.793506', '1', 'Album_1, Rating: 3', 1, '[{\"added\": {}}]', 8, 1),
(3, '2021-05-10 16:20:48.623551', '1', 'Album_2, Rating: 3', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 8, 1),
(4, '2021-05-10 16:21:18.787403', '1', 'Album_2, Rating: 4', 2, '[{\"changed\": {\"fields\": [\"Num stars\"]}}]', 8, 1),
(5, '2021-05-10 17:02:11.878732', '2', 'Album_2, Rating: 3', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 8, 1),
(6, '2021-05-10 17:02:26.644396', '1', 'Album_1, Rating: 4', 2, '[{\"changed\": {\"fields\": [\"Name\", \"Release date\"]}}]', 8, 1),
(7, '2021-05-10 17:16:56.346775', '2', 'Zakir Hossain', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]', 7, 1),
(8, '2021-05-10 17:17:07.698909', '3', 'Album_3, Rating: 5', 2, '[]', 8, 1),
(9, '2021-05-10 17:17:33.288849', '3', 'Album3, Rating: 5', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 8, 1),
(10, '2021-05-10 17:17:40.756542', '2', 'Album2, Rating: 3', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 8, 1),
(11, '2021-05-10 17:17:48.202576', '1', 'Album1, Rating: 4', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 8, 1),
(12, '2021-05-10 17:28:42.115260', '3', 'Making Music, Rating: 4', 2, '[{\"changed\": {\"fields\": [\"Name\", \"Release date\", \"Num stars\"]}}]', 8, 1),
(13, '2021-05-10 17:29:32.974329', '2', 'Saaz, Rating: 4', 2, '[{\"changed\": {\"fields\": [\"Artist\", \"Name\", \"Release date\", \"Num stars\"]}}]', 8, 1),
(14, '2021-05-10 17:30:12.153639', '1', 'Ulplugged, Rating: 5', 2, '[{\"changed\": {\"fields\": [\"Name\", \"Release date\", \"Num stars\"]}}]', 8, 1),
(15, '2021-05-10 17:31:04.157284', '4', 'From The Craddle, Rating: 5', 1, '[{\"added\": {}}]', 8, 1),
(16, '2021-05-10 17:31:43.870560', '5', 'Pilgrim, Rating: 5', 1, '[{\"added\": {}}]', 8, 1),
(17, '2021-05-10 17:32:23.587200', '6', 'Riding with the king, Rating: 4', 1, '[{\"added\": {}}]', 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'my_app', 'musician'),
(8, 'my_app', 'album');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-05-10 09:33:19.910238'),
(2, 'auth', '0001_initial', '2021-05-10 09:33:21.453394'),
(3, 'admin', '0001_initial', '2021-05-10 09:33:21.769045'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-05-10 09:33:21.802507'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-05-10 09:33:21.835261'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-05-10 09:33:21.992337'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-05-10 09:33:22.067598'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-05-10 09:33:22.154165'),
(9, 'auth', '0004_alter_user_username_opts', '2021-05-10 09:33:22.190248'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-05-10 09:33:22.277105'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-05-10 09:33:22.282422'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-05-10 09:33:22.310144'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-05-10 09:33:22.375661'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-05-10 09:33:22.453646'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-05-10 09:33:22.552536'),
(16, 'auth', '0011_update_proxy_permissions', '2021-05-10 09:33:22.578183'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-05-10 09:33:22.672872'),
(18, 'my_app', '0001_initial', '2021-05-10 09:33:23.136600'),
(19, 'my_app', '0002_auto_20210509_0040', '2021-05-10 09:33:23.204870'),
(20, 'sessions', '0001_initial', '2021-05-10 09:33:23.311693'),
(21, 'my_app', '0003_auto_20210510_1537', '2021-05-10 09:37:16.578469'),
(22, 'my_app', '0004_auto_20210510_1539', '2021-05-10 09:39:03.601471');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('9u185o6k2dkzcdzaf04o4h8vcvq7fj6y', '.eJxVjDsOwjAQBe_iGlkO6y8lPWewdr02DiBHipMKcXcSKQW0M_PeW0RclxrXnuc4sriIQZx-GWF65rYLfmC7TzJNbZlHknsiD9vlbeL8uh7t30HFXrc15ZBMUtmQYUII2pUhG82YGBDIb1wHq8-GCmDxEJyxoJy17LUnReLzBQO-OA0:1lg2Sp:8SflWLQ1-bPx7p4T14KLL8B4E1f_Ng47gnmeRJSWzXQ', '2021-05-24 09:44:35.550295');

-- --------------------------------------------------------

--
-- Table structure for table `my_app_album`
--

DROP TABLE IF EXISTS `my_app_album`;
CREATE TABLE IF NOT EXISTS `my_app_album` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `release_date` date NOT NULL,
  `num_stars` int(11) NOT NULL,
  `artist_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `my_app_album_artist_id_4074c7df` (`artist_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `my_app_album`
--

INSERT INTO `my_app_album` (`id`, `name`, `release_date`, `num_stars`, `artist_id`) VALUES
(1, 'Ulplugged', '1992-01-01', 5, 1),
(2, 'Saaz', '1988-10-01', 4, 2),
(3, 'Making Music', '1987-01-08', 4, 2),
(4, 'From The Craddle', '1994-01-31', 5, 1),
(5, 'Pilgrim', '1998-02-02', 5, 1),
(6, 'Riding with the king', '2000-12-16', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `my_app_musician`
--

DROP TABLE IF EXISTS `my_app_musician`;
CREATE TABLE IF NOT EXISTS `my_app_musician` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `instrument` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `my_app_musician`
--

INSERT INTO `my_app_musician` (`id`, `first_name`, `last_name`, `instrument`) VALUES
(1, 'Eric', 'Clapton', 'Guitar'),
(2, 'Zakir', 'Hossain', 'Tabla');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
