-- 코드를 입력하세요
SELECT ins.name,
        ins.datetime
FROM animal_ins AS ins
LEFT JOIN animal_outs AS outs
ON ins.animal_id = outs.animal_id
WHERE outs.animal_id is null
ORDER BY 2
LIMIT 3