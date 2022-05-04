# Generated by Django 3.1 on 2021-07-21 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant', models.CharField(max_length=300, verbose_name='Учреждение')),
                ('code', models.CharField(max_length=8, verbose_name='IP адрес')),
                ('description', models.CharField(blank=True, max_length=300)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prefix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=18, verbose_name='IP адрес')),
                ('description', models.CharField(blank=True, max_length=300)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.tenant', verbose_name='Учреждение')),
            ],
        ),
        migrations.CreateModel(
            name='IpAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('prefix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.prefix', verbose_name='Подсеть')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.tenant', verbose_name='Учреждение')),
            ],
        ),
    ]