SELECT flavor
FROM
    (
        SELECT *
        FROM july
        UNION ALL
        SELECT *
        FROM first_half
    ) A
GROUP BY flavor
ORDER BY SUM(total_order) DESC
LIMIT 3
;