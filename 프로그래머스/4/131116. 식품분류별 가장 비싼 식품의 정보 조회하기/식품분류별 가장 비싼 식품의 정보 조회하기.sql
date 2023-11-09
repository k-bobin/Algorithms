-- 코드를 입력하세요
SELECT category
        ,price as max_price
        ,product_name
FROM 
    (SELECT *,
            rank() over (partition by category order by price desc) as ranking
    FROM food_product) as new_table
WHERE category in ('과자', '국', '김치', '식용유')
    and ranking = 1
ORDER BY 2 desc
