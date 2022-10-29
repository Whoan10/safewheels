# Generated by Django 4.1.2 on 2022-10-26 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estabelecimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeE', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=100)),
                ('desc', models.CharField(blank=True, max_length=255, null=True)),
                ('imagens', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
