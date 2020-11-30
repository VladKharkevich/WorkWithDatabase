CREATE DATABASE IF NOT EXISTS classroom DEFAULT CHARACTER SET utf8;
USE classroom;
CREATE TABLE IF NOT EXISTS `room`(
	`room_id` INT(10) NOT NULL,
	`name` VARCHAR(20) NOT NULL,
	PRIMARY KEY (`room_id`) 	
) ENGINE=innodb DEFAULT CHARSET=utf8;
CREATE TABLE IF NOT EXISTS `student`(
	`student_id` INT(10) NOT NULL,
	`name` VARCHAR(100) NOT NULL,
	`birthday` DATETIME NOT NULL,
	`sex` CHAR(1) NOT NULL,
	`room_id` INT(10) NOT NULL, 
	PRIMARY KEY (`student_id`),
	CONSTRAINT `student_room_id_fk`
		FOREIGN KEY (`room_id`) REFERENCES `room`(`room_id`)
		ON UPDATE CASCADE
		ON DELETE CASCADE
) ENGINE=innodb DEFAULT CHARSET=utf8;