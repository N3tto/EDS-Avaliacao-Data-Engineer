WITH repetidos AS (
 SELECT nome, cpf, dt_atualizacao,
    ROW_NUMBER() OVER (PARTITION BY cpf ORDER BY dt_atualizacao DESC) AS row_num
 FROM stg_prontuario.paciente
)
SELECT nome, cpf, dt_atualizacao
FROM repetidos
WHERE row_num = 1;