# 14-bob: URL routing — urls.py misoli
# Loyiha darajasidagi urls.py

from django.contrib import admin
from django.urls import path, include

# Loyiha URLlari
urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Blog ilovasining URLlari
    path('blog/', include('blog.urls')),

    # Asosiy sahifa
    path('', include('pages.urls')),
]

# ---------------------------------------------------
# blog/urls.py — Ilova darajasidagi urls.py
# ---------------------------------------------------
# from django.urls import path
# from . import views
#
# app_name = 'blog'
#
# urlpatterns = [
#     path('', views.post_list, name='post_list'),           # /blog/
#     path('<int:pk>/', views.post_detail, name='post_detail'), # /blog/1/
#     path('yangi/', views.post_create, name='post_create'),  # /blog/yangi/
# ]

# ---------------------------------------------------
# URL naqshlari (patterns):
# ---------------------------------------------------
# path('maqola/<int:id>/')     — butun son: /maqola/5/
# path('user/<str:username>/')  — matn: /user/ali/
# path('sahifa/<slug:slug>/')   — slug: /sahifa/birinchi-maqola/
# path('arxiv/<int:yil>/<int:oy>/') — ko'p parametr: /arxiv/2026/4/
