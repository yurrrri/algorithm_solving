-- 코드를 입력하세요
SELECT product_code, sum(sales_amount * price) total
from product p, offline_sale o
where p.product_id = o.product_id
group by product_code
order by total desc, product_code