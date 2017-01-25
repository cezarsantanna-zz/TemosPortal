
SELECT date_trunc('day', to_timestamp(data_realizado)),
       sum(CASE
               WHEN abastece_evento.form_id = 1 THEN form_id
           END) AS MELHORIAS,
       sum(CASE
               WHEN abastece_evento.form_id = 2 THEN form_id
           END) AS CORRETIVAS,
       sum(CASE
               WHEN abastece_evento.form_id = 3 THEN form_id
           END) AS DESINSTALAR,
       sum(CASE
               WHEN abastece_evento.form_id = 5 THEN form_id
           END) AS ANTENA915,
       sum(CASE
               WHEN abastece_evento.form_id = 6 THEN form_id
           END) AS PLANOVERAO,
       sum(CASE
               WHEN abastece_evento.form_id = 7 THEN form_id
           END) AS PREDITIVA,
       sum(CASE
               WHEN abastece_evento.form_id = 8 THEN form_id
           END) AS PREVENTIVA,
       sum(CASE
               WHEN abastece_evento.form_id = 9 THEN form_id
           END) AS ANTENA58,
       sum(CASE
               WHEN abastece_evento.form_id = 10 THEN form_id
           END) AS SINAL,
       sum(CASE
               WHEN abastece_evento.form_id = 11 THEN form_id
           END) AS ICRSURVEY,
       sum(CASE
               WHEN abastece_evento.form_id = 14 THEN form_id
           END) AS ICRINFRA,
       sum(CASE
               WHEN abastece_evento.form_id = 15 THEN form_id
           END) AS ICRCONEX
FROM abastece_evento
WHERE empresa_id = 1
GROUP BY date_trunc('day', to_timestamp(data_realizado));
