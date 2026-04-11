# Topshiriq 1 (Oson): Kontakt forma yarating

from django import forms


# 1. AloqaForma yarating quyidagi maydonlar bilan:
#    - ism (CharField, max 100)
#    - email (EmailField)
#    - mavzu (CharField, max 200)
#    - xabar (CharField, Textarea widget)
#    - Barcha widgetlarga Bootstrap 'form-control' class qo'shing

class AloqaForma(forms.Form):
    pass  # Formani yozing


# 2. aloqa_view FBV yozing:
#    - GET: bo'sh formani ko'rsating
#    - POST: formani tekshiring, valid bo'lsa messages bilan xabar bering
#    - redirect bilan qaytaring

# def aloqa_view(request):
#     pass  # Kodingizni yozing


# 3. Template yarating (aloqa.html):
#    - {% csrf_token %} qo'shing
#    - forma.as_p yoki qo'lda render qiling
#    - Xato xabarlarni ko'rsating
#    - Bootstrap stillar ishlating
