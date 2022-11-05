.mode csv
.headers on
.import ../tmp/data.csv kiln

# get data for everything outside of the PID control window
create table out_of_window as select run_time,count(*) from kiln group by run_time having count(*)>1;
.mode box
.output ../tmp/reports.txt
select * from kiln a, out_of_window b where a.run_time=b.run_time;

# remove the first and last log entry and crazy entries
delete from kiln where run_time=0;
delete from kiln where time_left=0;
update kiln set d=0 where abs(d)>100;
delete from kiln where error/1.0 > 500;
delete from kiln where error/1.0 < -500;

# invert error
update kiln set error=error*-1.0;

# run time
select max(cast(run_time as integer))/3600 as run_hours from kiln;

# average error
select avg(abs(error)) as average_error from kiln;

# heat_on time for cost calculation
# 9640W for all elements
# .056582 per kwh from ga power
select (sum(heat_on)/3600)*9.640*.056582 as total_cost from kiln;

# what percent of the time where elements on?
select avg(heat_on/(heat_off+heat_on))*100 as elements_on_percent from kiln;

# max temp
select max(cast(temp as float)) as max_temperature from kiln;

.output ../tmp/temps_over_time.csv
.mode csv
select temp as Temperature,target as Target,error as Error,heat_on as Heat,p as Proportional, i as Integral, d as Derivative, run_time as Time from kiln;
