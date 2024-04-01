create database Hotelmanagement;
show databases;
use Hotelmanagement;
create table Customer(
ref varchar(40) primary key,
name varchar(40) not null,
mother varchar(50),
gender varchar(50) not null,
post varchar(40),
mobile varchar(20) not null,
email varchar(40) not null,
nationality varchar(40),
idproof varchar(40),
idnumber varchar(40),
address varchar(100)
);
create table room(
contact varchar(20) not null,
checkin varchar(20),
checkout varchar(20),
room_type varchar(50),
roomno varchar(40) primary key,
Meal varchar(50),
NoOfdays varchar(5),
paid_tax int ,
sub_total int,
total int
);

create table Detail(
Floor varchar(20) not null,
Roomno varchar(20)not null unique,
RoomType varbinary(40)
);

CREATE TABLE register (
  fname varchar(40) NOT NULL,
  lname varchar(40) NOT NULL,
  contact varchar(40) NOT NULL,
  email varchar(40) NOT NULL,
  security_q Varchar(45) Not NULL,
  security_a Varchar(45) Not NULL,
  password varchar(40) NOT NULL
)
select * from register;