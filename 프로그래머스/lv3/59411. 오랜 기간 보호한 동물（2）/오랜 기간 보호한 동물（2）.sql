-- 코드를 입력하세요
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS AS A RIGHT JOIN ANIMAL_OUTS AS B ON A.ANIMAL_ID=B.ANIMAL_ID
WHERE (B.DATETIME-A.DATETIME)>0
ORDER BY (B.DATETIME-A.DATETIME) DESC
# ORDER BY (A.DATETIME-B.DATETIME)
LIMIT 2