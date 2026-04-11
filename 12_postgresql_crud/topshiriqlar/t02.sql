-- Topshiriq 2 (O'rta): Do'kon inventar tizimi
-- Quyidagi vazifalarni bajaring:

-- 1. "mahsulotlar" jadvalini yarating:
--    id, nomi, kategoriya, narx (DECIMAL), miqdor (INTEGER),
--    yetkazuvchi (VARCHAR), qo'shilgan_sana (DATE DEFAULT CURRENT_DATE)

-- 2. Kamida 12 ta mahsulot kiriting (turli kategoriyalarda)

-- 3. Quyidagi so'rovlarni yozing:
--    a) Narxi 100000 dan yuqori mahsulotlar
--    b) Miqdori 10 dan kam bo'lgan mahsulotlar (kam qolgan)
--    c) Kategoriya bo'yicha: har bir kategoriyada nechta mahsulot bor?
--    d) Eng qimmat 5 ta mahsulotni ko'rsating
--    e) Umumiy inventar qiymati (narx * miqdor yig'indisi)

-- 4. UPDATE bilan:
--    a) Bitta mahsulot narxini 10% ga oshiring
--    b) "Elektronika" kategoriyasidagi barcha mahsulotlarga 5% chegirma bering

-- 5. DELETE bilan:
--    a) Miqdori 0 bo'lgan mahsulotlarni o'chiring
