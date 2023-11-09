-- 코드를 입력하세요
SELECT b.author_id
        ,a.author_name
        ,b.category
        ,sum(price * sales) as total_sales
FROM book as b
LEFT JOIN author as a 
on b.author_id = a.author_id
LEFT JOIN book_sales as s
on b.book_id = s.book_id
WHERE s.sales_date BETWEEN "2022-01-01" AND "2022-01-31"
GROUP BY 1,2,3
ORDER BY 1,3 desc;