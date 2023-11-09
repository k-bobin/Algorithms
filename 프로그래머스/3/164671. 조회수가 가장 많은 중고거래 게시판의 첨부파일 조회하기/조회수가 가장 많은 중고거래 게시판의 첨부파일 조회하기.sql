-- 코드를 입력하세요
SELECT concat('/home/grep/src/',
               used_goods_file.board_id,
               '/',
               used_goods_file.file_id,
               used_goods_file.file_name,
               used_goods_file.file_ext) as file_path
FROM used_goods_file
LEFT JOIN 
    (SELECT *
    FROM used_goods_board
    WHERE views in (SELECT max(views)
                    FROM used_goods_board)) as max_view
ON used_goods_file.board_id = max_view.board_id
WHERE max_view.board_id is not null
ORDER BY file_id desc