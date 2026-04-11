-- 12-bob: Jadval yaratish va ma'lumot kiritish (CREATE, INSERT)
-- Bu faylni psql orqali ishga tushiring:
-- psql -d web_dasturlash -f misol1.sql

-- Ma'lumotlar bazasi yaratish (agar kerak bo'lsa)
-- CREATE DATABASE web_dasturlash;

-- Talabalar jadvali
CREATE TABLE IF NOT EXISTS talabalar (
    id          SERIAL PRIMARY KEY,
    ism         VARCHAR(50) NOT NULL,
    familiya    VARCHAR(50) NOT NULL,
    email       VARCHAR(100) UNIQUE,
    yosh        INTEGER CHECK (yosh >= 16 AND yosh <= 60),
    fakultet    VARCHAR(100),
    kurs        INTEGER DEFAULT 1,
    ball        DECIMAL(5, 2),
    aktiv       BOOLEAN DEFAULT TRUE,
    yaratilgan  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Ma'lumot kiritish — bitta qator
INSERT INTO talabalar (ism, familiya, email, yosh, fakultet, kurs, ball)
VALUES ('Ali', 'Valiyev', 'ali@mail.uz', 20, 'Fizika-matematika', 2, 85.50);

-- Ma'lumot kiritish — bir nechta qator
INSERT INTO talabalar (ism, familiya, email, yosh, fakultet, kurs, ball) VALUES
    ('Gulnora', 'Karimova', 'gulnora@mail.uz', 19, 'Filologiya', 1, 92.00),
    ('Jasur', 'Toshmatov', 'jasur@mail.uz', 21, 'Fizika-matematika', 3, 78.30),
    ('Dilnoza', 'Rahimova', 'dilnoza@mail.uz', 20, 'Tabiiy fanlar', 2, 88.75),
    ('Bobur', 'Saidov', 'bobur@mail.uz', 22, 'Fizika-matematika', 4, 65.00),
    ('Malika', 'Umarova', 'malika@mail.uz', 18, 'Filologiya', 1, 95.25),
    ('Sardor', 'Nazarov', 'sardor@mail.uz', 21, 'Tabiiy fanlar', 3, 71.50),
    ('Ziyoda', 'Aliyeva', 'ziyoda@mail.uz', 19, 'Informatika', 1, 89.00);

-- Fanlar jadvali
CREATE TABLE IF NOT EXISTS fanlar (
    id      SERIAL PRIMARY KEY,
    nomi    VARCHAR(100) NOT NULL,
    kredit  INTEGER DEFAULT 3,
    semestr INTEGER CHECK (semestr >= 1 AND semestr <= 8)
);

INSERT INTO fanlar (nomi, kredit, semestr) VALUES
    ('Web dasturlash', 4, 3),
    ('Ma''lumotlar bazasi', 3, 4),
    ('Algoritm va ma''lumot tuzilmalari', 4, 2),
    ('Kompyuter tarmoqlari', 3, 5);

-- Natijani ko'rish
SELECT * FROM talabalar;
SELECT * FROM fanlar;
