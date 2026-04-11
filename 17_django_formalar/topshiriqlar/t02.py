# Topshiriq 2 (O'rta): Ro'yxatdan o'tish formasi validatsiya bilan

from django import forms


# 1. RoyxatForma yarating:
#    - ism (min 2 belgi)
#    - familiya (min 2 belgi)
#    - email (unikal — clean_email da tekshiring)
#    - telefon (+998 bilan boshlanishi kerak — validator)
#    - parol (min 8 belgi, raqam+harf aralash)
#    - parol_tasdiqlash (parol bilan mos kelishi kerak — clean da tekshiring)
#    - fakultet (ChoiceField)
#    - shartlar (BooleanField, required)

class RoyxatForma(forms.Form):
    pass  # Formani yozing

    # clean_email: email mavjudligini tekshirish

    # clean_ism: faqat harflardan iborat

    # clean: parollar mosligini tekshirish


# 2. royxatdan_otish_view yozing:
#    - GET: bo'sh forma
#    - POST: validate, muvaffaqiyatli bo'lsa redirect
#    - Xato bo'lsa formani qayta ko'rsating

# 3. Template yarating:
#    - Har bir maydonni alohida render qiling
#    - Xato xabarlarni qizil rangda ko'rsating
#    - To'g'ri maydonlarni yashil chegarada ko'rsating
