# 17-bob: Django Form va ModelForm yaratish

from django import forms
# from .models import Maqola, Talaba


# === Oddiy Form (Form sinfi) ===
class AloqaForma(forms.Form):
    """Aloqa formasi — model bilan bog'lanmagan."""
    ism = forms.CharField(
        max_length=100,
        label='Ismingiz',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ismingizni kiriting',
        })
    )
    email = forms.EmailField(
        label='Email manzilingiz',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'email@misol.uz',
        })
    )
    mavzu = forms.ChoiceField(
        choices=[
            ('', 'Mavzuni tanlang...'),
            ('savol', 'Savol'),
            ('taklif', 'Taklif'),
            ('xato', 'Xato haqida'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    xabar = forms.CharField(
        label='Xabaringiz',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Xabaringizni yozing...',
        })
    )


# === ModelForm — modeldan avtomatik forma ===
# class MaqolaForma(forms.ModelForm):
#     """Maqola formasi — modeldan yaratilgan."""
#     class Meta:
#         model = Maqola
#         fields = ['sarlavha', 'matn', 'kategoriya', 'teglar']
#         # yoki: fields = '__all__'
#         # yoki: exclude = ['muallif', 'yaratilgan']
#
#         labels = {
#             'sarlavha': 'Sarlavha',
#             'matn': 'Maqola matni',
#         }
#
#         widgets = {
#             'sarlavha': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Maqola sarlavhasi',
#             }),
#             'matn': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'rows': 10,
#             }),
#             'kategoriya': forms.Select(attrs={'class': 'form-select'}),
#             'teglar': forms.CheckboxSelectMultiple(),
#         }


# === TalabForma — barcha maydon turlari ===
class TalabaForma(forms.Form):
    """Turli maydon turlari namunasi."""

    ism = forms.CharField(max_length=50)
    familiya = forms.CharField(max_length=50)
    email = forms.EmailField()
    yosh = forms.IntegerField(min_value=16, max_value=60)
    ball = forms.DecimalField(max_digits=5, decimal_places=2)
    tugilgan_sana = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    aktiv = forms.BooleanField(required=False, initial=True)
    fakultet = forms.ChoiceField(choices=[
        ('fizmat', 'Fizika-matematika'),
        ('filologiya', 'Filologiya'),
        ('informatika', 'Informatika'),
    ])
    hobbilar = forms.MultipleChoiceField(
        choices=[
            ('sport', 'Sport'),
            ('musiqa', 'Musiqa'),
            ('dasturlash', 'Dasturlash'),
            ('kitob', 'Kitob o\'qish'),
        ],
        widget=forms.CheckboxSelectMultiple()
    )
    rasm = forms.ImageField(required=False)
