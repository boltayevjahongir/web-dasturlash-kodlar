# Topshiriq 1 (Oson): Blog uchun model yarating
# Quyidagi modellarni yarating:

from django.db import models


# 1. Post modeli:
#    - sarlavha (CharField, max 200)
#    - matn (TextField)
#    - muallif (CharField, max 100)
#    - nashr_sanasi (DateTimeField, auto_now_add)
#    - yangilangan (DateTimeField, auto_now)
#    - chop_etilgan (BooleanField, default False)
#    - __str__ metodi — sarlavhani qaytarsin
#    - Meta: ordering = ['-nashr_sanasi']

class Post(models.Model):
    pass  # Modelni yozing


# 2. Izoh modeli:
#    - post (ForeignKey -> Post, CASCADE)
#    - muallif_ism (CharField, max 100)
#    - email (EmailField)
#    - matn (TextField)
#    - yaratilgan (DateTimeField, auto_now_add)
#    - __str__ metodi

class Izoh(models.Model):
    pass  # Modelni yozing


# 3. Migratsiya buyruqlarini yozing:
#    a) _______________
#    b) _______________
