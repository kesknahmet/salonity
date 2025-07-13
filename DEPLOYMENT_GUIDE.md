# Salonity Production Deployment Kılavuzu

## 🚀 Deployment Seçenekleri

### 1. Heroku (Önerilen - Kolay)

#### Kurulum:
```bash
# Heroku CLI kurulumu
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Uygulama oluştur
heroku create salonity-app

# PostgreSQL addon ekle
heroku addons:create heroku-postgresql:mini

# Environment variables ayarla
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS="salonity-app.herokuapp.com"

# Deploy
git add .
git commit -m "Production ready"
git push heroku main

# Migrations
heroku run python manage.py migrate

# Superuser oluştur
heroku run python manage.py createsuperuser

# Static files
heroku run python manage.py collectstatic --noinput
```

### 2. Railway (Alternatif)

#### Kurulum:
```bash
# Railway CLI
npm install -g @railway/cli

# Login
railway login

# Proje oluştur
railway init

# Deploy
railway up

# Environment variables
railway variables set SECRET_KEY="your-secret-key"
railway variables set DEBUG=False
```

### 3. DigitalOcean (VPS)

#### Kurulum:
```bash
# Server kurulumu
sudo apt update
sudo apt install python3-pip python3-venv nginx postgresql

# Virtual environment
python3 -m venv venv
source venv/bin/activate

# Dependencies
pip install -r requirements.txt

# Database
sudo -u postgres createdb salonity_db
sudo -u postgres createuser salonity_user

# Gunicorn service
sudo nano /etc/systemd/system/salonity.service
```

## 🔧 Environment Variables

### Gerekli Variables:
```bash
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://username:password@host:port/dbname
CORS_ALLOWED_ORIGINS=https://yourdomain.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Opsiyonel Variables:
```bash
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

## 📦 Pre-deployment Checklist

### ✅ Tamamlanması Gerekenler:
- [ ] `requirements.txt` güncel
- [ ] `production.py` settings hazır
- [ ] `Procfile` oluşturuldu
- [ ] `runtime.txt` belirtildi
- [ ] Static files ayarlandı
- [ ] Database migration'ları hazır
- [ ] Environment variables tanımlandı
- [ ] CORS ayarları yapıldı
- [ ] Security settings aktif
- [ ] Logging konfigürasyonu

### 🔍 Test Edilecekler:
- [ ] API endpoint'leri çalışıyor
- [ ] Authentication çalışıyor
- [ ] Database bağlantısı
- [ ] Static files serve ediliyor
- [ ] Email gönderimi
- [ ] Error handling

## 🚀 Deployment Sonrası

### 1. Health Check
```bash
# API test
curl https://your-app.herokuapp.com/api/salons/

# Admin panel
https://your-app.herokuapp.com/admin/
```

### 2. Monitoring
```bash
# Logs
heroku logs --tail

# Performance
heroku ps
```

### 3. Backup
```bash
# Database backup
heroku pg:backups:capture
heroku pg:backups:download
```

## 🔒 Security Checklist

- [ ] DEBUG=False
- [ ] SECRET_KEY güvenli
- [ ] ALLOWED_HOSTS sınırlı
- [ ] CORS ayarları doğru
- [ ] HTTPS aktif
- [ ] Database credentials güvenli
- [ ] Rate limiting aktif
- [ ] XSS protection aktif

## 📊 Performance Optimization

### 1. Database
```bash
# Index'ler ekle
python manage.py makemigrations
python manage.py migrate
```

### 2. Caching
```bash
# Redis cache ekle
pip install django-redis
```

### 3. CDN
```bash
# Static files için CDN
# AWS S3, CloudFront, etc.
```

## 🆘 Troubleshooting

### Yaygın Sorunlar:

#### 1. Database Connection
```bash
# Connection test
heroku run python manage.py dbshell
```

#### 2. Static Files
```bash
# Collect static
heroku run python manage.py collectstatic --noinput
```

#### 3. Migration Issues
```bash
# Reset migrations
heroku run python manage.py migrate --fake-initial
```

#### 4. Memory Issues
```bash
# Dyno size artır
heroku ps:scale web=1:standard-1x
```

## 📞 Destek

**Deployment sorunları için:**
- Heroku: https://devcenter.heroku.com/
- Railway: https://docs.railway.app/
- DigitalOcean: https://docs.digitalocean.com/

---

**Son Güncelleme**: 12 Temmuz 2025  
**Versiyon**: 1.0 