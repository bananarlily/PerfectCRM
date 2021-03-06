# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-19 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20161219_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstlayermenu',
            name='name',
            field=models.CharField(max_length=64, verbose_name='菜单名'),
        ),
        migrations.AlterField(
            model_name='firstlayermenu',
            name='sub_menus',
            field=models.ManyToManyField(blank=True, to='crm.SubMenu'),
        ),
        migrations.AlterField(
            model_name='role',
            name='menus',
            field=models.ManyToManyField(blank=True, to='crm.FirstLayerMenu'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='name',
            field=models.CharField(max_length=64, verbose_name='二层菜单名'),
        ),
    ]
