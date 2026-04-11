# 15-bob: ORM bilan CRUD — QuerySet amaliyoti
# Bu buyruqlarni Django shell da ishga tushiring:
# python manage.py shell

# from app.models import Talaba, Fakultet, Fan

# === CREATE — yaratish ===

# Usul 1: create()
# talaba = Talaba.objects.create(
#     ism="Ali",
#     familiya="Valiyev",
#     email="ali@mail.uz",
#     yosh=20,
#     ball=85.50
# )

# Usul 2: save()
# talaba = Talaba(ism="Vali", familiya="Karimov", email="vali@mail.uz")
# talaba.ball = 92.00
# talaba.save()

# Usul 3: get_or_create()
# talaba, created = Talaba.objects.get_or_create(
#     email="guli@mail.uz",
#     defaults={'ism': 'Guli', 'familiya': 'Rahimova', 'ball': 78}
# )

# === READ — o'qish ===

# Barcha yozuvlar
# talabalar = Talaba.objects.all()

# Bitta yozuv
# talaba = Talaba.objects.get(id=1)
# talaba = Talaba.objects.get(email="ali@mail.uz")

# Filtrlash
# yuqori = Talaba.objects.filter(ball__gte=85)  # ball >= 85
# fizmat = Talaba.objects.filter(fakultet__nomi="Fizika-matematika")
# aktiv = Talaba.objects.filter(aktiv=True, kurs=2)

# Chiqarib tashlash (exclude)
# boshqa = Talaba.objects.exclude(fakultet__nomi="Filologiya")

# Saralash
# tartibda = Talaba.objects.all().order_by('familiya')    # A-Z
# teskari = Talaba.objects.all().order_by('-ball')         # ball kamayish

# Limit
# birinchi_5 = Talaba.objects.all()[:5]

# Soni
# jami = Talaba.objects.count()
# aktiv_soni = Talaba.objects.filter(aktiv=True).count()

# Mavjudligini tekshirish
# bor = Talaba.objects.filter(email="ali@mail.uz").exists()

# Aggregate
# from django.db.models import Avg, Max, Min, Sum, Count
# stats = Talaba.objects.aggregate(
#     ortacha=Avg('ball'),
#     eng_yuqori=Max('ball'),
#     eng_past=Min('ball'),
#     jami=Sum('ball'),
#     soni=Count('id')
# )

# values va values_list
# ismlar = Talaba.objects.values('ism', 'familiya', 'ball')
# email_list = Talaba.objects.values_list('email', flat=True)

# Lookup turlari
# __exact     — aynan teng
# __iexact    — katta-kichik harfga e'tibor bermaydi
# __contains  — ichida bor
# __icontains — ichida bor (case-insensitive)
# __startswith, __endswith
# __gt, __gte, __lt, __lte
# __in        — ro'yxatda bor
# __range     — oraliqda
# __isnull    — NULL

# === UPDATE — yangilash ===

# Bitta yozuv
# talaba = Talaba.objects.get(id=1)
# talaba.ball = 90
# talaba.save()

# Bir nechta yozuv
# Talaba.objects.filter(kurs=1).update(kurs=2)

# === DELETE — o'chirish ===

# Bitta yozuv
# talaba = Talaba.objects.get(id=5)
# talaba.delete()

# Bir nechta yozuv
# Talaba.objects.filter(aktiv=False).delete()

print("ORM misollarini Django shell da ishga tushiring!")
print("python manage.py shell")
