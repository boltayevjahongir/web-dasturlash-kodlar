# 16-bob: Template va merosxo'rlik misollari
# Bu fayl template namunalarini Python string sifatida ko'rsatadi.
# Haqiqiy loyihada bu fayllar templates/ papkasida .html bo'ladi.

# === base.html — Asosiy shablon ===
BASE_TEMPLATE = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Sayt nomi{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    {% block extra_css %}{% endblock %}
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="{% url 'bosh_sahifa' %}">Sayt</a>
            <div class="navbar-nav">
                <a class="nav-link" href="{% url 'maqola_royxat' %}">Maqolalar</a>
                <a class="nav-link" href="{% url 'haqida' %}">Haqida</a>
            </div>
        </div>
    </nav>

    <div class="container my-4">
        {% block content %}
        <!-- Sahifa kontenti shu yerda -->
        {% endblock %}
    </div>

    <footer class="bg-dark text-white py-3 mt-5">
        <div class="container text-center">
            &copy; 2026 Sayt nomi
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
"""

# === maqola_royxat.html — base.html dan meros oladi ===
ROYXAT_TEMPLATE = """
{% extends 'base.html' %}

{% block title %}Maqolalar{% endblock %}

{% block content %}
<h1>Maqolalar</h1>

{% if maqolalar %}
    {% for maqola in maqolalar %}
    <div class="card mb-3">
        <div class="card-body">
            <h5 class="card-title">{{ maqola.sarlavha }}</h5>
            <p class="card-text">{{ maqola.matn|truncatewords:30 }}</p>
            <small class="text-muted">
                {{ maqola.muallif }} | {{ maqola.yaratilgan|date:"d M Y" }}
            </small>
            <br>
            {% for teg in maqola.teglar.all %}
                <span class="badge bg-secondary">{{ teg.nomi }}</span>
            {% endfor %}
            <a href="{% url 'maqola_batafsil' maqola.pk %}" class="btn btn-sm btn-primary mt-2">
                Batafsil
            </a>
        </div>
    </div>
    {% endfor %}

    <!-- Sahifalash -->
    {% if is_paginated %}
    <nav>
        <ul class="pagination">
            {% if page_obj.has_previous %}
                <li class="page-item">
                    <a class="page-link" href="?page={{ page_obj.previous_page_number }}">Oldingi</a>
                </li>
            {% endif %}
            <li class="page-item active">
                <span class="page-link">{{ page_obj.number }} / {{ page_obj.paginator.num_pages }}</span>
            </li>
            {% if page_obj.has_next %}
                <li class="page-item">
                    <a class="page-link" href="?page={{ page_obj.next_page_number }}">Keyingi</a>
                </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %}

{% else %}
    <div class="alert alert-info">Hozircha maqolalar yo'q.</div>
{% endif %}
{% endblock %}
"""

# === Template teglar va filterlar ===
TEGLAR_MISOL = """
{# Bu izoh — ko'rinmaydi #}

{# O'zgaruvchi chiqarish #}
{{ ism }}
{{ talaba.familiya }}

{# if/elif/else #}
{% if ball >= 86 %}
    A'lo
{% elif ball >= 71 %}
    Yaxshi
{% else %}
    Qoniqarsiz
{% endif %}

{# for sikli #}
{% for talaba in talabalar %}
    {{ forloop.counter }}. {{ talaba.ism }}
{% empty %}
    Talabalar topilmadi.
{% endfor %}

{# url teg #}
<a href="{% url 'talaba_batafsil' pk=talaba.id %}">Ko'rish</a>

{# static teg #}
{% load static %}
<img src="{% static 'img/logo.png' %}" alt="Logo">

{# Filterlar #}
{{ matn|truncatewords:20 }}
{{ sana|date:"d.m.Y" }}
{{ ism|upper }}
{{ matn|default:"Ma'lumot yo'q" }}
{{ narx|floatformat:2 }}
{{ royxat|length }}
"""

print("Template misollari — yuqoridagi stringlarni templates/ papkasiga .html fayl sifatida saqlang.")
