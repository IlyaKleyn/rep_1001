
with c as (select pr1.Start_Date,pr2.End_Date, pr2.End_Date - pr1.Start_Date as duration
from Projects pr1 join Projects pr2
on pr1.Task_ID<>pr2.Task_ID
where pr1.End_Date=pr2.Start_Date
union all
select pr3.Start_Date,pr3.End_Date, pr3.End_Date - pr3.Start_Date
from Projects pr3
where datediff(pr3.End_Date, pr3.Start_Date)=1)
select 
case when c.End_Date = lead(c.Start_Date) over(order by c.Start_Date) and 
c.Start_Date = lag(c.End_Date) over(order by c.Start_Date)
then c.End_Date end as end_dt,
case when c.Start_Date = lag(c.End_Date) over(order by c.Start_Date) and 
c.End_Date = lead(c.Start_Date) over(order by c.Start_Date) 
then c.Start_Date end as start_dt
from c 

with start_dts as (
    select Start_Date,
    RANK() over (order by Start_Date) as start_rnk
    from 
    Projects where Start_Date not in (select End_Date from 
    Projects)
), with end_dts as (
    select End_Date,
    RANK() over (order by End_Date) as end_rnk
    from 
    Projects where End_Date not in (select Start_Date from 
    Projects)
)
select Start_Date, start_rnk, End_Date, end_rnk
from start_dts, end_dts
--where start_rnk=end_rnk
--and 


with maxi_from_several_chall as (
    select a.hacker_id,a.challenge_id, 
                max(a.score) over(partition by a.hacker_id) as maxi_score
from Submissions a group by 1
having count(a.challenge_id)>1), rest_scores as (
select hacker_id, score from Submissions 
    where challenge_id not in 
    (select challenge_id from maxi_from_several_chall)
) 
select * from rest_scores