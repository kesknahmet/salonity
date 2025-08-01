# Generated by Django 5.2.4 on 2025-07-10 19:09

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('salons', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('appointment_date', models.DateField(verbose_name='Randevu Tarihi')),
                ('appointment_time', models.TimeField(verbose_name='Randevu Saati')),
                ('end_time', models.TimeField(blank=True, null=True, verbose_name='Bitiş Saati')),
                ('status', models.CharField(choices=[('pending', 'Beklemede'), ('confirmed', 'Onaylandı'), ('completed', 'Tamamlandı'), ('cancelled', 'İptal Edildi'), ('no_show', 'Gelmedi')], default='pending', max_length=20, verbose_name='Durum')),
                ('notes', models.TextField(blank=True, verbose_name='Notlar')),
                ('customer_notes', models.TextField(blank=True, verbose_name='Müşteri Notları')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Fiyat')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('confirmed_at', models.DateTimeField(blank=True, null=True, verbose_name='Onaylanma Tarihi')),
                ('completed_at', models.DateTimeField(blank=True, null=True, verbose_name='Tamamlanma Tarihi')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='customers.customer')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='salons.salonemployee')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='salons.salon')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='services.service')),
            ],
            options={
                'verbose_name': 'Randevu',
                'verbose_name_plural': 'Randevular',
                'ordering': ['-appointment_date', '-appointment_time'],
            },
        ),
        migrations.CreateModel(
            name='AppointmentReview',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='Puan')),
                ('comment', models.TextField(blank=True, verbose_name='Yorum')),
                ('salon_response', models.TextField(blank=True, verbose_name='Salon Yanıtı')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Değerlendirme Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='appointments.appointment')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='customers.customer')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='salons.salon')),
            ],
            options={
                'verbose_name': 'Randevu Değerlendirmesi',
                'verbose_name_plural': 'Randevu Değerlendirmeleri',
                'ordering': ['-created_at'],
            },
        ),
    ]
