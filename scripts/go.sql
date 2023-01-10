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
delete from kiln where error/1.0 > 50;
delete from kiln where error/1.0 < -50;

# heat_rate
# this works, but its really jumpy because my tc jumps in 1/2 degree increments
# it is super slow because of the subselect to populate temp data from 60s ago
#alter table kiln add column heat_60;
#alter table kiln add column heat_rate;
#update kiln set heat_60 = (select b.temp from kiln b where b.run_time=kiln.run_time-60);
#update kiln set heat_60 = (select b.temp from kiln b where (b.run_time/1.0)<=((kiln.run_time-60)/1.0) order by b.run_time/1.0 desc limit 1);
#update kiln set heat_rate = (temp-heat_60)*60;

# invert error
update kiln set error=error*-1.0;

# run time
select printf("%0.2f",max(run_time/1.0)/3600) as run_hours from kiln;

# average error
select avg(abs(error)) as average_error from kiln;

# heat_on time for cost calculation
# 9640W for all elements
# .056582 per kwh from ga power
select printf("%0.2f",(sum(heat_on)/3600)*9.640*.056582) as total_cost from kiln;

# what percent of the time where elements on?
select printf("%0.2f",avg(heat_on/(heat_off+heat_on))*100) as elements_on_percent from kiln;

# max temp
select max(cast(temp as float)) as max_temperature from kiln;

.output ../tmp/temps_over_time.csv
.mode csv
select temp as Temperature,target as Target,error as Error,heat_on as Heat,p as Proportional, i as Integral, d as Derivative, run_time as Time from kiln;
