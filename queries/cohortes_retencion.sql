SELECT
    DATE_TRUNC('month', fecha_registro) AS cohorte,
    COUNT(DISTINCT user_id) AS usuarios_registro
FROM usuarios
GROUP BY 1
ORDER BY 1;