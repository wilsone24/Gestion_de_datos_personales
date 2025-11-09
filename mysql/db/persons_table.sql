DROP TABLE IF EXISTS persons;

CREATE TABLE
    persons (
        id_person INT AUTO_INCREMENT PRIMARY KEY,
        document_type VARCHAR(30) NOT NULL,
        document_number VARCHAR(10) NOT NULL UNIQUE,
        first_name VARCHAR(30) NOT NULL,
        second_name VARCHAR(30),
        last_name VARCHAR(60) NOT NULL,
        birth_date DATE NOT NULL,
        gender VARCHAR(25) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        phone_number VARCHAR(10) NOT NULL,
        photo_url VARCHAR(255)
    );

INSERT INTO
    persons (
        document_type,
        document_number,
        first_name,
        second_name,
        last_name,
        birth_date,
        gender,
        email,
        phone_number,
        photo_url
    )
VALUES
    (
        'Cédula',
        '1001781997',
        'Wilson',
        'Andrés',
        'Estrada',
        '1997-03-15',
        'Masculino',
        'wilson.estrada@example.com',
        '3014567890',
        'https://example.com/photos/wilson.jpg'
    ),
    (
        'Tarjeta de identidad',
        '987654321',
        'María',
        'José',
        'Gómez',
        '1995-07-22',
        'Femenino',
        'maria.gomez@example.com',
        '6781234567',
        'https://example.com/photos/maria.jpg'
    ),
    (
        'Cédula',
        '1122334455',
        'Luis',
        'Fernando',
        'Torres',
        '1988-11-05',
        'Masculino',
        'luis.torres@example.com',
        '3212233344',
        'https://example.com/photos/luis.jpg'
    ),
    (
        'Tarjeta de identidad',
        '1234567890',
        'Ana',
        'Lucía',
        'Pérez',
        '1992-02-17',
        'Femenino',
        'ana.perez@example.com',
        '3042312345',
        'https://example.com/photos/ana.jpg'
    ),
    (
        'Cédula',
        '7654321987',
        'Pedro',
        'Ignacio',
        'Ramírez',
        '1990-09-30',
        'Prefiero no reportar',
        'pedro.ramirez@example.com',
        '9876543210',
        'https://example.com/photos/pedro.jpg'
    );