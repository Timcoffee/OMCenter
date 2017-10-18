#change user pass:
#SET PASSWORD FOR 'omcenter'@'%' = PASSWORD("123456");

#create user omcenter identified by 'OmCenter';
#create user 'omcenter'@'localhost' identified by 'OmCenter';
#create user 'omcenter'@'127.0.0.1' identified by 'OmCenter';
#create user 'omcenter'@'%' identified by 'OmCenter';
#create database omcenter;
#grant all on omcenter.* to 'omcenter'@'%';
#grant all on omcenter.* to 'omcenter'@'localhost';
#grant all on omcenter.* to 'omcenter'@'127.0.0.1';
#use omcenter;

#auth models

create table user (
    id int not null AUTO_INCREMENT,
    userName varchar(45) not null unique,
    nickName varchar(45) not null unique,
    email varchar(60) not null unique,
    phoneNum varchar(30) not null unique,
    comment text default null,
    createTimestamp DATETIME,
    updateTimestamp DATETIME,
    primary key(id)
    );

create table localAuth (
    id int not null AUTO_INCREMENT,
    uid int NOT NULL unique,
    salt varchar(45) not null,
    password varchar(256) not null,
    createTimestamp DATETIME,
    updateTimestamp DATETIME,
    primary key(id),
    foreign key (uid) references user (id)
    );

create table token (
    id int not null AUTO_INCREMENT,
    uid int not null,
    token varchar(100) not null,
    permission text not null,
    ip varchar(15) not null,
    createTimestamp DATETIME,
    updateTimestamp DATETIME,
    primary key(id),
    unique key token(uid, token),
    foreign key (uid) references user (id)
    );

create table role (
    id int NOT NULL AUTO_INCREMENT,
    role_name varchar(45) not null unique,
    comment text default null,
    createTimestamp DATETIME,
    updateTimestamp DATETIME,
    primary key(id)
    );

create table roleMember (
    id int NOT NULL AUTO_INCREMENT,
    uid int not null,
    rid int not null,
    createTimestamp DATETIME,
    updateTimestamp DATETIME,
    primary key(id),
    foreign key (uid) references user (id),
    foreign key (rid) references role (id)
    );

create table module (
    id int not null AUTO_INCREMENT,
    moduleName varchar(32) not null unique,
    nickName varchar(32) not null,
    comment text default null,
    createTimestamp DATETIME,
    updateTimestamp DATETIME,
    primary key(id)
    );

create table permission (
    id int not null AUTO_INCREMENT,
    mid int not null,
    rid int not null,
    permission int not null,
    createTimestamp DATETIME,
    updateTimestamp DATETIME,
    primary key(id),
    foreign key (mid) references module (id),
    foreign key (rid) references role (id)
    );

create table moduleRelationship (
    id int not null AUTO_INCREMENT,
    mid int not null,
    pid int not null,
    createTimestamp DATETIME,
    updateTimestamp DATETIME,
    primary key(id),
    foreign key (mid) references module (id),
    foreign key (pid) references module (id)
    );
