-- Показать работников у которых нет почты или почта не в корпоративном домене (домен dualbootpartners.com)
SELECT e."name", e.Last_name, e.Email, d."name" AS "department"
FROM Employees AS e
LEFT JOIN Departments AS d
ON d.Department_id = e.Department_id
WHERE e.Email NOT LIKE '%@dualbootpartners.com'
OR e.Email IS NULL
ORDER BY d.Department_id, e."name";

-- Получить список работников нанятых в последние 30 дней
SELECT e."name", e.Last_name, e.Email, d."name" AS "department", e.Hire_date
FROM Employees AS e
LEFT JOIN Departments AS d
ON d.Department_id = e.Department_id
WHERE e.Hire_date > CURRENT_DATE - 30
ORDER BY d.Department_id, e."name";

-- Найти максимальную и минимальную зарплату по каждому департаменту
SELECT d."name" AS "department", MAX(e.salary) AS "max salary", MIN(e.salary) AS "min salary"
FROM Departments AS d
LEFT JOIN Employees AS e
ON e.Department_id = d.Department_id
GROUP BY d.Department_id
ORDER BY d.Department_id;

-- Посчитать количество работников в каждом регионе
SELECT r."name" AS "region", COUNT(e.Employee_id) AS "number of employees"
FROM Regions AS r
JOIN Locations AS l
ON l.Region_id = r.Region_id
JOIN Departments AS d
ON d.Location_id = l.Location_id
JOIN Employees AS e
ON e.Department_id = d.Department_id
GROUP BY r.Region_id
ORDER BY r.Region_id;

-- Показать сотрудников у которых фамилия длиннее 10 символов
SELECT e.Last_name, e."name", e.Email, d."name" AS "department"
FROM Employees AS e
LEFT JOIN Departments AS d
ON d.Department_id = e.Department_id
WHERE LENGTH(e.Last_name) > 10
ORDER BY d.Department_id, e.Last_name;

-- Показать сотрудников с зарплатой выше средней по всей компании
SELECT e."name", e.Last_name, e.Salary, e.Email, d."name" AS "department"
FROM Employees AS e
LEFT JOIN Departments AS d
ON d.Department_id = e.Department_id
WHERE e.Salary > (SELECT AVG(Salary) FROM Employees)
ORDER BY e.Salary DESC, d.Department_id;