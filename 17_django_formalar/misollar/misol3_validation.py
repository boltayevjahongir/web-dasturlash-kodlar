# 17-bob: Maxsus validatsiya va clean metodlari

from django import forms
from django.core.validators import RegexValidator, MinValueValidator


# === Maxsus validatorlar ===
telefon_validator = RegexValidator(
    regex=r'^\+998\d{9}$',
    message='Telefon raqami +998XXXXXXXXX formatida bo\'lishi kerak.'
)


# === Forma bilan validatsiya ===
class RoyxatdanOtishForma(forms.Form):
    """Ro'yxatdan o'tish formasi — validatsiya bilan."""

    ism = forms.CharField(
        min_length=2,
        max_length=50,
        label='Ism',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    familiya = forms.CharField(
        min_length=2,
        max_length=50,
        label='Familiya',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    telefon = forms.CharField(
        label='Telefon',
        validators=[telefon_validator],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+998901234567'
        })
    )

    parol = forms.CharField(
        min_length=8,
        label='Parol',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    parol_tasdiqlash = forms.CharField(
        label='Parolni tasdiqlang',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    yosh = forms.IntegerField(
        validators=[MinValueValidator(16)],
        label='Yosh',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    shartlar = forms.BooleanField(
        label='Shartlarga roziman',
        error_messages={'required': 'Shartlarga rozilik bildiring.'}
    )

    # === Maydon darajasida validatsiya (clean_<field>) ===
    def clean_ism(self):
        """Ism faqat harflardan iborat bo'lishi kerak."""
        ism = self.cleaned_data['ism']
        if not ism.replace("'", "").replace(" ", "").isalpha():
            raise forms.ValidationError("Ism faqat harflardan iborat bo'lishi kerak.")
        return ism.capitalize()

    def clean_email(self):
        """Email mavjudligini tekshirish."""
        email = self.cleaned_data['email']
        # Haqiqiy loyihada: User.objects.filter(email=email).exists()
        taqiqlangan = ['test@test.com', 'admin@admin.com']
        if email in taqiqlangan:
            raise forms.ValidationError("Bu email allaqachon ishlatilgan.")
        return email.lower()

    def clean_yosh(self):
        """Yoshni tekshirish."""
        yosh = self.cleaned_data['yosh']
        if yosh < 16 or yosh > 60:
            raise forms.ValidationError("Yosh 16 dan 60 gacha bo'lishi kerak.")
        return yosh

    # === Forma darajasida validatsiya (clean) ===
    def clean(self):
        """Parollar mos kelishini tekshirish."""
        cleaned_data = super().clean()
        parol = cleaned_data.get('parol')
        parol_tasdiqlash = cleaned_data.get('parol_tasdiqlash')

        if parol and parol_tasdiqlash:
            if parol != parol_tasdiqlash:
                raise forms.ValidationError("Parollar mos kelmaydi!")

            # Parol kuchliligini tekshirish
            if parol.isdigit():
                raise forms.ValidationError("Parol faqat raqamlardan iborat bo'lmasligi kerak.")

            if len(parol) < 8:
                self.add_error('parol', "Parol kamida 8 belgidan iborat bo'lishi kerak.")

        return cleaned_data
