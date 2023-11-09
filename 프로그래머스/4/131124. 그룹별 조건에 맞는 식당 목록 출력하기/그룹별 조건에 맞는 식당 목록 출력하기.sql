-- 코드를 입력하세요
WITH selected_id AS (
SELECT member_id
FROM
    (SELECT member_id
            ,count(*) as review_cnt
            ,rank() over (order by count(*) desc) as ranking
    FROM rest_review
    GROUP BY member_id) AS rank_table
WHERE ranking = 1
)

SELECT member_profile.member_name,
        review_text,
        date_format(review_date, '%Y-%m-%d') as review_date
FROM rest_review 
LEFT JOIN member_profile 
on rest_review.member_id = member_profile.member_id
WHERE rest_review.member_id in (SELECT member_id 
                    FROM selected_id)
ORDER BY 3,2