# Topshiriq 1 (Oson): Yangi loyiha va app yaratish qadamlari
# Quyidagi qadamlarni bajaring va har bir qadamda nima sodir bo'lishini tushuntiring:

# 1. Virtual muhit yarating va faollashtiring:
#    python -m venv venv
#    source venv/bin/activate  (macOS/Linux)
#    venv\Scripts\activate     (Windows)

# 2. Django o'rnating:
#    pip install django

# 3. Yangi loyiha yarating:
#    django-admin startproject mening_loyiham

# 4. Loyiha papkasiga kiring:
#    cd mening_loyiham

# 5. Yangi ilova yarating:
#    python manage.py startapp sahifalar

# 6. settings.py da ilovani ro'yxatga qo'shing:
#    INSTALLED_APPS = [..., 'sahifalar']

# 7. sahifalar/views.py da quyidagi viewni yarating:
def bosh_sahifa(request):
    """Bosh sahifa uchun view yozing.
    HttpResponse bilan 'Salom, bu mening birinchi Django loyiham!' qaytaring.
    """
    pass  # Kodingizni yozing

# 8. sahifalar/urls.py faylini yarating va URL yo'lini qo'shing

# 9. Loyiha urls.py ga include qo'shing

# 10. Serverni ishga tushiring:
#     python manage.py runserver
#     Brauzerda http://127.0.0.1:8000/ ni oching
