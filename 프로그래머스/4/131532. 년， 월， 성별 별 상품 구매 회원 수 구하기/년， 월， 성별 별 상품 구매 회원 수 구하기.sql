-- 코드를 입력하세요
SELECT year(sales_date) as year
        ,month(sales_date) as month
        ,info.gender
        ,count(distinct(sale.user_id)) as users
FROM online_sale as sale
INNER JOIN user_info as info
on sale.user_id = info.user_id
WHERE info.gender is not null
GROUP BY year,month, info.gender
ORDER BY 1,2,3