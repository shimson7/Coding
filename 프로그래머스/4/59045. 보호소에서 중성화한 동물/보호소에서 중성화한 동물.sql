-- 코드를 입력하세요
-- LIKE가 안되서 REGEXP()에 대해 처음 알게됨
SELECT
    A.ANIMAL_ID,
    A.ANIMAL_TYPE,
    A.NAME
FROM ANIMAL_INS AS A
JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID=B.ANIMAL_ID
WHERE A.SEX_UPON_INTAKE REGEXP ('Intact') 
AND B.SEX_UPON_OUTCOME REGEXP ('Spayed|Neutered')
ORDER BY A.ANIMAL_ID;

# SELECT 
#     I.ANIMAL_ID,
#     I.ANIMAL_TYPE,
#     I.NAME
# FROM ANIMAL_INS I
#     JOIN ANIMAL_OUTS O
#         ON I.ANIMAL_ID = O.ANIMAL_ID
# WHERE I.SEX_UPON_INTAKE REGEXP ('Intact')
#     AND O.SEX_UPON_OUTCOME REGEXP ('Spayed|Neutered')
# ORDER BY 1
# ;