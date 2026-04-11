# 15-bob: Django Model yaratish — Talaba va Fan
# Bu fayl app/models.py ichiga yoziladi

from django.db import models


class Fakultet(models.Model):
    """Fakultet modeli."""
    nomi = models.CharField(max_length=100)
    kod = models.CharField(max_length=10, unique=True)
    yaratilgan = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Fakultet'
        verbose_name_plural = 'Fakultetlar'
        ordering = ['nomi']

    def __str__(self):
        return self.nomi


class Talaba(models.Model):
    """Talaba modeli — asosiy maydon turlari."""

    # CharField — qisqa matn
    ism = models.CharField(max_length=50, verbose_name="Ism")
    familiya = models.CharField(max_length=50, verbose_name="Familiya")

    # EmailField — email format
    email = models.EmailField(unique=True)

    # IntegerField — butun son
    yosh = models.IntegerField(default=18)
    kurs = models.IntegerField(default=1)

    # DecimalField — aniq kasr son
    ball = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    # BooleanField — ha/yo'q
    aktiv = models.BooleanField(default=True)

    # DateField — sana
    tugilgan_sana = models.DateField(null=True, blank=True)

    # ForeignKey — bog'lanish
    fakultet = models.ForeignKey(
        Fakultet,
        on_delete=models.CASCADE,
        related_name='talabalar',
        null=True,
        blank=True
    )

    # DateTimeField — avtomatik sana
    yaratilgan = models.DateTimeField(auto_now_add=True)
    yangilangan = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'
        ordering = ['-ball']

    def __str__(self):
        return f"{self.ism} {self.familiya}"

    def toliq_ism(self):
        return f"{self.familiya} {self.ism}"

    def baho(self):
        if self.ball >= 86:
            return "A'lo"
        elif self.ball >= 71:
            return "Yaxshi"
        elif self.ball >= 56:
            return "Qoniqarli"
        return "Qoniqarsiz"


class Fan(models.Model):
    """Fan modeli."""
    nomi = models.CharField(max_length=100)
    kredit = models.IntegerField(default=3)
    semestr = models.IntegerField()
    oqituvchi = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Fan'
        verbose_name_plural = 'Fanlar'

    def __str__(self):
        return f"{self.nomi} ({self.kredit} kredit)"


# Migratsiya buyruqlari:
# python manage.py makemigrations
# python manage.py migrate
