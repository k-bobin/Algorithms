-- 코드를 입력하세요
SELECT outs.animal_id
        ,outs.name
FROM animal_outs as outs
LEFT JOIN animal_ins as ins
on outs.animal_id = ins.animal_id
WHERE ins.animal_id is null
ORDER BY 1