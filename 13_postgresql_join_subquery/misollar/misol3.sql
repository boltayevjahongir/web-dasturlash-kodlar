-- 13-bob: Indekslar va samaradorlik

-- === Indeks yaratish ===

-- Oddiy indeks
CREATE INDEX idx_talabalar_familiya ON talabalar(familiya);

-- Noyob (unique) indeks
CREATE UNIQUE INDEX idx_talabalar_email ON talabalar(email);

-- Kompozit indeks (bir nechta ustun)
CREATE INDEX idx_talabalar_guruh_ball ON talabalar(guruh_id, ball);

-- Qisman indeks (partial index)
CREATE INDEX idx_aktiv_talabalar ON talabalar(ball)
WHERE aktiv = TRUE;

-- === Indekslar ro'yxatini ko'rish ===
SELECT
    indexname,
    tablename,
    indexdef
FROM pg_indexes
WHERE tablename = 'talabalar';

-- === EXPLAIN — so'rov rejasini ko'rish ===

-- Indekssiz so'rov
EXPLAIN ANALYZE
SELECT * FROM talabalar WHERE familiya = 'Valiyev';

-- Indeksli so'rov (tezroq ishlashi kerak)
EXPLAIN ANALYZE
SELECT * FROM talabalar WHERE familiya = 'Valiyev';

-- JOIN so'rov rejasi
EXPLAIN ANALYZE
SELECT t.ism, g.nomi
FROM talabalar t
JOIN guruhlar g ON t.guruh_id = g.id
WHERE t.ball > 80;

-- === Indeksni o'chirish ===
-- DROP INDEX idx_talabalar_familiya;

-- === VIEW (ko'rinish) yaratish ===
CREATE OR REPLACE VIEW talaba_baholar AS
SELECT
    t.ism || ' ' || t.familiya AS talaba,
    g.nomi AS guruh,
    f.nomi AS fan,
    b.baho,
    b.sana
FROM baholar b
JOIN talabalar t ON b.talaba_id = t.id
JOIN fanlar f ON b.fan_id = f.id
LEFT JOIN guruhlar g ON t.guruh_id = g.id;

-- VIEW dan foydalanish
SELECT * FROM talaba_baholar;
SELECT * FROM talaba_baholar WHERE baho = 5;
