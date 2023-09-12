-- 코드를 입력하세요
SELECT mcdp_cd 진료과코드, count(*) 5월예약건수
from appointment
where date_format(apnt_ymd, "%Y-%m") like "2022-05"
group by mcdp_cd
# having date_format(apnt_ymd, "%Y-%m") like "2022-05"
order by 5월예약건수, 진료과코드