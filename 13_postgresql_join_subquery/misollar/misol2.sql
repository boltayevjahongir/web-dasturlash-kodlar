-- 13-bob: Subquery — ichma-ich so'rovlar

-- === WHERE ichida subquery ===

-- O'rtachadan yuqori ballga ega talabalar
SELECT ism, familiya, ball
FROM talabalar
WHERE ball > (SELECT AVG(ball) FROM talabalar);

-- Web dasturlashdan baho olgan talabalar
SELECT ism, familiya
FROM talabalar
WHERE id IN (
    SELECT talaba_id
    FROM baholar
    WHERE fan_id = (SELECT id FROM fanlar WHERE nomi = 'Web dasturlash')
);

-- Hech qanday baho olmagan talabalar
SELECT ism, familiya
FROM talabalar
WHERE id NOT IN (SELECT DISTINCT talaba_id FROM baholar);

-- === FROM ichida subquery (derived table) ===

-- Har bir guruhning o'rtacha balli
SELECT
    g.nomi AS guruh,
    sub.ortacha_ball
FROM guruhlar g
JOIN (
    SELECT guruh_id, ROUND(AVG(ball), 2) AS ortacha_ball
    FROM talabalar
    WHERE guruh_id IS NOT NULL
    GROUP BY guruh_id
) sub ON g.id = sub.guruh_id
ORDER BY sub.ortacha_ball DESC;

-- === EXISTS bilan subquery ===

-- Kamida bitta 5-baho olgan talabalar
SELECT ism, familiya
FROM talabalar t
WHERE EXISTS (
    SELECT 1
    FROM baholar b
    WHERE b.talaba_id = t.id AND b.baho = 5
);

-- === Correlated subquery ===

-- Har bir talabaning eng yuqori bahosi
SELECT
    t.ism,
    t.familiya,
    (SELECT MAX(b.baho)
     FROM baholar b
     WHERE b.talaba_id = t.id) AS eng_yuqori_baho
FROM talabalar t;

-- === CTE (Common Table Expression) — WITH ===

-- A'lochi talabalar va ularning baholari
WITH alochi_talabalar AS (
    SELECT id, ism, familiya, ball
    FROM talabalar
    WHERE ball >= 85
)
SELECT
    at.ism,
    at.familiya,
    f.nomi AS fan,
    b.baho
FROM alochi_talabalar at
JOIN baholar b ON at.id = b.talaba_id
JOIN fanlar f ON b.fan_id = f.id
ORDER BY at.ism;
