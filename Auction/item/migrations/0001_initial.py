# Generated by Django 5.0.3 on 2024-03-15 11:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(max_length=20, unique=True)),
                ('item_name', models.CharField(max_length=255)),
                ('item_category', models.CharField(choices=[('group1', 'Group 1'), ('group2', 'Group 2')], max_length=255)),
                ('standard_buying_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('standard_selling_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('uom', models.CharField(max_length=255)),
                ('item_subcategory', models.CharField(choices=[('category1', 'Category 1'), ('category2', 'Category 2')], max_length=255)),
                ('hsn_code', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('warehouse', models.CharField(max_length=255)),
            ],
        ),
    ]