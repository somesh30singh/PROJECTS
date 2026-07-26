DROP DATABASE IF EXISTS EMPLOYEE_JOINING_FORM;
CREATE DATABASE EMPLOYEE_JOINING_FORM;
USE EMPLOYEE_JOINING_FORM;

CREATE TABLE EMPLOYEE_DETAILS(
EMP_ID INT PRIMARY KEY AUTO_INCREMENT,
FIRST_NAME VARCHAR(50),
LAST_NAME VARCHAR(50),
PHONE CHAR(10) unique ,
AGE TINYINT UNSIGNED CHECK(AGE>18),
EMAIL VARCHAR(100) unique,
ADDRESS VARCHAR(200),
NATIONALITY VARCHAR(50)
);
use employee_joining_form;
select * from employee_details;
alter table employee_details auto_increment 1;
set sql_safe_updates = 0;
update employee_details set emp_id = case
when emp_id = 3 then 2
when emp_id = 5 then 3
when emp_id = 8 then 4
else emp_id
end;
set sql_safe_updates = 1;

start transaction;
savepoint July24;

update employee_details set emp_id = 6 where emp_id = 10;
