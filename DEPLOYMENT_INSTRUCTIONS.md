# Salonity Render Deployment Kılavuzu

## 🚀 Hızlı Başlangıç (5 Dakika)

### **Adım 1: Render Dashboard**
1. https://dashboard.render.com/ adresine gidin
2. GitHub ile login olun
3. "New +" butonuna tıklayın

### **Adım 2: Web Service Oluşturma**
1. "Web Service" seçin
2. GitHub reponuzu seçin (eğer yoksa "Connect a repository" tıklayın)
3. Repository: `Salonity-Django` seçin

### **Adım 3: Konfigürasyon**
```
Name: salonity-api
Environment: Python 3
Region: Frankfurt (EU) (önerilen)
Branch: main
Root Directory: Salonity-Django
Build Command: pip install -r requirements.txt
Start Command: gunicorn salonity.wsgi:application
```

### **Adım 4: Environment Variables**
```
SECRET_KEY: (otomatik oluşturulacak)
DEBUG: False
ALLOWED_HOSTS: .onrender.com
DATABASE_URL: (otomatik oluşturulacak)
```

### **Adım 5: Database**
1. "Add Database" tıklayın
2. PostgreSQL seçin
3. Plan: Free
4. Database Name: salonity

### **Adım 6: Deploy**
1. "Create Web Service" tıklayın
2. Build işlemini bekleyin (2-3 dakika)
3. "View" butonuna tıklayarak API'yi test edin

---

## 🔧 Manuel Deployment (GitHub yoksa)

### **Adım 1: GitHub Repository Oluşturma**
```bash
# Git repository oluştur
git init
git add .
git commit -m "Initial commit"

# GitHub'da yeni repo oluştur ve push et
git remote add origin https://github.com/username/salonity.git
git push -u origin main
```

### **Adım 2: Render'da Repository Bağlama**
1. Render Dashboard'da "New +" → "Web Service"
2. "Connect a repository" tıklayın
3. GitHub reponuzu seçin
4. Yukarıdaki adımları takip edin

---

## 🧪 Deployment Sonrası Test

### **1. API Test**
```bash
# Ana endpoint
curl https://salonity-api.onrender.com/api/salons/

# Admin panel
https://salonity-api.onrender.com/admin/
```

### **2. Database Migration**
```bash
# Render Dashboard'da "Shell" sekmesine gidin
python manage.py migrate
python manage.py createsuperuser
```

### **3. Static Files**
```bash
python manage.py collectstatic --noinput
```

---

## 📊 Ücretsiz Plan Limitleri

### **Render Free Plan:**
- **Web Service**: 750 saat/ay (yaklaşık 31 gün)
- **Database**: 1GB storage
- **Bandwidth**: Sınırsız
- **Custom Domain**: Desteklenir

### **Performans:**
- **Cold Start**: 30-60 saniye (ilk istek)
- **Response Time**: 200-500ms
- **Concurrent Users**: 100-500

---

## 🔄 Railway'e Geçiş (İsteğe Bağlı)

### **Railway CLI Login Sorunu Çözümü:**
```bash
# Token ile login
railway login --token YOUR_TOKEN

# Veya browser'da manuel login
railway login --browser
```

### **Railway vs Render:**
| Özellik | Railway | Render |
|---------|---------|--------|
| Free Plan | 500 saat | 750 saat |
| Cold Start | 10-30s | 30-60s |
| Database | PostgreSQL | PostgreSQL |
| Custom Domain | ✅ | ✅ |
| CLI | ✅ | ❌ |

---

## 🎯 Sonraki Adımlar

### **Deployment Sonrası:**
1. ✅ API testleri
2. ✅ Database migration
3. ✅ Admin panel erişimi
4. ✅ CORS ayarları
5. ✅ Monitoring kurulumu

### **1. Hafta:**
1. Performance testing
2. Load testing
3. Error monitoring
4. Backup setup

### **1. Ay:**
1. Custom domain
2. SSL certificate
3. CDN setup
4. Analytics

---

## 🆘 Sorun Giderme

### **Yaygın Sorunlar:**

#### 1. Build Hatası
```bash
# requirements.txt kontrol et
pip install -r requirements.txt

# Python version kontrol et
python --version
```

#### 2. Database Bağlantı Hatası
```bash
# DATABASE_URL kontrol et
echo $DATABASE_URL

# Migration çalıştır
python manage.py migrate
```

#### 3. Static Files Hatası
```bash
# Static files collect et
python manage.py collectstatic --noinput

# STATIC_ROOT kontrol et
```

#### 4. Import Hatası
```bash
# Missing dependencies
pip install missing-package
```

---

## 📞 Destek

**Render Support:**
- Documentation: https://render.com/docs
- Community: https://community.render.com/
- Status: https://status.render.com/

**Salonity Support:**
- GitHub Issues: https://github.com/username/salonity/issues
- Email: support@salonity.com

---

**Son Güncelleme**: 12 Temmuz 2025  
**Versiyon**: 1.0 