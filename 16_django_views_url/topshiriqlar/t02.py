# Topshiriq 2 (O'rta): CBV bilan blog sahifalari
# Quyidagi Class-Based Views yarating:

from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy


# 1. BoshSahifaView (TemplateView):
#    - So'nggi 5 ta maqolani context ga qo'shing
class BoshSahifaView(TemplateView):
    pass  # Kodingizni yozing


# 2. MaqolaListView (ListView):
#    - Faqat nashr_etilgan=True maqolalar
#    - Sahifalash: 5 tadan
#    - Sarlavha qidirish: GET parametr 'q' bo'yicha filter
class MaqolaListView(ListView):
    pass  # Kodingizni yozing


# 3. MaqolaDetailView (DetailView):
#    - Maqola va uning izohlarini ko'rsating
#    - context ga izohlar sonini qo'shing
class MaqolaDetailView(DetailView):
    pass  # Kodingizni yozing


# 4. Templatelar yarating:
#    - base.html (asosiy shablon)
#    - blog/maqola_royxat.html (extends base.html, for sikl, sahifalash)
#    - blog/maqola_batafsil.html (extends base.html, maqola va izohlar)

# 5. urls.py:
# urlpatterns = [
#     path('', BoshSahifaView.as_view(), name='bosh_sahifa'),
#     path('maqolalar/', MaqolaListView.as_view(), name='maqola_royxat'),
#     path('maqolalar/<int:pk>/', MaqolaDetailView.as_view(), name='maqola_batafsil'),
# ]
