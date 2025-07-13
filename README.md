# Comparative Critical Studies - Django Journal Project

Bu Django asosida yaratilgan ilmiy jurnal veb-sayti. Loyiha Tailwind CSS, Alpine.js va Flowbite komponentlari bilan qurilgan.

## 📋 Loyiha haqida

Bu loyiha **Edinburgh University Press** uchun yaratilgan ilmiy jurnal veb-sayti bo'lib, quyidagi xususiyatlarga ega:

- 📚 Jurnal sahifalari va maqolalar
- 👥 Tahririyat kengashi ma'lumotlari
- 📝 Maqola topshirish tizimi
- 🔍 Barcha sonlar va maqolalar
- 📧 Obuna va aloqa

## 🚀 O'rnatish va ishga tushirish

### 1. Loyihani yuklab olish

```bash
git clone <repository-url>
cd templates
```

### 2. Python virtual environment yaratish

```bash
# Windows uchun
python -m venv venv
venv\Scripts\activate

# Linux/Mac uchun
python3 -m venv venv
source venv/bin/activate
```

### 3. Python paketlarini o'rnatish

```bash
pip install -r requirements.txt
```

### 4. Node.js va npm o'rnatish

Loyihada Tailwind CSS ishlatilgani uchun Node.js va npm kerak:

1. [Node.js rasmiy saytidan](https://nodejs.org/) yuklab oling
2. O'rnatishni yakunlang
3. Terminalda tekshiring:
   ```bash
   node --version
   npm --version
   ```

### 5. Frontend paketlarini o'rnatish

```bash
npm install
```

### 6. Tailwind CSS build qilish

```bash
# Development uchun (doimiy kuzatib turadi)
npm run build

# Production uchun (minify qilingan)
npm run build-prod
```

### 7. Django migratsiyalari

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Superuser yaratish (ixtiyoriy)

```bash
python manage.py createsuperuser
```

### 9. Development serverini ishga tushirish

```bash
python manage.py runserver
```

Loyiha http://127.0.0.1:8000/ manzilida ochiladi.

## 🛠️ Loyiha strukturasi

```
templates/
├── myproject/                 # Django asosiy loyiha
│   ├── settings.py           # Loyiha sozlamalari
│   ├── urls.py               # Asosiy URL konfiguratsiyasi
│   └── wsgi.py               # WSGI konfiguratsiyasi
├── static/                   # Static fayllar
│   ├── css/                  # CSS fayllari
│   │   ├── tailwind.css      # Tailwind CSS (build qilingan)
│   │   ├── flowbite.css      # Flowbite CSS
│   │   └── fonts/            # Shriftlar
│   ├── js/                   # JavaScript fayllari
│   │   ├── alpine.js         # Alpine.js
│   │   └── flowbite.js       # Flowbite JS
│   ├── fonts/                # Open Sans shriftlari
│   └── assets/               # Rasmlar va boshqa fayllar
├── templates/                # HTML shablonlar
│   ├── base.html             # Asosiy shablon
│   ├── index.html            # Bosh sahifa
│   └── ...                   # Boshqa sahifalar
├── package.json              # Node.js paketlar
├── tailwind.config.js        # Tailwind konfiguratsiyasi
└── requirements.txt          # Python paketlar
```

## 🎨 Tailwind CSS bilan ishlash

### Tailwind CSS nima?

Tailwind CSS - bu utility-first CSS framework bo'lib, HTML elementlariga to'g'ridan-to'g'ri class berish orqali stillar yaratish imkonini beradi.

### Asosiy classlar:

```html
<!-- Padding -->
<div class="p-4">
  <!-- padding: 1rem -->
  <div class="px-8 py-4">
    <!-- padding-left/right: 2rem, padding-top/bottom: 1rem -->

    <!-- Margin -->
    <div class="m-4">
      <!-- margin: 1rem -->
      <div class="mx-auto">
        <!-- margin-left/right: auto -->

        <!-- Ranglar -->
        <div class="bg-blue-500">
          <!-- background-color: blue -->
          <div class="text-white">
            <!-- color: white -->

            <!-- O'lchamlar -->
            <div class="w-full">
              <!-- width: 100% -->
              <div class="h-screen">
                <!-- height: 100vh -->

                <!-- Flexbox -->
                <div class="flex">
                  <!-- display: flex -->
                  <div class="justify-center">
                    <!-- justify-content: center -->
                    <div class="items-center">
                      <!-- align-items: center -->

                      <!-- Grid -->
                      <div class="grid grid-cols-3">
                        <!-- display: grid, grid-template-columns: repeat(3, 1fr) -->
                      </div>
                    </div></div
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```

### Responsive dizayn:

```html
<div class="w-full md:w-1/2 lg:w-1/3">
  <!-- Kichik ekran: 100% -->
  <!-- O'rta ekran: 50% -->
  <!-- Katta ekran: 33.33% -->
</div>
```

### Custom CSS qo'shish:

Agar Tailwind'da mavjud bo'lmagan stillar kerak bo'lsa, `base.html` faylidagi `<style>` tagiga qo'shishingiz mumkin:

```html
<style>
  .custom-class {
    /* Custom stillar */
  }

  @media (min-width: 1024px) {
    .lg\:custom-class {
      /* Desktop uchun custom stillar */
    }
  }
</style>
```

## 🔧 Development jarayoni

### 1. Yangi sahifa qo'shish

1. `templates/` papkasida yangi HTML fayl yarating
2. `base.html` ni extend qiling:
   ```html
   {% extends 'base.html' %} {% block content %}
   <!-- Sahifa mazmuni -->
   {% endblock %}
   ```
3. `urls.py` ga yangi URL qo'shing

### 2. Tailwind CSS o'zgarishlari

Agar Tailwind classlarini o'zgartirsangiz:

```bash
# Development rejimida (avtomatik yangilanadi)
npm run build

# Yoki production build
npm run build-prod
```

### 3. Yangi paket qo'shish

```bash
# Frontend paket
npm install package-name

# Python paket
pip install package-name
pip freeze > requirements.txt
```

## 📱 Responsive dizayn

Loyiha barcha qurilmalarda yaxshi ko'rinish uchun responsive dizayn bilan yaratilgan:

- **Mobile**: 320px - 768px
- **Tablet**: 768px - 1024px
- **Desktop**: 1024px va undan katta

### Responsive classlar:

```html
<!-- Kichik ekranlar -->
<div class="text-sm sm:text-base lg:text-lg">
  <!-- Grid responsive -->
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
    <!-- Padding responsive -->
    <div class="px-4 sm:px-8 md:px-16 lg:px-28"></div>
  </div>
</div>
```

## 🚀 Production deployment

### 1. Static fayllarni yig'ish

```bash
python manage.py collectstatic
```

### 2. Environment variables

`.env` fayl yarating:

```env
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=your-domain.com
```

### 3. Database

```bash
python manage.py migrate
```

### 4. Web server

Nginx yoki Apache bilan sozlang.

## 🐛 Xatoliklarni tuzatish

### Tailwind CSS ishlamayapti

1. Node.js o'rnatilganligini tekshiring
2. `npm install` bajaring
3. `npm run build` bajaring
4. Browser cache'ni tozalang

### Static fayllar ko'rinmayapti

1. `python manage.py collectstatic` bajaring
2. `settings.py` da `STATIC_URL` va `STATIC_ROOT` to'g'ri sozlanganligini tekshiring

### Database xatosi

1. `python manage.py makemigrations` bajaring
2. `python manage.py migrate` bajaring

## 📞 Yordam va aloqa

Muammolar yuzaga kelganda:

1. GitHub Issues oching
2. Yoki email orqali bog'laning
3. Loyiha hujjatlarini o'qing

## 📄 Litsenziya

Bu loyiha MIT litsenziyasi ostida tarqatiladi.

---

**Eslatma**: Bu loyiha Django 4.x va Tailwind CSS 3.x versiyalari bilan ishlaydi. Yangi versiyalar bilan muammo bo'lsa, versiyalarni tekshiring.
