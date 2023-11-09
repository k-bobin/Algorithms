-- 코드를 입력하세요
SELECT places.id
        ,places.name
        ,places.host_id
FROM places
RIGHT JOIN 
    (SELECT *
    FROM places
    GROUP BY host_id
    HAVING count(*)>= 2) as heavy_users
ON places.host_id = heavy_users.host_id
ORDER BY 1

