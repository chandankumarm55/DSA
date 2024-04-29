select st.student_id , st.student_name, su.subject_name ,
COUNT(e.student_id) AS attended_exams
from Students st cross join 
Subjects su left join 
Examinations e on st.student_id = e.student_id and su.subject_name = e.subject_name
group by 
st.student_id,
st.student_name,
su.subject_name
order by 
st.student_id,
su.subject_name
