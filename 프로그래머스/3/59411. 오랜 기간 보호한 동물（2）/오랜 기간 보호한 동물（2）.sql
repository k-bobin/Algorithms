-- 코드를 입력하세요
SELECT inouts.animal_id
        ,inouts.name
FROM
    (SELECT ins.animal_id
            ,ins.name
            ,datediff(outs.datetime, ins.datetime) AS days_difference
    FROM animal_outs as outs
    LEFT JOIN animal_ins as ins
    ON outs.animal_id = ins.animal_id
    WHERE ins.animal_id is not null
    ORDER BY days_difference desc
    LIMIT 2) as inouts