DROP TABLE IF EXISTS diagnostico;
DROP TABLE IF EXISTS atendimento;

CREATE TABLE atendimento(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(100),
    tipo_atendimento CHAR(1)
);

CREATE TABLE diagnostico(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(100),
    id_atendimento INT NOT NULL,
    CONSTRAINT fk_diagnostico FOREIGN KEY (id_atendimento) REFERENCES atendimento(id)
);
