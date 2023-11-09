-- 코드를 입력하세요
SELECT users_info.user_id
        ,nickname
        ,concat(city,' ',street_address1,' ',street_address2) as 전체주소
        ,concat(substr(tlno,1,3),'-',substr(tlno,4,4),'-',substr(tlno,8,4)) as 전화번호
FROM
    (SELECT writer_id
            ,count(*) as total_contents
    FROM used_goods_board as board
    GROUP BY writer_id
    HAVING  total_contents >= 3) AS selected_users
LEFT JOIN used_goods_user as users_info
on selected_users.writer_id =  users_info.user_id
ORDER BY 1 desc