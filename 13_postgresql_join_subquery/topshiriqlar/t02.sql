-- Topshiriq 2 (O'rta): Murakkab subquery va JOIN kombinatsiyalari

-- 1. Subquery bilan: o'rtacha baho eng yuqori bo'lgan guruhni toping

-- 2. EXISTS bilan: hech qanday fan o'qimagan talabalarni toping

-- 3. CTE (WITH) bilan: har bir fandan eng yuqori baho olgan talabani toping

-- 4. Composite so'rov: Quyidagi ma'lumotlarni bitta so'rovda ko'rsating:
--    - Talaba ismi
--    - Guruh nomi
--    - Fanlar soni
--    - O'rtacha baho
--    - Eng yuqori baho
--    (GROUP BY + JOIN + aggregate funksiyalar)

-- 5. VIEW yarating: "guruh_statistika" nomi bilan
--    Har bir guruh uchun: talabalar soni, o'rtacha ball, eng yuqori ball
