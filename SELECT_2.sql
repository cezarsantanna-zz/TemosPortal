SELECT date_trunc('day', to_timestamp(data_realizado)),
       sum(count(form_id)) OVER (
                                 ORDER BY date_trunc('day', to_timestamp(data_realizado)))
FROM abastece_evento
WHERE empresa_id = 1
GROUP BY date_trunc('day', to_timestamp(data_realizado))
ORDER BY date_trunc('day', to_timestamp(data_realizado));
