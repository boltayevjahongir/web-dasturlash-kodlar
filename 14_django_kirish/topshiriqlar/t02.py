# Topshiriq 2 (O'rta): Ko'p sahifali URL routing
# Quyidagi sahifalar uchun viewlar va URL routing yarating:

# 1. Bosh sahifa: /
#    "Xush kelibsiz!" xabarini ko'rsatsin

# 2. Haqida sahifasi: /haqida/
#    O'zingiz haqingizda ma'lumot ko'rsatsin

# 3. Talabalar ro'yxati: /talabalar/
#    Talabalar ro'yxatini ko'rsatsin (dictionary ro'yxatidan)

# 4. Talaba profili: /talabalar/<int:id>/
#    Bitta talaba ma'lumotini ko'rsatsin

# 5. Aloqa: /aloqa/
#    Kontakt ma'lumotlarini ko'rsatsin

# views.py
from django.http import HttpResponse


def bosh_sahifa(request):
    pass  # Kodingizni yozing


def haqida(request):
    pass  # Kodingizni yozing


def talabalar_royxati(request):
    # Namuna ma'lumotlar
    talabalar = [
        {'id': 1, 'ism': 'Ali', 'ball': 85},
        {'id': 2, 'ism': 'Vali', 'ball': 92},
    ]
    pass  # HTML formatida ro'yxatni ko'rsating


def talaba_profil(request, id):
    pass  # id bo'yicha talaba ma'lumotini ko'rsating


def aloqa(request):
    pass  # Kodingizni yozing


# urls.py
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     # URL naqshlarini yozing
# ]
