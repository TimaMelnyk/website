# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='order-date')),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.UserProfile')),
            ],
        ),
    ]