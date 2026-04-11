# 16-bob: Function-Based Views (FBV) misollari

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404


# === Oddiy FBV ===
def bosh_sahifa(request):
    """Bosh sahifa — template bilan."""
    context = {
        'sarlavha': 'Bosh sahifa',
        'xabar': 'Xush kelibsiz!',
    }
    return render(request, 'sahifalar/bosh.html', context)


# === Ro'yxat ko'rinishi ===
def talabalar_royxat(request):
    """Talabalar ro'yxati."""
    # from .models import Talaba
    # talabalar = Talaba.objects.all()

    # Namuna uchun:
    talabalar = [
        {'id': 1, 'ism': 'Ali', 'familiya': 'Valiyev', 'ball': 85},
        {'id': 2, 'ism': 'Vali', 'familiya': 'Karimov', 'ball': 92},
        {'id': 3, 'ism': 'Guli', 'familiya': 'Rahimova', 'ball': 78},
    ]

    context = {
        'sarlavha': 'Talabalar',
        'talabalar': talabalar,
    }
    return render(request, 'sahifalar/talabalar.html', context)


# === Batafsil ko'rinish ===
def talaba_batafsil(request, pk):
    """Bitta talaba ma'lumoti."""
    # talaba = get_object_or_404(Talaba, pk=pk)
    # context = {'talaba': talaba}
    # return render(request, 'sahifalar/talaba_batafsil.html', context)
    return HttpResponse(f"Talaba ID: {pk}")


# === GET parametrlari bilan ===
def qidirish(request):
    """Qidirish — GET parametri."""
    sorov = request.GET.get('q', '')
    # natijalar = Talaba.objects.filter(ism__icontains=sorov) if sorov else []

    context = {
        'sorov': sorov,
        # 'natijalar': natijalar,
    }
    return render(request, 'sahifalar/qidirish.html', context)


# === Redirect ===
def eski_sahifa(request):
    """Eski URL dan yangi URL ga yo'naltirish."""
    return redirect('bosh_sahifa')  # URL name bo'yicha


# === 404 xato ===
def maxsus_404(request, exception):
    """Maxsus 404 sahifa."""
    return render(request, '404.html', status=404)


# === urls.py ===
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.bosh_sahifa, name='bosh_sahifa'),
#     path('talabalar/', views.talabalar_royxat, name='talabalar'),
#     path('talabalar/<int:pk>/', views.talaba_batafsil, name='talaba_batafsil'),
#     path('qidirish/', views.qidirish, name='qidirish'),
# ]
