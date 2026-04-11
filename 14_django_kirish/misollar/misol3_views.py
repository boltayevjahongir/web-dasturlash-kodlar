# 14-bob: Birinchi view funksiya — "Salom, Django!"

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# === Eng oddiy view — HttpResponse ===
def salom(request):
    """Oddiy matn javob qaytaruvchi view."""
    return HttpResponse("Salom, Django!")


# === HTML javob ===
def bosh_sahifa(request):
    """HTML formatida javob qaytaruvchi view."""
    html = """
    <html>
    <head><title>Bosh sahifa</title></head>
    <body>
        <h1>Xush kelibsiz!</h1>
        <p>Bu Django bilan yaratilgan birinchi sahifa.</p>
        <ul>
            <li><a href="/blog/">Blog</a></li>
            <li><a href="/haqida/">Haqida</a></li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html)


# === Template bilan view ===
def haqida(request):
    """Template fayldan foydalanuvchi view."""
    context = {
        'sarlavha': 'Biz haqimizda',
        'matn': 'Bu sahifa Django template tizimi yordamida yaratilgan.',
        'yil': 2026,
    }
    return render(request, 'pages/haqida.html', context)


# === JSON javob ===
def api_talabalar(request):
    """JSON formatida ma'lumot qaytaruvchi view."""
    talabalar = [
        {'ism': 'Ali', 'ball': 85},
        {'ism': 'Vali', 'ball': 92},
        {'ism': 'Guli', 'ball': 78},
    ]
    return JsonResponse({'talabalar': talabalar})


# === Parametrli view ===
def talaba_detail(request, talaba_id):
    """URL parametrini qabul qiluvchi view."""
    return HttpResponse(f"Talaba ID: {talaba_id}")


# === Request ma'lumotlari ===
def request_info(request):
    """Request ob'ekti haqida ma'lumot."""
    info = f"""
    Metod: {request.method}
    Yo'l: {request.path}
    GET parametrlari: {request.GET}
    User Agent: {request.META.get('HTTP_USER_AGENT', 'Noma'lum')}
    """
    return HttpResponse(f"<pre>{info}</pre>")
