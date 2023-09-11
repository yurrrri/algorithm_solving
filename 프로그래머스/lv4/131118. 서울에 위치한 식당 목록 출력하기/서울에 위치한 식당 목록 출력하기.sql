-- 코드를 입력하세요
SELECT i.rest_id, rest_name, food_type, favorites, address, round(avg(review_score), 2) score
from rest_info i
join rest_review r on i.rest_id = r.rest_id
where address like "서울%"
group by 1, 2, 3, 4, 5
order by score desc, favorites desc

# SELECT I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS, ROUND(AVG(REVIEW_SCORE),2) AS SCORE
# FROM REST_INFO I
# INNER JOIN REST_REVIEW R ON I.REST_ID = R.REST_ID
# WHERE I.ADDRESS LIKE '서울%'
# GROUP BY 1,2,3,4,5
# ORDER BY SCORE DESC, I.FAVORITES DESC