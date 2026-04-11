-- Topshiriq 1 (Oson): Kutubxona ma'lumotlar bazasini yarating
-- Quyidagi vazifalarni bajaring:

-- 1. "kutubxona" ma'lumotlar bazasini yarating

-- 2. "kitoblar" jadvalini yarating:
--    id (SERIAL PRIMARY KEY)
--    nomi (VARCHAR, NOT NULL)
--    muallif (VARCHAR, NOT NULL)
--    yil (INTEGER)
--    sahifalar_soni (INTEGER)
--    janr (VARCHAR)
--    mavjud (BOOLEAN DEFAULT TRUE)

-- 3. Kamida 8 ta kitob ma'lumotini kiriting (INSERT)

-- 4. Quyidagi so'rovlarni yozing:
--    a) Barcha kitoblarni ko'rsating
--    b) Faqat mavjud kitoblarni ko'rsating
--    c) 2020-yildan keyin chiqgan kitoblarni ko'rsating
--    d) Janr bo'yicha guruhlang va har bir janrdagi kitoblar sonini ko'rsating
--    e) Muallif bo'yicha alifbo tartibida saralang
