# Topshiriq 1 (Oson): FBV bilan talabalar sahifasi
# Quyidagi viewlarni yozing:

from django.shortcuts import render
from django.http import HttpResponse


# 1. bosh_sahifa view:
#    - "Xush kelibsiz!" xabarini template orqali ko'rsatsin
#    - Template: templates/bosh.html (base.html dan extends qilsin)
def bosh_sahifa(request):
    pass  # Kodingizni yozing


# 2. talabalar_royxat view:
#    - Talabalar ro'yxatini template ga context sifatida uzating
#    - Template da {% for %} bilan jadvalda ko'rsating
def talabalar_royxat(request):
    talabalar = [
        {'id': 1, 'ism': 'Ali', 'ball': 85},
        {'id': 2, 'ism': 'Vali', 'ball': 92},
        {'id': 3, 'ism': 'Guli', 'ball': 78},
    ]
    pass  # Kodingizni yozing


# 3. talaba_batafsil view:
#    - pk parametri qabul qilsin
#    - Bitta talaba ma'lumotini ko'rsatsin
def talaba_batafsil(request, pk):
    pass  # Kodingizni yozing


# 4. urls.py yozing:
# urlpatterns = [
#     # URL naqshlarini qo'shing
# ]

# 5. base.html template yarating:
#    - Navbar, content block, footer
#    - Bootstrap CDN ulangan
