SELECT base.planejada,
       SUM(sum(base.MEL)) OVER (
                                ORDER BY base.planejada) AS SUM_MEL,
       SUM(sum(base.COR)) OVER (
                                ORDER BY base.planejada) AS SUM_COR,
       SUM(sum(base.DES)) OVER (
                                ORDER BY base.planejada) AS SUM_DES,
       SUM(sum(base.ANT915)) OVER (
                                   ORDER BY base.planejada) AS SUM_ANT915,
       SUM(sum(base.PLAV)) OVER (
                                 ORDER BY base.planejada) AS SUM_PLAV,
       SUM(sum(base.PRED)) OVER (
                                 ORDER BY base.planejada) AS SUM_PRED,
       SUM(sum(base.PREV)) OVER (
                                 ORDER BY base.planejada) AS SUM_PREV,
       SUM(sum(base.RET58)) OVER (
                                  ORDER BY base.planejada) AS SUM_RET58,
       SUM(sum(base.SIN)) OVER (
                                ORDER BY base.planejada) AS SUM_SIN,
       SUM(sum(base.ICRS)) OVER (
                                 ORDER BY base.planejada) AS SUM_ICRS,
       SUM(sum(base.ICRI)) OVER (
                                 ORDER BY base.planejada) AS SUM_ICRI,
       SUM(sum(base.ICRC)) OVER (
                                 ORDER BY base.planejada) AS SUM_ICRC
FROM
    (SELECT date_trunc('day', to_timestamp(data_planejado - extract(timezone
                                                                    FROM date_trunc('day', to_timestamp(data_planejado))))) AS data_planejado,
            sum(CASE
                    WHEN abastece_evento.form_id = 1 THEN 1
                    ELSE 0
                END) AS MEL,
            sum(CASE
                    WHEN abastece_evento.form_id = 2 THEN 1
                    ELSE 0
                END) AS COR,
            sum(CASE
                    WHEN abastece_evento.form_id = 3 THEN 1
                    ELSE 0
                END) AS DES,
            sum(CASE
                    WHEN abastece_evento.form_id = 5 THEN 1
                    ELSE 0
                END) AS ANT915,
            sum(CASE
                    WHEN abastece_evento.form_id = 6 THEN 1
                    ELSE 0
                END) AS PLAV,
            sum(CASE
                    WHEN abastece_evento.form_id = 7 THEN 1
                    ELSE 0
                END) AS PRED,
            sum(CASE
                    WHEN abastece_evento.form_id = 8 THEN 1
                    ELSE 0
                END) AS PREV,
            sum(CASE
                    WHEN abastece_evento.form_id = 9 THEN 1
                    ELSE 0
                END) AS RET58,
            sum(CASE
                    WHEN abastece_evento.form_id = 10 THEN 1
                    ELSE 0
                END) AS SIN,
            sum(CASE
                    WHEN abastece_evento.form_id = 11 THEN 1
                    ELSE 0
                END) AS ICRS,
            sum(CASE
                    WHEN abastece_evento.form_id = 14 THEN 1
                    ELSE 0
                END) AS ICRI,
            sum(CASE
                    WHEN abastece_evento.form_id = 15 THEN 1
                    ELSE 0
                END) AS ICRC
     FROM abastece_evento
     WHERE empresa_id = 1
     GROUP BY planejada
     ORDER BY planejada) AS base
GROUP BY base.planejada;
