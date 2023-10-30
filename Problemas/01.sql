DROP TABLE IF EXISTS stg_prontuario.paciente;

CREATE TABLE stg_prontuario.paciente (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  dt_nascimento DATE NOT NULL,
  cpf BIGINT NOT NULL,
  nome_mae VARCHAR(255) NULL,
  dt_atualizacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
