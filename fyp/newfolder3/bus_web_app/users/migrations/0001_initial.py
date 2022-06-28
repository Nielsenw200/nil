# Generated by Django 3.2.12 on 2022-06-28 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bus_catalog', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoicing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tran_id', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_catalog.authuser')),
            ],
        ),
    ]