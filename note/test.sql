-- 모든 열을 선택하는 경우
SELECT	* 
FROM 	employees;

-- 특정 열을 선택하는 경우
SELECT	employee_id, 	
		first_name, 
		last_name 
FROM 	employees;

-- 특정 테이블에서 조건에 맞는 행 선택(예제에선 department_id가 30인 데이터)
SELECT	* 
FROM 	employees 
WHERE 	department_id = 30;

-- 조건을 여러 개 사용하여 행 선택
SELECT	* 
FROM 	employees 
WHERE 	salary > 50000 
AND 	department_id = 20;

-- 행의 정렬
SELECT	* 
FROM 	employees 
ORDER BY hire_date DESC;

-- 특정 열에 별칭(alias) 사용
SELECT	first_name AS "First Name", 
		last_name AS "Last Name" 
FROM 	employees;

-- 중복된 값을 제외하고 유일한 값만 선택
SELECT DISTINCT	department_id 
FROM 			employees;

-- 특정 범위의 행 선택
SELECT	* 
FROM 	employees 
WHERE 	hire_date 
BETWEEN '01-JAN-21' AND '31-DEC-21';