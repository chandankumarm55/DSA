SELECT e.name , b.bonus 
FROM  Employee e
LEFT join Bonus b ON e.empId = b.empId
where b.bonus<1000 or b.bonus is NULL
