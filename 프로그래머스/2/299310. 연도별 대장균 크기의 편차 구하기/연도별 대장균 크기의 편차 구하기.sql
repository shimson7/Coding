-- 코드를 작성해주세요
SELECT YEAR(DIFFERENTIATION_DATE) YEAR, 
    (SELECT MAX(SIZE_OF_COLONY) FROM ECOLI_DATA WHERE YEAR(DIFFERENTIATION_DATE) = YEAR) - SIZE_OF_COLONY as YEAR_DEV,
    ID
FROM ECOLI_DATA 
ORDER BY YEAR, YEAR_DEV