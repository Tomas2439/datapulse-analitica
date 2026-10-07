SELECT
    DATE_TRUNC('month', fecha_registro) AS cohorte,
    COUNT(DISTINCT user_id) AS usuarios_registro
FROM usuarios
GROUP BY 1
ORDER BY 1;

WITH cohortes AS (
    SELECT user_id, DATE_TRUNC('month', fecha_registro) AS cohorte
    FROM usuarios
),
actividad AS (
    SELECT user_id, DATE_TRUNC('month', fecha_evento) AS mes_actividad
    FROM eventos
    WHERE tipo_evento = 'login'
)
SELECT
    c.cohorte,
    a.mes_actividad,
    COUNT(DISTINCT c.user_id) AS usuarios_activos,
    ROUND(
        COUNT(DISTINCT c.user_id) * 100.0 /
        MAX(COUNT(DISTINCT c.user_id)) OVER (PARTITION BY c.cohorte), 1
    ) AS pct_retencion
FROM cohortes c
JOIN actividad a ON c.user_id = a.user_id
WHERE a.mes_actividad >= c.cohorte
GROUP BY c.cohorte, a.mes_actividad
ORDER BY c.cohorte, a.mes_actividad;