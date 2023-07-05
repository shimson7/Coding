-- 코드를 입력하세요
SELECT A.CATEGORY AS CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK AS A INNER JOIN BOOK_SALES AS B ON A.BOOK_ID=B.BOOK_ID
WHERE DATE_FORMAT(B.SALES_DATE, '%Y-%m') = '2022-01'
GROUP BY A.CATEGORY
ORDER BY A.CATEGORY;
