# Topshiriq 1 (Oson): Admin panelni sozlang
# Quyidagi modellar uchun admin panelni sozlang:

from django.contrib import admin


# Berilgan modellar (models.py da):
# class Kategoriya(models.Model):
#     nomi = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)
#
# class Mahsulot(models.Model):
#     nomi = models.CharField(max_length=200)
#     tavsif = models.TextField()
#     narx = models.DecimalField(max_digits=10, decimal_places=2)
#     miqdor = models.IntegerField(default=0)
#     kategoriya = models.ForeignKey(Kategoriya, on_delete=models.CASCADE)
#     aktiv = models.BooleanField(default=True)
#     yaratilgan = models.DateTimeField(auto_now_add=True)


# 1. KategoriyaAdmin yarating:
#    - list_display: nomi, slug, mahsulotlar_soni (maxsus metod)
#    - prepopulated_fields: slug -> nomi
#    - search_fields: nomi

# 2. MahsulotAdmin yarating:
#    - list_display: nomi, kategoriya, narx, miqdor, aktiv
#    - list_filter: kategoriya, aktiv
#    - search_fields: nomi, tavsif
#    - list_editable: narx, miqdor, aktiv
#    - list_per_page: 20
#    - fieldsets: Asosiy, Narx va miqdor, Holat

# 3. Admin sayt sarlavhasini o'zgartiring

# class KategoriyaAdmin(admin.ModelAdmin):
#     pass  # Sozlamalarni yozing

# class MahsulotAdmin(admin.ModelAdmin):
#     pass  # Sozlamalarni yozing
