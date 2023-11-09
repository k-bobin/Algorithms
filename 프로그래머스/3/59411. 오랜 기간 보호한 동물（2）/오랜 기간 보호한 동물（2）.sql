-- 코드를 입력하세요
SELECT ins.animal_id
            ,ins.name
FROM animal_outs as outs
LEFT JOIN animal_ins as ins
ON outs.animal_id = ins.animal_id
WHERE ins.animal_id is not null
ORDER BY datediff(outs.datetime, ins.datetime) desc
LIMIT 2