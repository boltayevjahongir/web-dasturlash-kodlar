-- 12-bob: Ma'lumot o'qish (SELECT, WHERE, ORDER BY)

-- Barcha talabalar
SELECT * FROM talabalar;

-- Faqat ism va familiya
SELECT ism, familiya FROM talabalar;

-- WHERE — shartli tanlash
SELECT ism, familiya, ball
FROM talabalar
WHERE ball >= 85;

-- AND / OR
SELECT ism, fakultet, ball
FROM talabalar
WHERE fakultet = 'Fizika-matematika' AND ball > 70;

SELECT ism, fakultet, ball
FROM talabalar
WHERE fakultet = 'Filologiya' OR ball >= 90;

-- LIKE — matn qidirish
SELECT ism, familiya
FROM talabalar
WHERE familiya LIKE '%ov%';

-- IN — bir nechta qiymatdan tanlash
SELECT ism, fakultet
FROM talabalar
WHERE fakultet IN ('Informatika', 'Fizika-matematika');

-- BETWEEN — oraliqdan tanlash
SELECT ism, yosh, ball
FROM talabalar
WHERE ball BETWEEN 75 AND 90;

-- ORDER BY — saralash
SELECT ism, ball
FROM talabalar
ORDER BY ball DESC;

-- ORDER BY bilan LIMIT
SELECT ism, ball
FROM talabalar
ORDER BY ball DESC
LIMIT 3;

-- OFFSET — sahifalash
SELECT ism, ball
FROM talabalar
ORDER BY ball DESC
LIMIT 3 OFFSET 3;

-- COUNT, AVG, SUM, MIN, MAX
SELECT
    COUNT(*) AS jami_talabalar,
    AVG(ball) AS ortacha_ball,
    MIN(ball) AS eng_past,
    MAX(ball) AS eng_yuqori,
    SUM(ball) AS umumiy_ball
FROM talabalar;

-- GROUP BY — guruhlash
SELECT
    fakultet,
    COUNT(*) AS soni,
    ROUND(AVG(ball), 2) AS ortacha_ball
FROM talabalar
GROUP BY fakultet
ORDER BY ortacha_ball DESC;

-- HAVING — guruhlangan natijalarni filtrlash
SELECT
    fakultet,
    COUNT(*) AS soni,
    ROUND(AVG(ball), 2) AS ortacha_ball
FROM talabalar
GROUP BY fakultet
HAVING AVG(ball) > 80;

-- DISTINCT — takrorlanmas qiymatlar
SELECT DISTINCT fakultet FROM talabalar;

-- AS — nom berish (alias)
SELECT
    ism || ' ' || familiya AS toliq_ism,
    ball AS baho,
    CASE
        WHEN ball >= 86 THEN 'A''lo'
        WHEN ball >= 71 THEN 'Yaxshi'
        WHEN ball >= 56 THEN 'Qoniqarli'
        ELSE 'Qoniqarsiz'
    END AS daraja
FROM talabalar
ORDER BY ball DESC;
