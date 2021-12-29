-- create
CREATE TABLE temporary_log(
Date_Time  DATE NOT NULL,
Cpu_Count int(11) NOT NULL,
Cpu_Working_Time DOUBLE(11,3) NOT NULL,
Cpu_idle_Time DOUBLE(11,3) NOT NULL,
cpu_percent Double(11,3) NOT NULL,
Usage_cpu_count int(11) NOT NULL, 
number_of_software_interrupts_since_boot DOUBLE(11,3) NOT NULL,
number_of_system_calls_since_boot int(11) NOT NULL,
number_of_interrupts_since_boot int(11) NOT NULL,
cpu_avg_load_over_1_min DOUBLE(11,3) NOT NULL,
cpu_avg_load_over_5_min   DOUBLE(11,3) NOT NULL,
cpu_avg_load_over_15_min DOUBLE(11,3) NOT NULL,
system_total_memory BIGINT(20)NOT NULL,
system_used_memory BIGINT(20) NOT NULL,
system_free_memory BIGINT(20) NOT NULL,
system_active_memory BIGINT(20) NOT NULL,
system_inactive_memory BIGINT(20)NOT NULL,
system_buffers_memory BIGINT(20) NOT NULL,
system_cached_memory BIGINT(20) NOT NULL,
system_shared_memory BIGINT(20) NOT NULL,
system_avalible_memory BIGINT(20) NOT NULL,
disk_total_memory BIGINT(20) NOT NULL,
disk_used_memory BIGINT(20) NOT NULL,
disk_free_memory BIGINT(20) NOT NULL,
disk_read_count BIGINT(20) NOT NULL,
disk_write_count BIGINT(20) NOT NULL,
disk_read_bytes BIGINT(20) NOT NULL,
disk_write_bytes BIGINT(20) NOT NULL,
time_spent_reading_from_disk BIGINT(20) NOT NULL,
time_spent_writing_to_disk BIGINT(20) NOT NULL,
time_spent_doing_actual_Input_Output BIGINT(20) NOT NULL,
number_of_bytes_sent BIGINT(20) NOT NULL,
number_of_bytes_received BIGINT(20) NOT NULL,
number_of_packets_sent BIGINT(20) NOT NULL,
number_of_packets_recived BIGINT(20) NOT NULL,
total_number_of_errors_while_receiving BIGINT(20) NOT NULL,
total_number_of_errors_while_sending BIGINT(20) NOT NULL,
total_number_of_incoming_packets_which_were_dropped BIGINT(20) NOT NULL,
total_number_of_outgoing_packets_which_were_dropped BIGINT(20) NOT NULL,
boot_time varchar(100) NOT NULL,
user_name varchar(50) NOT NULL,
keyboard int(11) NOT NULL,
mouse int(11) NOT NULL,
technology varchar(100) NOT NULL,
files_changed int(11) NOT NULL,
PRIMARY KEY (user_name)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- load data from csv file to table
LOAD DATA LOCAL INFILE '/home/aishwarya/Desktop/mysql/LMSDB/CpuLogData2019-11-17-new.csv' INTO TABLE temporary_log FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (Date_Time ,
Cpu_Count ,
Cpu_Working_Time ,
Cpu_idle_Time ,
cpu_percent ,
Usage_cpu_count , 
number_of_software_interrupts_since_boot ,
number_of_system_calls_since_boot ,
number_of_interrupts_since_boot ,
cpu_avg_load_over_1_min,
cpu_avg_load_over_5_min  ,
cpu_avg_load_over_15_min ,
system_total_memory  ,
system_used_memory ,
system_free_memory ,
system_active_memory ,
system_inactive_memory ,
system_buffers_memory,
system_cached_memory ,
system_shared_memory ,
system_avalible_memory ,
disk_total_memory ,
disk_used_memory ,
disk_free_memory ,
disk_read_count ,
disk_write_count ,
disk_read_bytes ,
disk_write_bytes ,
time_spent_reading_from_disk ,
time_spent_writing_to_disk ,
time_spent_doing_actual_Input_Output ,
number_of_bytes_sent ,
number_of_bytes_received ,
number_of_packets_sent ,
number_of_packets_recived ,
total_number_of_errors_while_receiving ,
total_number_of_errors_while_sending ,
total_number_of_incoming_packets_which_were_dropped ,
total_number_of_outgoing_packets_which_were_dropped ,
boot_time,
user_name ,
keyboard ,
mouse ,
technology ,
files_changed 
);

--
select  * from temporary_log;
-- where
select * from temporary_log where Cpu_Count=2;

select * from temporary_log where Cpu_Count=4;

select * from temporary_log where technology='android';

--
-- union query and order by
select * from temporary_log where Cpu_Count=2
UNION
select * from temporary_log where Cpu_Count=4 order by Cpu_Count DESC;
--

-- count() and goup by
select  technology,count(user_name) from temporary_log group by technology;

-- view1

create or replace view user_task as  select user_name, technology,files_changed from 
temporary_log;

select * from user_task;
-- view2
create or replace view devices as  select user_name, keyboard,mouse from 
temporary_log;

select * from devices;

-- view3
create or replace view memory_management AS  
SELECT  user_name,system_total_memory  ,
system_used_memory ,
system_free_memory ,
system_active_memory ,
system_inactive_memory ,
system_buffers_memory,
system_cached_memory ,
system_shared_memory ,
system_avalible_memory 
from temporary_log ;

select * from memory_management;

-- view4

create or replace view disk_management As
select user_name,
disk_total_memory ,
disk_used_memory ,
disk_free_memory ,
disk_read_count ,
disk_write_count ,
disk_read_bytes ,
disk_write_bytes ,
time_spent_reading_from_disk ,
time_spent_writing_to_disk 
from temporary_log;

select * from disk_management;

--
-- view5
create or replace view cpu_management As
select
user_name,Cpu_Count ,
Cpu_Working_Time ,
Cpu_idle_Time ,
cpu_percent ,
Usage_cpu_count ,
cpu_avg_load_over_1_min,
cpu_avg_load_over_5_min  ,
cpu_avg_load_over_15_min 
from temporary_log;

select * from cpu_management;
--
-- view6

create or replace view packet_management As
select user_name,
number_of_bytes_sent ,
number_of_bytes_received ,
number_of_packets_sent ,
number_of_packets_recived ,
total_number_of_errors_while_receiving ,
total_number_of_errors_while_sending ,
total_number_of_incoming_packets_which_were_dropped ,
total_number_of_outgoing_packets_which_were_dropped 
from temporary_log;

select * from packet_management;


