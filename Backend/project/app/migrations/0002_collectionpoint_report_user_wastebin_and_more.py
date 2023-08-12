# Generated by Django 4.2.4 on 2023-08-12 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('collection_schedule', models.CharField(max_length=255)),
                ('capacity', models.PositiveIntegerField()),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(max_length=50)),
                ('date_generated', models.DateTimeField()),
                ('parameters', models.JSONField()),
                ('data', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Collector', 'Collector'), ('Manager', 'Manager'), ('End_user', 'Contributer'), ('Region_head', 'Region Head'), ('Recycle_facility', 'Recycle_facility')], max_length=20)),
                ('contact_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WasteBin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.PositiveIntegerField()),
                ('current_fill_level', models.PositiveIntegerField()),
                ('last_emptied_date', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.collectionpoint')),
            ],
        ),
        migrations.CreateModel(
            name='WasteDisposalSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('capacity', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='react',
            name='department',
            field=models.CharField(max_length=40),
        ),
        migrations.CreateModel(
            name='WasteCollectionRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_datetime', models.DateTimeField()),
                ('collected_amount', models.PositiveIntegerField()),
                ('notes', models.TextField()),
                ('bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.wastebin')),
                ('collector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DisposalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disposal_datetime', models.DateTimeField()),
                ('disposed_amount', models.PositiveIntegerField()),
                ('notes', models.TextField()),
                ('bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.wastebin')),
                ('collector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('disposal_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.wastedisposalsite')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('schedule', models.CharField(max_length=255)),
                ('assigned_collector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('end_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end_routes', to='app.collectionpoint')),
                ('start_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_routes', to='app.collectionpoint')),
            ],
        ),
    ]
