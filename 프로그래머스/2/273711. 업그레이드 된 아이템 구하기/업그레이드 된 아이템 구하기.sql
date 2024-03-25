-- 코드를 작성해주세요
SELECT
    ITEM_ID
    , ITEM_NAME
    , RARITY
FROM
    ITEM_INFO
WHERE
    ITEM_ID IN (
        SELECT
            A.ITEM_ID
        FROM ITEM_TREE A
            INNER JOIN ITEM_INFO B
                ON A.PARENT_ITEM_ID = B.ITEM_ID
        WHERE
            RARITY = 'RARE'
    )
ORDER BY
    ITEM_ID DESC