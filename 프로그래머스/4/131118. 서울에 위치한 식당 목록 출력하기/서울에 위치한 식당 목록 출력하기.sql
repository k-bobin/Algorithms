-- 코드를 입력하세요
SELECT rest_info.rest_id
        , rest_info.rest_name
        , rest_info.food_type
        , rest_info.favorites
        , rest_info.address
        , rest_score.score
FROM rest_info 
LEFT JOIN 
            (SELECT rest_id
                    ,round(avg(review_score),2) as score
            FROM rest_review
            GROUP BY rest_id) as rest_score
ON rest_info.rest_id = rest_score.rest_id
WHERE rest_score.rest_id is not null
        AND address LIKE '서울%'
ORDER BY score desc
        ,favorites desc;