import os
import django

# Django settings'i yükle
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'salonity.settings')
django.setup()

from django.contrib.auth.models import User

# Superuser bilgileri
username = 'admin'
email = 'admin@salonity.com'
password = 'admin123'

# Kullanıcı var mı kontrol et
if User.objects.filter(username=username).exists():
    print(f"Kullanıcı '{username}' zaten mevcut!")
else:
    # Superuser oluştur
    user = User.objects.create_superuser(username, email, password)
    print(f"Superuser oluşturuldu: {username}")
    print(f"Email: {email}")
    print(f"Şifre: {password}")
    print("\nAdmin paneline giriş yapabilirsin: http://127.0.0.1:8000/admin/") 