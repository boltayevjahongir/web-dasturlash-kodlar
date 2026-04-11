-- 12-bob: Ma'lumot yangilash va o'chirish (UPDATE, DELETE)

-- === UPDATE — ma'lumot yangilash ===

-- Bitta talabaning ballini yangilash
UPDATE talabalar
SET ball = 90.00
WHERE email = 'jasur@mail.uz';

-- Bir nechta ustunni yangilash
UPDATE talabalar
SET kurs = 2, ball = 88.50
WHERE ism = 'Gulnora' AND familiya = 'Karimova';

-- Shartli yangilash — barcha 1-kurs talabalarni
UPDATE talabalar
SET kurs = kurs + 1
WHERE kurs = 1;

-- Yangilangan qatorni ko'rish (RETURNING)
UPDATE talabalar
SET ball = ball + 5
WHERE fakultet = 'Informatika'
RETURNING ism, familiya, ball;

-- === DELETE — ma'lumot o'chirish ===

-- Bitta qatorni o'chirish
DELETE FROM talabalar
WHERE email = 'bobur@mail.uz';

-- Shartli o'chirish
DELETE FROM talabalar
WHERE ball < 60 AND aktiv = FALSE;

-- O'chirilgan qatorni ko'rish (RETURNING)
DELETE FROM talabalar
WHERE id = 5
RETURNING *;

-- Barcha ma'lumotlarni o'chirish (ehtiyot bo'ling!)
-- DELETE FROM talabalar;

-- Jadvalni to'liq tozalash (tezroq)
-- TRUNCATE TABLE talabalar RESTART IDENTITY;

-- === Jadval tuzilmasini o'zgartirish (ALTER TABLE) ===

-- Yangi ustun qo'shish
ALTER TABLE talabalar
ADD COLUMN telefon VARCHAR(20);

-- Ustun turini o'zgartirish
ALTER TABLE talabalar
ALTER COLUMN telefon TYPE VARCHAR(30);

-- Ustun nomini o'zgartirish
ALTER TABLE talabalar
RENAME COLUMN telefon TO tel_raqam;

-- Ustunni o'chirish
ALTER TABLE talabalar
DROP COLUMN IF EXISTS tel_raqam;

-- Jadval nomini o'zgartirish
-- ALTER TABLE talabalar RENAME TO students;

-- Natijani ko'rish
SELECT * FROM talabalar;
