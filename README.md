# Web dasturlash va dizayn — Kod misollar repozitoriyasi

Bu repozitoriya **"Web dasturlash va dizayn"** o'quv qo'llanmasiga ilova sifatida tayyorlangan kod misollar to'plamidir. Har bir bob uchun alohida papkada misollar va topshiriqlar joylashtirilgan.

## Muallif

**Boltayev Jahongir Erkin o'g'li**
Termiz davlat universiteti (TerDU)

## Mundarija

| # | Bob nomi | Papka |
|---|----------|-------|
| 1 | Web texnologiyalar tarixi | [`01_web_texnologiyalar_tarixi`](01_web_texnologiyalar_tarixi/) |
| 2 | HTML tuzilmasi | [`02_html_tuzilmasi`](02_html_tuzilmasi/) |
| 3 | CSS sintaksisi | [`03_css_sintaksisi`](03_css_sintaksisi/) |
| 4 | Flexbox, Grid, responsiv dizayn | [`04_flexbox_grid_responsiv`](04_flexbox_grid_responsiv/) |
| 5 | JavaScript o'zgaruvchilar | [`05_javascript_ozgaruvchilar`](05_javascript_ozgaruvchilar/) |
| 6 | JavaScript operatorlar | [`06_javascript_operatorlar`](06_javascript_operatorlar/) |
| 7 | JavaScript shart va takrorlash | [`07_javascript_shart_takrorlash`](07_javascript_shart_takrorlash/) |
| 8 | Funksiyalar va massivlar | [`08_javascript_funksiyalar_massivlar`](08_javascript_funksiyalar_massivlar/) |
| 9 | DOM, hodisalar, interaktivlik | [`09_dom_hodisalar_interaktivlik`](09_dom_hodisalar_interaktivlik/) |
| 10 | Bootstrap asoslari | [`10_bootstrap_asoslari`](10_bootstrap_asoslari/) |
| 11 | Bootstrap responsiv dizayn | [`11_bootstrap_responsiv_dizayn`](11_bootstrap_responsiv_dizayn/) |
| 12 | PostgreSQL CRUD | [`12_postgresql_crud`](12_postgresql_crud/) |
| 13 | PostgreSQL JOIN va subquery | [`13_postgresql_join_subquery`](13_postgresql_join_subquery/) |
| 14 | Django kirish | [`14_django_kirish`](14_django_kirish/) |
| 15 | Django Models va ORM | [`15_django_models_orm`](15_django_models_orm/) |
| 16 | Django Views va URL | [`16_django_views_url`](16_django_views_url/) |
| 17 | Django formalar | [`17_django_formalar`](17_django_formalar/) |
| 18 | Django CRUD | [`18_django_crud`](18_django_crud/) |

## O'rnatish

### HTML/CSS/JS misollarini ishga tushirish

HTML fayllarni istalgan brauzerda ochish kifoya:

```bash
git clone https://github.com/username/web-dasturlash-kodlar.git
cd web-dasturlash-kodlar
# HTML faylni brauzerda oching
open 02_html_tuzilmasi/misollar/misol1.html
```

### PostgreSQL misollarini ishga tushirish

PostgreSQL o'rnatilgan bo'lishi kerak:

```bash
# Ma'lumotlar bazasini yarating
createdb web_dasturlash

# SQL faylni ishga tushiring
psql -d web_dasturlash -f 12_postgresql_crud/misollar/misol1.sql
```

### Django loyihalarini ishga tushirish

Python 3.10+ va Django o'rnatilgan bo'lishi kerak:

```bash
pip install django psycopg2-binary
cd 14_django_kirish/misollar/
python manage.py runserver
```

## Papka tuzilmasi

Har bir bob papkasi quyidagi tuzilmaga ega:

```
NN_bob_nomi/
  README.md          # Bob haqida ma'lumot
  misollar/          # Kod misollari
  topshiriqlar/      # Mustaqil ish topshiriqlari
```

## Talablar

- Brauzer (Chrome, Firefox yoki Safari) — HTML/CSS/JS uchun
- Node.js 18+ — JS fayllarni terminalda ishga tushirish uchun (ixtiyoriy)
- PostgreSQL 15+ — ma'lumotlar bazasi boblari uchun
- Python 3.10+ va Django 5.0+ — Django boblari uchun

## Litsenziya

Ushbu repozitoriyadagi barcha kodlar o'quv maqsadlarida foydalanish uchun ochiq.
Tijorat maqsadlarida foydalanish uchun muallifdan ruxsat oling.

**MIT License** — batafsil ma'lumot uchun [LICENSE](LICENSE) faylini ko'ring.

---

**© 2026 Boltayev Jahongir Erkin o'g'li, Termiz davlat universiteti**
