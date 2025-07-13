# Salonity API Dokümantasyonu

## Genel Bilgiler

- **Base URL**: `http://127.0.0.1:8000/api/`
- **Authentication**: Token Authentication
- **Content-Type**: `application/json`

## Authentication

### Token Alma
```bash
# Login sonrası token alınır
POST /api/customers/login/
{
    "username": "testuser1",
    "password": "password123"
}
```

### Token Kullanımı
```bash
# Header'da token gönderin
Authorization: Token YOUR_TOKEN_HERE
```

---

## 1. Müşteri API'leri

### 1.1 Müşteri Kayıt
```bash
POST /api/customers/register/
Content-Type: application/json

{
    "username": "yeni_kullanici",
    "email": "yeni@email.com",
    "password": "güvenli_şifre",
    "first_name": "Ad",
    "last_name": "Soyad",
    "phone": "0555 123 45 67"
}
```

### 1.2 Müşteri Giriş
```bash
POST /api/customers/login/
Content-Type: application/json

{
    "username": "testuser1",
    "password": "password123"
}
```

### 1.3 Sadakat Bilgileri
```bash
GET /api/customers/loyalty/
Authorization: Token YOUR_TOKEN_HERE

# Yanıt:
{
    "loyalty_level": "bronze",
    "loyalty_level_display": "Bronz",
    "total_points": 0,
    "current_points": 0,
    "total_spent": "0.00",
    "total_visits": 0
}
```

---

## 2. Salon API'leri

### 2.1 Salon Listesi
```bash
GET /api/salons/
Authorization: Token YOUR_TOKEN_HERE

# Yanıt:
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "ad7c5547-1026-434d-a200-08dc7c539cb3",
            "name": "Güzellik Salonu",
            "salon_type": "guzellik_salonu",
            "salon_type_display": "Güzellik Salonu",
            "address": "İstanbul, Kadıköy",
            "phone": "0555 123 45 67",
            "email": "info@guzelliksalonu.com",
            "description": "Profesyonel güzellik hizmetleri",
            "rating": null,
            "total_reviews": 0,
            "is_verified": false,
            "city": "İstanbul",
            "district": "Kadıköy"
        }
    ]
}
```

### 2.2 Salon Detayı
```bash
GET /api/salons/{salon_id}/
Authorization: Token YOUR_TOKEN_HERE
```

### 2.3 Salon Sahibi Kayıt
```bash
POST /api/salons/register/
Content-Type: application/json

{
    "username": "salon_sahibi",
    "email": "salon@email.com",
    "password": "güvenli_şifre",
    "salon_name": "Salon Adı",
    "salon_address": "Salon Adresi",
    "salon_phone": "0555 123 45 67"
}
```

---

## 3. Hizmet API'leri

### 3.1 Hizmet Listesi
```bash
GET /api/services/
Authorization: Token YOUR_TOKEN_HERE

# Yanıt:
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "d67ececd-999e-44b9-accc-50502eaf486f",
            "name": "Saç Kesimi",
            "description": "Profesyonel saç kesimi",
            "price": "100.00",
            "duration": 60,
            "image": null,
            "salon": "ad7c5547-1026-434d-a200-08dc7c539cb3",
            "category": "45819c34-9d4b-43d0-8559-da1382e5e683"
        }
    ]
}
```

### 3.2 Hizmet Kategorileri
```bash
GET /api/services/categories/
Authorization: Token YOUR_TOKEN_HERE

# Yanıt:
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "45819c34-9d4b-43d0-8559-da1382e5e683",
            "name": "Saç Bakımı",
            "description": "Saç kesimi, boyama, bakım",
            "icon": ""
        }
    ]
}
```

### 3.3 Salon Hizmetleri
```bash
GET /api/services/salon/{salon_id}/
Authorization: Token YOUR_TOKEN_HERE
```

---

## 4. Randevu API'leri

### 4.1 Randevu Listesi
```bash
GET /api/appointments/
Authorization: Token YOUR_TOKEN_HERE

# Yanıt:
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "appointment_id",
            "salon_name": "Güzellik Salonu",
            "service_name": "Saç Kesimi",
            "employee_name": null,
            "appointment_date": "2025-07-13",
            "appointment_time": "14:00:00",
            "end_time": "15:00:00",
            "status": "pending",
            "status_display": "Beklemede",
            "price": "100.00",
            "created_at": "2025-07-12T09:15:34.124469Z"
        }
    ]
}
```

### 4.2 Randevu Oluşturma
```bash
POST /api/appointments/create/
Authorization: Token YOUR_TOKEN_HERE
Content-Type: application/json

{
    "service": "d67ececd-999e-44b9-accc-50502eaf486f",
    "salon": "ad7c5547-1026-434d-a200-08dc7c539cb3",
    "appointment_date": "2025-07-13",
    "appointment_time": "14:00",
    "notes": "Test randevusu",
    "employee": null
}
```

### 4.3 Randevu Detayı
```bash
GET /api/appointments/{appointment_id}/
Authorization: Token YOUR_TOKEN_HERE
```

### 4.4 Randevu Güncelleme
```bash
PUT /api/appointments/{appointment_id}/update/
Authorization: Token YOUR_TOKEN_HERE
Content-Type: application/json

{
    "status": "confirmed",
    "notes": "Güncellenmiş notlar"
}
```

### 4.5 Randevu İptal
```bash
PUT /api/appointments/{appointment_id}/cancel/
Authorization: Token YOUR_TOKEN_HERE
```

### 4.6 Randevu Değerlendirmesi
```bash
POST /api/appointments/{appointment_id}/review/
Authorization: Token YOUR_TOKEN_HERE
Content-Type: application/json

{
    "rating": 5,
    "comment": "Harika bir hizmet aldım!"
}
```

---

## 5. Hata Kodları

| Kod | Açıklama |
|-----|----------|
| 200 | Başarılı |
| 201 | Oluşturuldu |
| 400 | Hatalı İstek |
| 401 | Yetkisiz Erişim |
| 403 | Yasak |
| 404 | Bulunamadı |
| 500 | Sunucu Hatası |

## 6. Örnek Kullanım Senaryoları

### Senaryo 1: Yeni Müşteri Kaydı ve Randevu
1. Müşteri kaydı yapın
2. Giriş yapın ve token alın
3. Salon listesini görüntüleyin
4. Hizmet listesini görüntüleyin
5. Randevu oluşturun

### Senaryo 2: Mevcut Müşteri Randevu Yönetimi
1. Giriş yapın
2. Randevularınızı görüntüleyin
3. Yeni randevu oluşturun
4. Randevu güncelleyin/iptal edin
5. Randevu değerlendirmesi yapın

---

## 7. Test Verileri

### Mevcut Test Verileri:
- **Kullanıcı**: testuser1
- **Token**: 3c8351459260c70c5766876ab9d75f398e03f69f
- **Salon**: Güzellik Salonu (ID: ad7c5547-1026-434d-a200-08dc7c539cb3)
- **Hizmet**: Saç Kesimi (ID: d67ececd-999e-44b9-accc-50502eaf486f)
- **Kategori**: Saç Bakımı (ID: 45819c34-9d4b-43d0-8559-da1382e5e683)

### Test Komutları:
```bash
# Sadakat bilgileri
curl -H "Authorization: Token 3c8351459260c70c5766876ab9d75f398e03f69f" \
     http://127.0.0.1:8000/api/customers/loyalty/

# Salon listesi
curl -H "Authorization: Token 3c8351459260c70c5766876ab9d75f398e03f69f" \
     http://127.0.0.1:8000/api/salons/

# Hizmet listesi
curl -H "Authorization: Token 3c8351459260c70c5766876ab9d75f398e03f69f" \
     http://127.0.0.1:8000/api/services/

# Randevu listesi
curl -H "Authorization: Token 3c8351459260c70c5766876ab9d75f398e03f69f" \
     http://127.0.0.1:8000/api/appointments/
```

---

## 8. Geliştirme Notları

- Tüm API'ler pagination destekler
- Token authentication zorunludur (sadakat API'si hariç)
- Tarih formatı: YYYY-MM-DD
- Saat formatı: HH:MM
- UUID'ler kullanılır
- Decimal fiyatlar 2 ondalık basamakla

---

**Son Güncelleme**: 12 Temmuz 2025
**Versiyon**: 1.0 