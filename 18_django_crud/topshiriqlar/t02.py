# Topshiriq 2 (O'rta): To'liq CRUD loyiha yarating
# "Kutubxona" loyihasini yarating — kitoblar boshqaruv tizimi

# 1. Modellar (models.py):
#    - Muallif: ism, familiya, tugilgan_yil, bio
#    - Janr: nomi, slug
#    - Kitob: nomi, muallif(FK), janr(FK), yil, sahifalar, tavsif, mavjud(bool)
#    - Foydalanuvchi: ism, email
#    - Ijaraga: foydalanuvchi(FK), kitob(FK), olingan_sana, qaytarish_sana, qaytarildi(bool)

# 2. Formalar (forms.py):
#    - KitobForma (ModelForm) — barcha kerakli maydonlar bilan
#    - IjaraForma (ModelForm) — kitob va foydalanuvchi tanlash

# 3. Viewlar (views.py) — FBV yoki CBV:
#    - kitob_royxat: barcha kitoblar, qidiruv, filtrlash, sahifalash
#    - kitob_batafsil: bitta kitob, ijara tarixi
#    - kitob_yaratish: forma bilan yangi kitob qo'shish
#    - kitob_tahrirlash: mavjud kitobni tahrirlash
#    - kitob_ochirish: kitobni o'chirish (tasdiqlash bilan)
#    - ijara_qilish: kitobni ijaraga berish

# 4. Templatelar:
#    - base.html: navbar, footer, Bootstrap
#    - kitoblar/royxat.html: jadval, qidiruv, filtrlash
#    - kitoblar/batafsil.html: to'liq ma'lumot
#    - kitoblar/forma.html: yaratish/tahrirlash formasi
#    - kitoblar/ochirish.html: tasdiqlash sahifasi

# 5. URL routing (urls.py):
#    - /kitoblar/
#    - /kitoblar/<pk>/
#    - /kitoblar/yangi/
#    - /kitoblar/<pk>/tahrir/
#    - /kitoblar/<pk>/ochirish/
#    - /kitoblar/<pk>/ijara/

# 6. Admin panel:
#    - Barcha modellarni sozlang
#    - list_display, search_fields, list_filter
#    - IjaraInline bilan kitob sahifasida ijaralarni ko'rsating

# 7. Loyihani ishga tushiring va barcha CRUD operatsiyalarni test qiling
