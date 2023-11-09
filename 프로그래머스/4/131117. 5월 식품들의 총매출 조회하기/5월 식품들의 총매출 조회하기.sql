-- 코드를 입력하세요
SELECT p.product_id
        ,p.product_name
        ,sum(price * amount) as total_sales
FROM food_product as p 
LEFT JOIN food_order as o 
ON p.product_id = o.product_id
WHERE o.product_id is not null
        AND month(produce_date) = 5
GROUP BY o.product_id
ORDER BY 3 desc, 1;