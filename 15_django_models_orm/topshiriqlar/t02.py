# Topshiriq 2 (O'rta): Do'kon modellari va ORM so'rovlar

from django.db import models


# 1. Quyidagi modellarni yarating:

# Kategoriya: nomi, tavsif
class Kategoriya(models.Model):
    pass  # Modelni yozing


# Mahsulot: nomi, tavsif, narx, miqdor, kategoriya (FK), rasm, yaratilgan
class Mahsulot(models.Model):
    pass  # Modelni yozing


# Buyurtma: mijoz_ism, email, jami_summa, holat (choices), yaratilgan
class Buyurtma(models.Model):
    HOLAT_CHOICES = [
        ('yangi', 'Yangi'),
        ('tayyorlanmoqda', 'Tayyorlanmoqda'),
        ('yetkazildi', 'Yetkazildi'),
        ('bekor', 'Bekor qilingan'),
    ]
    pass  # Modelni yozing


# 2. Django shell da quyidagi ORM so'rovlarini yozing:

# a) Barcha mahsulotlarni narx bo'yicha kamayish tartibida oling

# b) Narxi 50000 dan 100000 gacha bo'lgan mahsulotlarni toping

# c) Miqdori 5 dan kam bo'lgan mahsulotlarni toping

# d) Har bir kategoriyada nechta mahsulot borligini hisoblang

# e) Barcha mahsulotlarning o'rtacha narxini toping

# f) "Yangi" holatdagi buyurtmalar sonini hisoblang

# g) Eng qimmat mahsulotni toping

# h) Bitta kategoriyaning barcha mahsulotlarini oling (related_name)
