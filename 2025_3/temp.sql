
with cte1 as (
select 
    id,
    height,
    rank() over (partition by id order by createdon desc) as rank_number

from empHeight)
select id, height
from cte1
where rank_number = 1

"john snow/1935"
// instr(abc, "/")

select 
    substr(abc, instr(abc, "/")-1) as name,
    substr()