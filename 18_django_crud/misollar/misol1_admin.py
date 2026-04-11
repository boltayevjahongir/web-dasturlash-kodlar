# 18-bob: Django Admin panel sozlash
# Bu fayl app/admin.py ichiga yoziladi

from django.contrib import admin
# from .models import Talaba, Fan, Fakultet, Baho


# === Oddiy registratsiya ===
# admin.site.register(Fan)


# === ModelAdmin bilan sozlangan admin ===
# @admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    """Talaba admin paneli sozlamasi."""

    # Ro'yxatda ko'rinadigan ustunlar
    list_display = ['ism', 'familiya', 'email', 'fakultet', 'kurs', 'ball', 'aktiv']

    # Filtrlash paneli
    list_filter = ['fakultet', 'kurs', 'aktiv']

    # Qidiruv maydonlari
    search_fields = ['ism', 'familiya', 'email']

    # Ro'yxatda tahrirlash
    list_editable = ['ball', 'aktiv']

    # Har sahifada nechta
    list_per_page = 20

    # Saralash
    ordering = ['-ball']

    # Slug avtomatik to'ldirish
    # prepopulated_fields = {'slug': ('ism', 'familiya')}

    # Maydonlar guruhlash
    fieldsets = (
        ('Shaxsiy ma\'lumotlar', {
            'fields': ('ism', 'familiya', 'email', 'tugilgan_sana')
        }),
        ('Ta\'lim ma\'lumotlari', {
            'fields': ('fakultet', 'kurs', 'ball')
        }),
        ('Holat', {
            'fields': ('aktiv',),
            'classes': ('collapse',),  # Yig'iluvchi bo'lim
        }),
    )

    # Faqat o'qish uchun maydonlar
    readonly_fields = ['yaratilgan', 'yangilangan']

    # Harakatlar
    actions = ['faollashtirish', 'nofaollashtirish']

    @admin.action(description='Tanlangan talabalarni faollashtirish')
    def faollashtirish(self, request, queryset):
        queryset.update(aktiv=True)

    @admin.action(description='Tanlangan talabalarni nofaollashtirish')
    def nofaollashtirish(self, request, queryset):
        queryset.update(aktiv=False)


# === Inline admin (bog'langan model) ===
# class BahoInline(admin.TabularInline):
#     model = Baho
#     extra = 1  # Bo'sh qatorlar soni
#     fields = ['fan', 'baho', 'sana']


# @admin.register(Fakultet)
class FakultetAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'kod', 'talabalar_soni']
    search_fields = ['nomi']
    # inlines = [TalabaInline]  # Inline ko'rsatish

    def talabalar_soni(self, obj):
        return obj.talabalar.count()
    talabalar_soni.short_description = 'Talabalar soni'


# === Admin sayt sozlamalari ===
admin.site.site_header = "Web Dasturlash — Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Boshqaruv paneli"

# Superuser yaratish:
# python manage.py createsuperuser
