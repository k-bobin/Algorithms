-- 코드를 입력하세요               
WITH milk_purchase AS (
    SELECT cart_id
    FROM cart_products
    WHERE name LIKE '%Milk%'
), yogurt_purchase AS (
    SELECT cart_id
    FROM cart_products
    WHERE name LIKE '%Yogurt%'
)


SELECT m.cart_id
FROM milk_purchase as m
INNER JOIN yogurt_purchase as y
on m.cart_id = y.cart_id
ORDER BY 1
