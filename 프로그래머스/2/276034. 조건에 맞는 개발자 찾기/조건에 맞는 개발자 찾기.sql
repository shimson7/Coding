-- 코드를 작성해주세요
SELECT DISTINCT(ID), EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS D, SKILLCODES S
WHERE (D.SKILL_CODE & S.CODE )>0 AND S.NAME REGEXP 'Python|C#'
ORDER BY ID;