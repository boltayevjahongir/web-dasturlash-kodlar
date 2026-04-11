# 17-bob: Formani view da ishlatish (GET/POST)

from django.shortcuts import render, redirect
from django.contrib import messages
# from .forms import AloqaForma, MaqolaForma


# === FBV bilan forma ===
def aloqa(request):
    """Aloqa formasi — GET va POST ni qayta ishlash."""
    if request.method == 'POST':
        # forma = AloqaForma(request.POST)
        forma = None  # Namuna

        if forma and forma.is_valid():
            # Tozalangan ma'lumotlarni olish
            ism = forma.cleaned_data['ism']
            email = forma.cleaned_data['email']
            mavzu = forma.cleaned_data['mavzu']
            xabar = forma.cleaned_data['xabar']

            # Xabarni saqlash yoki email yuborish
            # send_mail(mavzu, xabar, email, ['admin@site.uz'])

            messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi!')
            return redirect('aloqa')
    else:
        # forma = AloqaForma()
        forma = None

    return render(request, 'sahifalar/aloqa.html', {'forma': forma})


# === ModelForm bilan CRUD ===
def maqola_yaratish(request):
    """Yangi maqola yaratish formasi."""
    if request.method == 'POST':
        # forma = MaqolaForma(request.POST, request.FILES)
        forma = None

        if forma and forma.is_valid():
            maqola = forma.save(commit=False)
            maqola.muallif = request.user
            maqola.save()
            forma.save_m2m()  # ManyToMany maydonlarni saqlash

            messages.success(request, 'Maqola yaratildi!')
            return redirect('maqola_batafsil', pk=maqola.pk)
    else:
        # forma = MaqolaForma()
        forma = None

    return render(request, 'blog/maqola_forma.html', {'forma': forma})


def maqola_tahrirlash(request, pk):
    """Maqolani tahrirlash."""
    # maqola = get_object_or_404(Maqola, pk=pk)

    if request.method == 'POST':
        # forma = MaqolaForma(request.POST, request.FILES, instance=maqola)
        forma = None

        if forma and forma.is_valid():
            forma.save()
            messages.success(request, 'Maqola yangilandi!')
            return redirect('maqola_batafsil', pk=pk)
    else:
        # forma = MaqolaForma(instance=maqola)
        forma = None

    return render(request, 'blog/maqola_forma.html', {'forma': forma})


# === Template namunasi (aloqa.html) ===
TEMPLATE = """
{% extends 'base.html' %}
{% block content %}
<h1>Aloqa</h1>

{% if messages %}
    {% for message in messages %}
        <div class="alert alert-{{ message.tags }}">{{ message }}</div>
    {% endfor %}
{% endif %}

<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}

    {# Usul 1: Avtomatik render #}
    {{ forma.as_p }}

    {# Usul 2: Qo'lda render (ko'proq nazorat) #}
    {# {% for field in forma %}
    <div class="mb-3">
        <label class="form-label">{{ field.label }}</label>
        {{ field }}
        {% if field.errors %}
            {% for error in field.errors %}
                <div class="text-danger">{{ error }}</div>
            {% endfor %}
        {% endif %}
        {% if field.help_text %}
            <small class="text-muted">{{ field.help_text }}</small>
        {% endif %}
    </div>
    {% endfor %} #}

    <button type="submit" class="btn btn-primary">Yuborish</button>
</form>
{% endblock %}
"""

print("Forma misollari — views.py va templates/ da ishlatiladi.")
