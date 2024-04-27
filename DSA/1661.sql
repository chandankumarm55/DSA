select a.machine_id , 
round(AVG(b.timestamp - a.timestamp),3) as processing_time
from Activity  a
join Activity b ON a.machine_id =b.machine_id 
and
a.process_id = b.process_id
AND a.activity_type = 'start' 
              AND b.activity_type = 'end'
Group By  a.machine_id;
