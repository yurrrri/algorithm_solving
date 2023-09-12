-- 코드를 입력하세요
-- MYSQL, ORACLE
# SELECT O.ANIMAL_ID, O.NAME
# FROM ANIMAL_OUTS O
# LEFT JOIN ANIMAL_INS I
# ON O.ANIMAL_ID = I.ANIMAL_ID
# WHERE I.DATETIME IS NULL
# ORDER BY O.ANIMAL_ID, O.NAME;
SELECT o.animal_id, o.name
from animal_ins i right join animal_outs o
on i.animal_id = o.animal_id
where i.datetime is null
order by o.animal_id, o.name