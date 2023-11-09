-- 코드를 입력하세요

SELECT ins.animal_id
        ,ins.animal_type
        ,ins.name
FROM animal_ins as ins
LEFT JOIN animal_outs as outs
on ins.animal_id  = outs.animal_id
WHERE sex_upon_intake LIKE 'Intact%'
        AND (sex_upon_outcome LIKE 'Spayed%' OR sex_upon_outcome LIKE 'Neutered%')
ORDER BY 1,2,3
        