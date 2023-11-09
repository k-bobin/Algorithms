-- 코드를 입력하세요
SELECT users.user_id
        ,users.nickname
        ,board.total_sales
FROM used_goods_user as users
RIGHT JOIN 
    (SELECT writer_id
            ,sum(price) AS total_sales
    FROM used_goods_board
    WHERE STATUS = 'DONE'
    GROUP BY writer_id
    HAVING total_sales >= 700000) as board
ON users.user_id = board.writer_id
ORDER BY 3