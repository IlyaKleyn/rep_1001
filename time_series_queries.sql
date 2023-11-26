

--вычисление процента от целого
select sales_month,kind_of_business,
sales*100/total_sales as pct_of_total
from
(select a.sales_month, a.kind_of_business, a.sales, sum(b.sales) as total_sales
from retail_sales a join retail_sales b
on a.sales_month=b.sales_month 
and b.kind_of_business in ('Men''s clothing stores', 'Women''s clothing stores')
where a.kind_of_business in ('Men''s clothing stores', 'Women''s clothing stores')
group by 1,2,3) aa