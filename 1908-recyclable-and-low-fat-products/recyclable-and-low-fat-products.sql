# Write your MySQL query statement below
SELECT p.product_id
From Products p
WHERE low_fats = 'Y'
AND recyclable = 'Y';