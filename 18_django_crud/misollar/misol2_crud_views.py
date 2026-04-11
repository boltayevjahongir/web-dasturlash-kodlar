# 18-bob: CRUD viewlar to'liq misol

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
# from .models import Talaba
# from .forms import TalabaForma


# === READ — Ro'yxat (List) ===
def talaba_royxat(request):
    """Talabalar ro'yxati sahifalash bilan."""
    # talabalar_list = Talaba.objects.all()
    talabalar_list = []  # Namuna

    # Qidiruv
    sorov = request.GET.get('q', '')
    if sorov:
        pass
        # talabalar_list = talabalar_list.filter(
        #     Q(ism__icontains=sorov) | Q(familiya__icontains=sorov)
        # )

    # Sahifalash
    paginator = Paginator(talabalar_list, 10)
    sahifa = request.GET.get('sahifa')
    talabalar = paginator.get_page(sahifa)

    context = {
        'talabalar': talabalar,
        'sorov': sorov,
    }
    return render(request, 'talabalar/royxat.html', context)


# === READ — Batafsil (Detail) ===
def talaba_batafsil(request, pk):
    """Bitta talaba ma'lumoti."""
    # talaba = get_object_or_404(Talaba, pk=pk)
    # context = {'talaba': talaba}
    # return render(request, 'talabalar/batafsil.html', context)
    pass


# === CREATE — Yaratish ===
def talaba_yaratish(request):
    """Yangi talaba qo'shish."""
    if request.method == 'POST':
        # forma = TalabaForma(request.POST)
        forma = None
        if forma and forma.is_valid():
            talaba = forma.save()
            messages.success(request, f'{talaba.ism} muvaffaqiyatli qo\'shildi!')
            return redirect('talaba_batafsil', pk=talaba.pk)
    else:
        # forma = TalabaForma()
        forma = None

    return render(request, 'talabalar/forma.html', {
        'forma': forma,
        'sarlavha': 'Yangi talaba qo\'shish',
    })


# === UPDATE — Yangilash ===
def talaba_tahrirlash(request, pk):
    """Talaba ma'lumotini tahrirlash."""
    # talaba = get_object_or_404(Talaba, pk=pk)

    if request.method == 'POST':
        # forma = TalabaForma(request.POST, instance=talaba)
        forma = None
        if forma and forma.is_valid():
            forma.save()
            messages.success(request, 'Ma\'lumotlar yangilandi!')
            return redirect('talaba_batafsil', pk=pk)
    else:
        # forma = TalabaForma(instance=talaba)
        forma = None

    return render(request, 'talabalar/forma.html', {
        'forma': forma,
        'sarlavha': 'Talabani tahrirlash',
    })


# === DELETE — O'chirish ===
def talaba_ochirish(request, pk):
    """Talabani o'chirish (tasdiqlash bilan)."""
    # talaba = get_object_or_404(Talaba, pk=pk)

    if request.method == 'POST':
        # ism = talaba.ism
        # talaba.delete()
        # messages.success(request, f'{ism} o\'chirildi!')
        return redirect('talaba_royxat')

    # return render(request, 'talabalar/ochirish.html', {'talaba': talaba})
    pass


# === urls.py ===
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.talaba_royxat, name='talaba_royxat'),
#     path('<int:pk>/', views.talaba_batafsil, name='talaba_batafsil'),
#     path('yangi/', views.talaba_yaratish, name='talaba_yaratish'),
#     path('<int:pk>/tahrir/', views.talaba_tahrirlash, name='talaba_tahrirlash'),
#     path('<int:pk>/ochirish/', views.talaba_ochirish, name='talaba_ochirish'),
# ]
