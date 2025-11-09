DROP TABLE IF EXISTS logs;

CREATE TABLE
    logs (
        id_log INT AUTO_INCREMENT PRIMARY KEY,
        document_type VARCHAR(30) NOT NULL,
        document_number VARCHAR(10) NOT NULL,
        log_type VARCHAR(50) NOT NULL,
        description VARCHAR(255) NOT NULL,
        log_date DATETIME NOT NULL
    );