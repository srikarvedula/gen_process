create database data_gen;
use data_gen;
drop database data_gen;
create table gen_table(
	random_int			int
,random_str				varchar(20)
,random_date			varchar(20)
,name_of_file 			varchar(80) 
);

select * from gen_table;
select count(*) from gen_table where name_of_file = 'data28042020001325.csv';

create table log_table(
	process_name			varchar(20)
,file_name				varchar(60)
,message			varchar(20)
,process_date		varchar(20)
);

select * from log_table;
select count(*) from log_table where message='failed'; 
select * from log_table where message='failed'; 
