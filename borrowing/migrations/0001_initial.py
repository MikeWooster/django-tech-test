# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-16 22:17
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.TextField()),
                ('postcode', models.CharField(max_length=8)),
                ('registered_company_number', models.CharField(max_length=8, validators=[django.core.validators.MinLengthValidator(8)])),
                ('business_sector', models.CharField(choices=[('RE', 'Retail'), ('PS', 'Professional Services'), ('FD', 'Food & Drink'), ('EN', 'Entertainment')], default='RE', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='LoanRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(10000.0), django.core.validators.MaxValueValidator(100000.0)])),
                ('loan_length_days', models.PositiveSmallIntegerField()),
                ('reason', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='borrowing.Company')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('telephone_number', models.CharField(max_length=15)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='borrowing.Company')),
                ('userauth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
