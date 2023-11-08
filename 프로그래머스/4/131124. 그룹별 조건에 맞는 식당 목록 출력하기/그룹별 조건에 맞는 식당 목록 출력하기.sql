select member_name, review_text, date_format(review_date,"%Y-%m-%d")
    from rest_review as r
        join (select a.member_id
                ,m.member_name
                ,rank() over(order by reviewcount desc) as ranking
                    from(select *
                                ,count(member_id) as reviewcount
                            from rest_review
                            group by rest_review.member_id) as a
                    join member_profile as m
                    on a.member_id=m.member_id) as c
        on r.member_id = c.member_id
where ranking = 1
order by r.review_date,r.review_text