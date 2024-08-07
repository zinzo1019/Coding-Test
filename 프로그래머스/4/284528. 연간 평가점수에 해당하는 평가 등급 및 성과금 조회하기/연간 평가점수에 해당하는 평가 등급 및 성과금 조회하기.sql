SELECT HE.EMP_NO, HE.EMP_NAME
     , CASE WHEN AVG(SCORE) >= 96 THEN 'S'
            WHEN AVG(SCORE) >= 90 THEN 'A'
            WHEN AVG(SCORE) >= 80 THEN 'B'
            ELSE 'C'
       END AS GRADE
     , CASE WHEN AVG(SCORE) >= 96 THEN (20/100) * SAL
            WHEN AVG(SCORE) >= 90 THEN (15/100) * SAL
            WHEN AVG(SCORE) >= 80 THEN (10/100) * SAL
            ELSE 0
       END AS BONUS
FROM HR_EMPLOYEES HE
LEFT JOIN HR_GRADE HG
ON HE.EMP_NO = HG.EMP_NO
GROUP BY HE.EMP_NO
ORDER BY HE.EMP_NO