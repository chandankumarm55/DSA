SELECT e1.name
FROM Employee e
JOIN Employee e1 ON e.managerId = e1.id
GROUP BY e.managerId
HAVING COUNT(*) >= 5;
