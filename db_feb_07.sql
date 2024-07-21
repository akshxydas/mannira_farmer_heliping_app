/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - farmer_helping_app
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`farmer_helping_app` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `farmer_helping_app`;

/*Table structure for table `agricuture_office` */

DROP TABLE IF EXISTS `agricuture_office`;

CREATE TABLE `agricuture_office` (
  `office_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`office_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `agricuture_office` */

insert  into `agricuture_office`(`office_id`,`name`,`email`,`phone`,`place`,`district`) values 
(3,'anhiram','email','123','mata','knr'),
(6,'akash','akash@ak','9999','my','kanur'),
(8,'tttt','aks@akd','6338','mm','knr');

/*Table structure for table `application` */

DROP TABLE IF EXISTS `application`;

CREATE TABLE `application` (
  `application_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(100) DEFAULT NULL,
  `app_number` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `last_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`application_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `application` */

insert  into `application`(`application_id`,`date`,`app_number`,`name`,`description`,`last_date`) values 
(3,'2022-12-01','77','jkl','lkkjg','7654'),
(4,'2022-12-01','77','jkl','lkkjg','7654'),
(10,'2022-12-08','111111','aaaaaaa','deseee','2022-12-02'),
(11,'2023-01-19','12098','rice','variety of rice','12-02-2023');

/*Table structure for table `bank` */

DROP TABLE IF EXISTS `bank`;

CREATE TABLE `bank` (
  `bank_id` int(11) NOT NULL AUTO_INCREMENT,
  `bank_name` varchar(50) DEFAULT NULL,
  `acc_no` varchar(50) DEFAULT NULL,
  `pin` varchar(70) DEFAULT NULL,
  `balance` varchar(100) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`bank_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `bank` */

insert  into `bank`(`bank_id`,`bank_name`,`acc_no`,`pin`,`balance`,`user_id`) values 
(1,'aa','12334','123','2000',9),
(2,'kgb','4400 4044 4044','670706','6700',15),
(3,'sbi','927668091','6789','750',14);

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`date`,`time`,`from_id`,`to_id`,`message`) values 
(1,'2023-12-29','11:04',6,17,'hellooo'),
(2,'2023-02-09',NULL,6,17,'hiiii'),
(3,'2023-02-09','11:09:24',17,6,'sdfsdff'),
(4,'2023-02-09','15:48:43',6,17,'asdfgh'),
(5,'2023-02-09','15:48:57',17,6,'plmnkoijhb'),
(6,'2023-02-09','15:49:13',6,17,'dcvbgh'),
(7,'2023-02-09','15:54:14',15,3,'hello'),
(8,'2023-02-09','15:54:39',3,15,'hiii');

/*Table structure for table `complaint_reply` */

DROP TABLE IF EXISTS `complaint_reply`;

CREATE TABLE `complaint_reply` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmer_id` int(11) DEFAULT NULL,
  `complaint` varchar(500) DEFAULT NULL,
  `reply` varchar(500) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `complaint_reply` */

insert  into `complaint_reply`(`complaint_id`,`farmer_id`,`complaint`,`reply`,`date`) values 
(1,1,'no seed recieved','asdsdgsg','2022-08-10'),
(2,2,'subsidy issue','pending','2002-04-06'),
(3,14,'jjjjjjjjjjjjjjjj','pending','2023-01-19');

/*Table structure for table `contact` */

DROP TABLE IF EXISTS `contact`;

CREATE TABLE `contact` (
  `contact_id` int(11) NOT NULL AUTO_INCREMENT,
  `contact_name` varchar(50) DEFAULT NULL,
  `contact_number` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`contact_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `contact` */

insert  into `contact`(`contact_id`,`contact_name`,`contact_number`,`email`) values 
(1,'Abhiram','9207668081','abhiram8055u@gmail.com'),
(6,'Akash','9207487160','agashmlpta@gmail.com'),
(7,'Akshay ','6238426480','akshay@gmail.com'),
(8,'Edwin','7034188710','edwin@gmail.com'),
(9,'Arjun','8547323099','arjun@gmail.com');

/*Table structure for table `crop` */

DROP TABLE IF EXISTS `crop`;

CREATE TABLE `crop` (
  `crop_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `crop_category` varchar(100) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `link` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`crop_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `crop` */

insert  into `crop`(`crop_id`,`name`,`price`,`crop_category`,`date`,`link`) values 
(1,'ff','ff','ff','ff','ff'),
(4,'fgsh','hhff','jjj','2022-12-02','llllll'),
(5,'nnnn','ppp','ccc','2022-12-02','llll'),
(6,'rrr','nnnnkfktg','1','2022-12-02','lllll');

/*Table structure for table `enquiry` */

DROP TABLE IF EXISTS `enquiry`;

CREATE TABLE `enquiry` (
  `enquiry_id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(500) DEFAULT NULL,
  `person_name` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `contact_number` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`enquiry_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `enquiry` */

insert  into `enquiry`(`enquiry_id`,`description`,`person_name`,`date`,`contact_number`) values 
(1,'qweer','aswin','2022-07-06','9988776655'),
(3,'dddddddddddddddddd','nnnnnnnnnnnnnn','12343','9876543210'),
(4,'qqqqqqqqqqqqqqq','wwwwwwwwwwwwwwww','2023-01-13','1111111111111111'),
(5,'my tractor working','abhi','2023-01-19','9876543210'),
(6,'There is no option to give feedback.','Arjun Das P','2023-02-07','8547323068');

/*Table structure for table `faq` */

DROP TABLE IF EXISTS `faq`;

CREATE TABLE `faq` (
  `q_id` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(200) DEFAULT NULL,
  `answer` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`q_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `faq` */

insert  into `faq`(`q_id`,`question`,`answer`) values 
(1,'fg','gvv'),
(2,'ed','fc');

/*Table structure for table `farmer` */

DROP TABLE IF EXISTS `farmer`;

CREATE TABLE `farmer` (
  `farmer_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmername` varchar(60) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `house` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `pin` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`farmer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `farmer` */

insert  into `farmer`(`farmer_id`,`farmername`,`email`,`phone`,`house`,`place`,`pin`) values 
(11,'akash123','ak@emasil','7068907','mlptm','knr','67kozikode0631'),
(13,'akshay','farmer@gmail.com','9876543210','kannur','iritty','670631'),
(14,'akshaydas','akshay@gmail.com','98765432','angadikadav','angadi','670706'),
(15,'akash cv','akash@gmail.com','8765460987','mlptm','kannur','670631'),
(16,'Gokul C','gokulc@gmil.com','9876543210','puthanpura','kuthuparamba','670643'),
(17,'Arjun Das P','arjundaspalappilli@gmail.com','8547323068','Palappilli','Kanichar','670674'),
(18,'amalraj','amalrajpv479@gmail.com','9876543210','ponnarath','thalassery','670107');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `farmer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`date`,`description`,`farmer_id`) values 
(1,'2022-06-05','good app',11),
(2,'2022-04-28','bad app',14),
(4,'2023-02-08','***** 5 star yee',17);

/*Table structure for table `fertilizer` */

DROP TABLE IF EXISTS `fertilizer`;

CREATE TABLE `fertilizer` (
  `fertilizer_id` int(11) NOT NULL AUTO_INCREMENT,
  `price_list` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `link` varchar(100) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fertilizer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `fertilizer` */

insert  into `fertilizer`(`fertilizer_id`,`price_list`,`name`,`description`,`link`,`date`) values 
(1,'fce','fc','fcertrjrj','fcejrsjs','2022-12-02');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(1,'admin@gmail.com','12345','admin'),
(3,'abhiram@gmail.com','8055','officer'),
(5,'aks@akd','2693','officer'),
(6,'aks@akd','1981','officer'),
(7,'amalraj 2gmail.com','1416','officer'),
(8,'aks@akd','8576','officer'),
(14,'akshay@gmail.com','555','farmer'),
(15,'akash@gmail.com','2020','farmer'),
(16,'gokulc@gmail.com','123','farmer'),
(17,'arjundaspalappilli@gmail.com','nithyarjun','farmer'),
(18,'amalrajpv479@gmail.com','apk','farmer');

/*Table structure for table `machine` */

DROP TABLE IF EXISTS `machine`;

CREATE TABLE `machine` (
  `machine_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `link` varchar(100) DEFAULT NULL,
  `manufacture` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`machine_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `machine` */

insert  into `machine`(`machine_id`,`name`,`description`,`date`,`link`,`manufacture`) values 
(1,'akah','ddd','2022-12-02','aaa','mm'),
(3,'tractor','motor engine','2023-01-05','track.com','tata'),
(4,'coconut picker','coconut picker mechine well useful for plucking coconut from coconut tree .time saving and easy to use.','2023-02-08','','abc company');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `link` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`date`,`description`,`title`,`link`) values 
(6,'2022-12-02','dddjfjdfj','tttjfj','hfdfhdj'),
(7,'2022-12-02','on mobile','abhi','http://www.google.com'),
(9,'2023-02-08','new subsidy for rice is issued','subsidy','https://www.youtube.com/'),
(10,'2023-02-08','a well hardworking farmer with 3acres of plants thats including  coconut trees,babana tree,some vegetables,coccoand other small plants','farmer','');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `req_id` int(11) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `acc_no` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`date`,`req_id`,`amount`,`acc_no`) values 
(1,'2023-02-09',3,'1700.0','927668091'),
(2,'2023-02-09',5,'250.0','927668091');

/*Table structure for table `policy` */

DROP TABLE IF EXISTS `policy`;

CREATE TABLE `policy` (
  `policy_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(500) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `link` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`policy_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `policy` */

insert  into `policy`(`policy_id`,`title`,`description`,`date`,`link`) values 
(1,'land','only used for rice growing','2020-3-4','aaaa');

/*Table structure for table `price` */

DROP TABLE IF EXISTS `price`;

CREATE TABLE `price` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `filepath` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `price` */

insert  into `price`(`item_id`,`date`,`filepath`) values 
(1,'2022-12-01','jhd'),
(4,'2022-12-15','/static/files/20221215_141219.pdf');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `item_price` varchar(50) DEFAULT NULL,
  `item_description` varchar(200) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `farmer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`item_name`,`date`,`item_price`,`item_description`,`quantity`,`farmer_id`) values 
(10,'rice','2023-01-19','34','  palakkadan matta','6',15),
(11,'potato','2023-01-19','25','brown fresh new','200',14),
(13,'kappa','2023-01-25','25','good quality \r\nhome made','90',16);

/*Table structure for table `product_request` */

DROP TABLE IF EXISTS `product_request`;

CREATE TABLE `product_request` (
  `req_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmer_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `date` varchar(60) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`req_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `product_request` */

insert  into `product_request`(`req_id`,`farmer_id`,`product_id`,`quantity`,`date`,`status`) values 
(2,15,11,'10','2023-01-19','pending'),
(3,14,10,'50','2023-01-19','Paid'),
(4,16,11,'50','2023-01-25','pending'),
(5,14,13,'10','2023-02-09','Paid');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(50) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `stock_id` int(50) DEFAULT NULL,
  `farmer_id` int(50) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`request_id`,`date`,`stock_id`,`farmer_id`,`quantity`,`status`) values 
(1,'2023-02-06',9,14,'4','approved'),
(2,'2023-02-06',9,14,'4','pending'),
(3,'2023-02-06',12,14,'6','Paid'),
(4,'2023-02-08',11,14,'5','pending');

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `farmer_id` int(11) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `review` */

insert  into `review`(`review_id`,`farmer_id`,`description`,`date`,`product_id`) values 
(6,12,'climatic change','2023-01-19',12),
(8,12,'its true','2023-01-19',0),
(9,13,'genuine details','2023-01-19',0),
(11,15,'bad','2023-01-19',11),
(12,14,'nice product\r\n','2023-01-19',10);

/*Table structure for table `schedule` */

DROP TABLE IF EXISTS `schedule`;

CREATE TABLE `schedule` (
  `schedule_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `req_id` int(11) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`schedule_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `schedule` */

insert  into `schedule`(`schedule_id`,`date`,`time`,`req_id`,`place`) values 
(1,'122221','123',1,'ddd'),
(2,'','',0,''),
(3,'123','1111',0,'EDOOR'),
(4,'9999','8888',0,'irity'),
(5,'9999','8888',0,'iritty'),
(6,'02-12-2023','10:30 am',0,'village office');

/*Table structure for table `stocks` */

DROP TABLE IF EXISTS `stocks`;

CREATE TABLE `stocks` (
  `stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `item_id` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `office_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`stock_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `stocks` */

insert  into `stocks`(`stock_id`,`item_id`,`type`,`quantity`,`office_id`,`date`) values 
(1,1,'crop','924',2,'2022-12-15'),
(2,4,'crop','470',2,'2022-12-15'),
(3,1,'fertilizer','237',2,'2022-12-15'),
(8,5,'crop','90',2,'2023-01-05'),
(9,1,'machine','60',3,'2023-01-05'),
(10,3,'machine','5',3,'2023-01-05'),
(11,5,'crop','50',3,'2023-01-29'),
(12,1,'fertilizer','26',3,'2023-02-06');

/*Table structure for table `story` */

DROP TABLE IF EXISTS `story`;

CREATE TABLE `story` (
  `story_id` int(11) NOT NULL AUTO_INCREMENT,
  `office_id` int(11) DEFAULT NULL,
  `title` varchar(70) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `date` varchar(60) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`story_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `story` */

insert  into `story`(`story_id`,`office_id`,`title`,`description`,`date`,`type`,`image`) values 
(8,3,'the cocunut thief','the most wanted cocunut thief was caught under purushu\'s cctv','2023-02-07','story','/static/files/rs_20230207_152454.jpg'),
(9,3,'disease','new diseases is spreading','2023-02-07','news','/static/files/rs_20230207_160724.jpg'),
(10,3,'biggest jackfruit','the biggest jackfruit according to the previous year report ','2023-02-07','story','/static/files/rs_20230207_160946.jpg'),
(11,3,'new crop found','a new variety of crop was discoverd ','2023-02-07','story','/static/files/rs_20230207_161138.jpg');

/*Table structure for table `subsidy` */

DROP TABLE IF EXISTS `subsidy`;

CREATE TABLE `subsidy` (
  `subsidy_id` int(11) NOT NULL AUTO_INCREMENT,
  `subsidy_name` varchar(100) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `date_of_issue` varchar(50) DEFAULT NULL,
  `last_date` varchar(50) DEFAULT NULL,
  `eligibility` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`subsidy_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `subsidy` */

insert  into `subsidy`(`subsidy_id`,`subsidy_name`,`description`,`date_of_issue`,`last_date`,`eligibility`) values 
(1,'dgd','dhd','2022-12-01','dd','ede'),
(5,'sssss','t789','2022-12-02','2022-09-04','eli'),
(6,'','','2022-12-08','','');

/*Table structure for table `tool` */

DROP TABLE IF EXISTS `tool`;

CREATE TABLE `tool` (
  `tool_id` int(11) NOT NULL AUTO_INCREMENT,
  `office_id` int(11) DEFAULT NULL,
  `tool_name` varchar(50) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`tool_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `tool` */

insert  into `tool`(`tool_id`,`office_id`,`tool_name`,`quantity`,`description`,`price`) values 
(1,NULL,'pick axe','23','medium size , iron alloy','14.7'),
(2,NULL,'malappuram kathi','23','highly sharpness,used by pavanayi','2500000'),
(3,NULL,'basket','50','useful for  storing fertilizers','300'),
(4,NULL,'fertilizer mixer','12','used for mixing fertilizers','1000'),
(6,NULL,'seed separator','15','used for separating different types of seeds','750');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
