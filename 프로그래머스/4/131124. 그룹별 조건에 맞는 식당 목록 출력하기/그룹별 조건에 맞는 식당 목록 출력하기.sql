-- 코드를 입력하세요
# WITH selected_id AS (
# SELECT member_id
# FROM
#     (SELECT member_id
#             ,count(*) as review_cnt
#             ,rank() over (order by count(*) desc) as ranking
#     FROM rest_review
#     GROUP BY member_id) AS rank_table
# WHERE ranking = 1
# )

# SELECT member_profile.member_name,
#         review_text,
#         date_format(review_date, '%Y-%m-%d') as review_date
# FROM rest_review 
# LEFT JOIN member_profile 
# on rest_review.member_id = member_profile.member_id
# WHERE rest_review.member_id in (SELECT member_id 
#                     FROM selected_id)
# ORDER BY 3,2


WITH c1 AS(
    SELECT member_id, DENSE_RANK() OVER(ORDER BY COUNT(member_id) DESC) ranking
    FROM REST_REVIEW 
    GROUP BY member_id
)
SELECT member_name, review_text, DATE_FORMAT(review_date, '%Y-%m-%d') review_date # SUBSTR(review_date, 1, 10)
FROM MEMBER_PROFILE m 
JOIN c1 ON m.member_id = c1.member_id
JOIN REST_REVIEW r ON m.member_id = r.member_id
WHERE ranking = 1
ORDER BY review_date, review_text;