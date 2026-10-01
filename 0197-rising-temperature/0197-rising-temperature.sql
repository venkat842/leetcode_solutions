SELECT id
FROM weather w1
WHERE 
 temperature > 
 (SELECT temperature
  FROM weather w2
  WHERE w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL  1 DAY))