SELECT 
 q.query_name,
 ROUND(SUM(q.rating/q.position) / COUNT(q.query_name),2) AS quality,
 ROUND((COALESCE((SELECT COUNT(*)
  FROM Queries q1
  WHERE q1.rating < 3
  AND q.query_name = q1.query_name
  GROUP BY q1.query_name) / COUNT(q.query_name),0)) * 100,2) AS poor_query_percentage
FROM 
 Queries q
GROUP BY 
 q.query_name
