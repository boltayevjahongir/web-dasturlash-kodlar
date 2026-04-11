# 18-bob: Amaliy loyiha — to'liq CRUD tizimi
# Bu fayl loyihaning umumiy tuzilmasini ko'rsatadi

LOYIHA_TUZILMASI = """
talabalar_tizimi/
    manage.py
    config/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    talabalar/
        __init__.py
        models.py       # Talaba, Fakultet modellari
        forms.py        # TalabaForma (ModelForm)
        views.py        # CRUD viewlar
        urls.py         # URL naqshlari
        admin.py        # Admin sozlash
        templates/
            talabalar/
                base.html           # Asosiy shablon
                royxat.html         # Ro'yxat (List)
                batafsil.html       # Batafsil (Detail)
                forma.html          # Yaratish/Tahrirlash formasi
                ochirish.html       # O'chirish tasdiqlash
        static/
            talabalar/
                css/style.css
                js/script.js
    static/
        css/global.css
"""

# === models.py ===
MODELS = """
from django.db import models
from django.urls import reverse

class Fakultet(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi

class Talaba(models.Model):
    ism = models.CharField(max_length=50)
    familiya = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE, related_name='talabalar')
    kurs = models.IntegerField(default=1)
    ball = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    aktiv = models.BooleanField(default=True)
    yaratilgan = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-ball']

    def __str__(self):
        return f'{self.ism} {self.familiya}'

    def get_absolute_url(self):
        return reverse('talaba_batafsil', kwargs={'pk': self.pk})
"""

# === forms.py ===
FORMS = """
from django import forms
from .models import Talaba

class TalabaForma(forms.ModelForm):
    class Meta:
        model = Talaba
        fields = ['ism', 'familiya', 'email', 'fakultet', 'kurs', 'ball']
        widgets = {
            'ism': forms.TextInput(attrs={'class': 'form-control'}),
            'familiya': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'fakultet': forms.Select(attrs={'class': 'form-select'}),
            'kurs': forms.NumberInput(attrs={'class': 'form-control'}),
            'ball': forms.NumberInput(attrs={'class': 'form-control'}),
        }
"""

# === Ishga tushirish buyruqlari ===
BUYRUQLAR = """
# 1. Loyihani yaratish
django-admin startproject config .
python manage.py startapp talabalar

# 2. settings.py ga qo'shish
# INSTALLED_APPS += ['talabalar']

# 3. Modellarni migratsiya qilish
python manage.py makemigrations
python manage.py migrate

# 4. Superuser yaratish
python manage.py createsuperuser

# 5. Serverni ishga tushirish
python manage.py runserver

# 6. Brauzerda ochish:
# http://127.0.0.1:8000/           — Bosh sahifa
# http://127.0.0.1:8000/talabalar/ — Talabalar ro'yxati
# http://127.0.0.1:8000/admin/     — Admin panel
"""

print("=== Amaliy loyiha tuzilmasi ===")
print(LOYIHA_TUZILMASI)
print("\n=== Ishga tushirish buyruqlari ===")
print(BUYRUQLAR)
