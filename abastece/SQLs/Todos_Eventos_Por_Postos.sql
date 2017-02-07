select
    abastece_posto.cgmp,
    abastece_posto.name,
    abastece_form.name,
    date_trunc('day', to_timestamp(abastece_evento.data_realizado)::TIMESTAMP WITHOUT TIME ZONE) AS realizado
from
    abastece_posto left join abastece_evento on abastece_posto.id = abastece_evento.posto_id
    inner join abastece_form on abastece_evento.form_id = abastece_form.id
order by abastece_posto.cgmp