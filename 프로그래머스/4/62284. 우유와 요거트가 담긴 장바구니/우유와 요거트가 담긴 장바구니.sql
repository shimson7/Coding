SELECT DISTINCT CART_ID
FROM CART_PRODUCTS
WHERE EXISTS (
  SELECT *
  FROM CART_PRODUCTS AS t
  WHERE t.CART_ID = CART_PRODUCTS.CART_ID
  AND t.NAME = 'Milk'
)
AND EXISTS (
  SELECT *
  FROM CART_PRODUCTS AS t
  WHERE t.CART_ID = CART_PRODUCTS.CART_ID
  AND t.NAME = 'Yogurt'
)
ORDER BY CART_ID
;
