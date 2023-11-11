-- 코드를 입력하세요
# SELECT TITLE
#        ,GB.BOARD_ID
#        ,GR.REPLY_ID
#        ,GR.WRITER_ID
#        ,GR.CONTENTS
#        ,DATE_FORMAT(GR.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
# FROM USED_GOODS_BOARD AS GB JOIN USED_GOODS_REPLY AS GR
# ON GB.BOARD_ID = GR.BOARD_ID
# WHERE GB.CREATED_DATE LIKE '2022-10%'
# ORDER BY GR.CREATED_DATE ASC
#         ,GB.TITLE ASC;

SELECT
b.TITLE,
b.BOARD_ID,
r.REPLY_ID,
r.WRITER_ID,
r.CONTENTS,
DATE_FORMAT(r.CREATED_DATE, "%Y-%m-%d")
FROM USED_GOODS_BOARD b JOIN USED_GOODS_REPLY r
ON b.BOARD_ID = r.BOARD_ID
WHERE b.CREATED_DATE BETWEEN "2022-10-01" AND "2022-10-31"
ORDER BY r.CREATED_DATE, b.TITLE;