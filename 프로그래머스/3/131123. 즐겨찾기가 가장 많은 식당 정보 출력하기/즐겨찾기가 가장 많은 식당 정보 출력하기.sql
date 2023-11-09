-- 코드를 입력하세요
# SELECT food_type
#         ,rest_id
#         ,rest_name
#         ,favorites
# FROM rest_info
# WHERE favorites IN (SELECT MAX(favorites)
#                     FROM rest_info
#                     GROUP BY food_type)
# GROUP BY food_type
# ORDER BY food_type DESC

SELECT food_type
        ,rest_id
        ,rest_name
        ,favorites
FROM
    (SELECT *
            ,RANK () OVER (PARTITION BY food_type
                            ORDER BY favorites DESC
                            ) as favorite_rank 
    FROM rest_info) as rank_table
WHERE favorite_rank = 1
ORDER BY 1 desc