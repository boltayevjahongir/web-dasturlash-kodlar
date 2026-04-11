# 16-bob: Class-Based Views (CBV) misollari

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

# from .models import Maqola


# === TemplateView — oddiy shablon ===
class BoshSahifaView(TemplateView):
    template_name = 'sahifalar/bosh.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sarlavha'] = 'Bosh sahifa'
        context['xabar'] = 'CBV bilan yaratilgan!'
        return context


# === ListView — ro'yxat ===
class MaqolaListView(ListView):
    # model = Maqola
    template_name = 'blog/maqola_royxat.html'
    context_object_name = 'maqolalar'
    paginate_by = 10
    ordering = ['-yaratilgan']

    def get_queryset(self):
        """Faqat nashr etilgan maqolalar."""
        # return Maqola.objects.filter(nashr_etilgan=True)
        return []


# === DetailView — batafsil ===
class MaqolaDetailView(DetailView):
    # model = Maqola
    template_name = 'blog/maqola_batafsil.html'
    context_object_name = 'maqola'


# === CreateView — yaratish ===
class MaqolaCreateView(CreateView):
    # model = Maqola
    template_name = 'blog/maqola_forma.html'
    fields = ['sarlavha', 'matn', 'kategoriya']
    success_url = reverse_lazy('maqola_royxat')


# === UpdateView — tahrirlash ===
class MaqolaUpdateView(UpdateView):
    # model = Maqola
    template_name = 'blog/maqola_forma.html'
    fields = ['sarlavha', 'matn', 'kategoriya']
    success_url = reverse_lazy('maqola_royxat')


# === DeleteView — o'chirish ===
class MaqolaDeleteView(DeleteView):
    # model = Maqola
    template_name = 'blog/maqola_ochirish.html'
    success_url = reverse_lazy('maqola_royxat')


# === urls.py (CBV uchun) ===
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.BoshSahifaView.as_view(), name='bosh_sahifa'),
#     path('maqolalar/', views.MaqolaListView.as_view(), name='maqola_royxat'),
#     path('maqolalar/<int:pk>/', views.MaqolaDetailView.as_view(), name='maqola_batafsil'),
#     path('maqolalar/yangi/', views.MaqolaCreateView.as_view(), name='maqola_yaratish'),
#     path('maqolalar/<int:pk>/tahrir/', views.MaqolaUpdateView.as_view(), name='maqola_tahrir'),
#     path('maqolalar/<int:pk>/ochirish/', views.MaqolaDeleteView.as_view(), name='maqola_ochirish'),
# ]
