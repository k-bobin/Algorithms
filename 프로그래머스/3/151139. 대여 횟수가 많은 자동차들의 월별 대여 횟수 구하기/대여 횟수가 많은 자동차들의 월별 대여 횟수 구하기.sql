# -- 코드를 입력하세요
SELECT month(start_date) as month
        ,history.car_id
        ,count(*) as records
FROM car_rental_company_rental_history as history 
WHERE history.car_id IN
                    (SELECT car_id
                    FROM car_rental_company_rental_history
                    WHERE start_date between '2022-08-01' and '2022-10-31'
                    GROUP BY car_id
                    HAVING count(*) >= 5)
    AND history.start_date between '2022-08-01' and '2022-10-31'
GROUP BY month,
         history.car_id
ORDER BY 1,
         2 desc
         
