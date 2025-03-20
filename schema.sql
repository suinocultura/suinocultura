CREATE TABLE suinos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    raca VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    peso DECIMAL(5,2) NOT NULL,
    sexo CHAR(1) NOT NULL,
    status VARCHAR(20) DEFAULT 'Ativo'
);

CREATE TABLE vacinas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    suino_id INT,
    vacina VARCHAR(100) NOT NULL,
    data_aplicacao DATE NOT NULL,
    FOREIGN KEY (suino_id) REFERENCES suinos(id)
);

CREATE TABLE peso_historico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    suino_id INT,
    peso DECIMAL(5,2) NOT NULL,
    data_pesagem DATE NOT NULL,
    FOREIGN KEY (suino_id) REFERENCES suinos(id)
);

CREATE TABLE reproducao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    matriz_id INT,
    data_inseminacao DATE NOT NULL,
    data_parto_previsto DATE,
    status VARCHAR(20),
    FOREIGN KEY (matriz_id) REFERENCES suinos(id)
);
