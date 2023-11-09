-- 코드를 입력하세요
SELECT a.apnt_no
        ,p.pt_name
        ,p.pt_no
        ,d.mcdp_cd
        ,d.dr_name
        ,a.apnt_ymd
FROM appointment as a 
LEFT JOIN patient as p 
ON a.pt_no = p.pt_no
LEFT JOIN doctor as d 
ON a.mddr_id =  d.dr_id
WHERE d.mcdp_cd LIKE '%CS%'
    and date_format(a.apnt_ymd, '%Y-%m-%d') = '2022-04-13'
    and a.apnt_cncl_yn = 'N'
ORDER BY 6 