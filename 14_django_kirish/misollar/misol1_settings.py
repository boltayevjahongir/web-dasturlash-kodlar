# 14-bob: Django settings.py asosiy sozlamalari
# Bu fayl to'liq settings.py emas, faqat muhim qismlarni ko'rsatadi.

# === Loyiha ildiz papkasi ===
# BASE_DIR = Path(__file__).resolve().parent.parent

# === Maxfiy kalit (ishlab chiqishda) ===
# SECRET_KEY = 'django-insecure-...'  # Haqiqiy loyihada .env ga o'tkazing!

# === Debug rejimi ===
# DEBUG = True  # Ishlab chiqishda True, serverda False

# === Ruxsat berilgan hostlar ===
# ALLOWED_HOSTS = []  # Serverda ['example.com', 'www.example.com']

# === O'rnatilgan ilovalar ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # O'z ilovalaringizni shu yerga qo'shing:
    # 'blog.apps.BlogConfig',
    # 'accounts.apps.AccountsConfig',
]

# === Ma'lumotlar bazasi (PostgreSQL) ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'web_dasturlash',
        'USER': 'postgres',
        'PASSWORD': 'parol',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# === Til va vaqt mintaqasi ===
LANGUAGE_CODE = 'uz'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

# === Statik fayllar ===
STATIC_URL = 'static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# === Media fayllar ===
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'
