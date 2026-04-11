# 15-bob: ForeignKey — jadvallar bog'lanishi

from django.db import models


class Muallif(models.Model):
    """Muallif modeli."""
    ism = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.ism


class Kategoriya(models.Model):
    """Kategoriya modeli."""
    nomi = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nomi


class Maqola(models.Model):
    """Maqola modeli — ForeignKey bog'lanish."""

    sarlavha = models.CharField(max_length=200)
    matn = models.TextField()
    slug = models.SlugField(unique=True)

    # One-to-Many: Bitta muallifning ko'p maqolasi bo'ladi
    muallif = models.ForeignKey(
        Muallif,
        on_delete=models.CASCADE,
        related_name='maqolalar'
    )

    # One-to-Many: Bitta kategoriyada ko'p maqola
    kategoriya = models.ForeignKey(
        Kategoriya,
        on_delete=models.SET_NULL,
        null=True,
        related_name='maqolalar'
    )

    # Many-to-Many: Maqola bir nechta tegga ega bo'lishi mumkin
    teglar = models.ManyToManyField('Teg', blank=True, related_name='maqolalar')

    nashr_etilgan = models.BooleanField(default=False)
    yaratilgan = models.DateTimeField(auto_now_add=True)
    yangilangan = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-yaratilgan']

    def __str__(self):
        return self.sarlavha


class Teg(models.Model):
    """Teg modeli — ManyToMany bog'lanish."""
    nomi = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nomi


class Izoh(models.Model):
    """Izoh modeli — maqolaga izoh."""
    maqola = models.ForeignKey(
        Maqola,
        on_delete=models.CASCADE,
        related_name='izohlar'
    )
    muallif_ism = models.CharField(max_length=100)
    matn = models.TextField()
    yaratilgan = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-yaratilgan']

    def __str__(self):
        return f"{self.muallif_ism}: {self.matn[:50]}"


# === ORM bilan bog'lanishli so'rovlar ===
# Django shell da ishga tushiring:

# ForeignKey orqali murojaat:
# maqola = Maqola.objects.get(id=1)
# maqola.muallif              # Muallif ob'ekti
# maqola.muallif.ism          # Muallif ismi
# maqola.kategoriya.nomi      # Kategoriya nomi

# related_name orqali teskari murojaat:
# muallif = Muallif.objects.get(id=1)
# muallif.maqolalar.all()     # Shu muallifning barcha maqolalari
# muallif.maqolalar.count()   # Maqolalar soni

# ManyToMany:
# maqola.teglar.all()         # Maqolaning barcha teglari
# maqola.teglar.add(teg1, teg2)  # Teg qo'shish
# maqola.teglar.remove(teg1)     # Teg olib tashlash

# select_related (ForeignKey uchun — 1 so'rov)
# maqolalar = Maqola.objects.select_related('muallif', 'kategoriya').all()

# prefetch_related (ManyToMany va reverse FK uchun)
# maqolalar = Maqola.objects.prefetch_related('teglar', 'izohlar').all()
