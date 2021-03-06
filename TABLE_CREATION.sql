create DATABASE BANK;
USE BANK;

CREATE TABLE BANK_DETAILS (
BID VARCHAR(20) PRIMARY KEY,
BNAME VARCHAR(50)
) ;
CREATE TABLE BRANCH_DETAILS (
BRID VARCHAR(20) PRIMARY KEY,
BID VARCHAR(20) ,
BRNAME VARCHAR(30),
BTYPE ENUM("CORPORATE" , "RETAIL") 
) ;

CREATE TABLE CUSTOMERS(
CID INT PRIMARY KEY AUTO_INCREMENT ,
CNAME VARCHAR(30),
CTYPE ENUM( "C" , "R") ,
ACC_NO BIGINT  ,
BRID VARCHAR(20) ,
PAR_ACC VARCHAR(30)  
) ;
select * from BANK_DETAILS;
SELECT * FROM BRANCH_DETAILS;
SELECT * FROM CUSTOMERS;
