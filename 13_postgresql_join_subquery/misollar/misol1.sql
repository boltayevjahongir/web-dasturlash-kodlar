-- 13-bob: JOIN turlari — INNER, LEFT, RIGHT, FULL

-- Jadvallarni yaratish
CREATE TABLE IF NOT EXISTS guruhlar (
    id      SERIAL PRIMARY KEY,
    nomi    VARCHAR(20) NOT NULL,
    yonalish VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS talabalar (
    id          SERIAL PRIMARY KEY,
    ism         VARCHAR(50) NOT NULL,
    familiya    VARCHAR(50) NOT NULL,
    guruh_id    INTEGER REFERENCES guruhlar(id),
    ball        DECIMAL(5, 2)
);

CREATE TABLE IF NOT EXISTS fanlar (
    id      SERIAL PRIMARY KEY,
    nomi    VARCHAR(100) NOT NULL,
    kredit  INTEGER DEFAULT 3
);

CREATE TABLE IF NOT EXISTS baholar (
    id          SERIAL PRIMARY KEY,
    talaba_id   INTEGER REFERENCES talabalar(id),
    fan_id      INTEGER REFERENCES fanlar(id),
    baho        INTEGER CHECK (baho >= 2 AND baho <= 5),
    sana        DATE DEFAULT CURRENT_DATE
);

-- Ma'lumotlarni kiritish
INSERT INTO guruhlar (nomi, yonalish) VALUES
    ('INF-21', 'Informatika'),
    ('FIZ-21', 'Fizika'),
    ('MAT-21', 'Matematika'),
    ('KIM-21', 'Kimyo');

INSERT INTO talabalar (ism, familiya, guruh_id, ball) VALUES
    ('Ali', 'Valiyev', 1, 85),
    ('Vali', 'Karimov', 1, 92),
    ('Guli', 'Rahimova', 2, 78),
    ('Dildora', 'Saidova', 2, 88),
    ('Eldor', 'Toshmatov', 3, 71),
    ('Farida', 'Umarova', NULL, 95);  -- Guruhsiz talaba

INSERT INTO fanlar (nomi, kredit) VALUES
    ('Web dasturlash', 4),
    ('Fizika', 3),
    ('Matematika', 4);

INSERT INTO baholar (talaba_id, fan_id, baho) VALUES
    (1, 1, 4), (1, 3, 5),
    (2, 1, 5), (2, 3, 4),
    (3, 2, 4), (3, 3, 3),
    (4, 2, 5),
    (5, 3, 3);

-- === INNER JOIN — faqat mos keladiganlar ===
SELECT
    t.ism, t.familiya, g.nomi AS guruh
FROM talabalar t
INNER JOIN guruhlar g ON t.guruh_id = g.id;
-- Farida ko'rinmaydi (guruh_id = NULL)

-- === LEFT JOIN — chapdan hammasi ===
SELECT
    t.ism, t.familiya, g.nomi AS guruh
FROM talabalar t
LEFT JOIN guruhlar g ON t.guruh_id = g.id;
-- Farida ham ko'rinadi (guruh = NULL)

-- === RIGHT JOIN — o'ngdan hammasi ===
SELECT
    g.nomi AS guruh, t.ism, t.familiya
FROM talabalar t
RIGHT JOIN guruhlar g ON t.guruh_id = g.id;
-- KIM-21 ham ko'rinadi (talabasiz)

-- === FULL OUTER JOIN — hammasini ko'rsatish ===
SELECT
    t.ism, t.familiya, g.nomi AS guruh
FROM talabalar t
FULL OUTER JOIN guruhlar g ON t.guruh_id = g.id;

-- === Ko'p jadvalini birlashtirish ===
SELECT
    t.ism || ' ' || t.familiya AS talaba,
    g.nomi AS guruh,
    f.nomi AS fan,
    b.baho
FROM baholar b
JOIN talabalar t ON b.talaba_id = t.id
JOIN fanlar f ON b.fan_id = f.id
LEFT JOIN guruhlar g ON t.guruh_id = g.id
ORDER BY t.ism, f.nomi;
