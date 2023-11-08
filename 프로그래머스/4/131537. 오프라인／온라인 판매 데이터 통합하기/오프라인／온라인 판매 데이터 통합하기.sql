SELECT DATE_FORMAT(Z.SALES_DATE,'%Y-%m-%d') AS SALES_DATE, Z.PRODUCT_ID, Z.USER_ID, Z.SALES_AMOUNT
    FROM (
            SELECT ONLINE_SALE_ID AS SALE_ID
                   ,USER_ID
                   ,PRODUCT_ID
                   ,SALES_AMOUNT
                   ,SALES_DATE
                FROM ONLINE_SALE
            UNION ALL
            SELECT OFFLINE_SALE_ID AS SALE_ID
                   ,NULL AS USER_ID
                   ,PRODUCT_ID
                   ,SALES_AMOUNT
                   ,SALES_DATE
                FROM OFFLINE_SALE
        ) AS Z
        WHERE DATE_FORMAT(Z.SALES_DATE, '%Y') =2022 
        AND DATE_FORMAT(Z.SALES_DATE, '%m') = 03
        ORDER BY SALES_DATE, PRODUCT_ID, USER_ID;