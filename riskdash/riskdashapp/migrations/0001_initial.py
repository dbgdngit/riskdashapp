# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-02 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Control_Owners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='control_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Controls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controlref', models.CharField(max_length=9)),
                ('description', models.CharField(max_length=60)),
                ('type', models.CharField(max_length=60)),
                ('is_pci', models.CharField(max_length=1)),
                ('is_cyber_essentials', models.CharField(max_length=1)),
                ('is_iso27001', models.CharField(max_length=1)),
                ('is_gdpr', models.CharField(max_length=1)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riskdashapp.control_status')),
            ],
        ),
        migrations.CreateModel(
            name='Impact_rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Likelihood_rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Res_Likelihood_rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riskref', models.CharField(max_length=9)),
                ('description', models.CharField(max_length=60)),
                ('created_date', models.DateTimeField(verbose_name='created on')),
                ('last_updated_date', models.DateTimeField(verbose_name='last updated on')),
                ('previous_updated_date', models.DateTimeField(verbose_name='previous update')),
                ('Rating_rationale', models.CharField(max_length=60)),
                ('Absolute_Impact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riskdashapp.Impact_rating')),
                ('Absolute_Likelihood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riskdashapp.Likelihood_rating')),
                ('Associated_Controls', models.ManyToManyField(to='riskdashapp.Controls')),
                ('Residual_Likelihood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riskdashapp.Res_Likelihood_rating')),
            ],
        ),
        migrations.CreateModel(
            name='Risk_Owners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Risk_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='risk',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riskdashapp.Risk_Owners'),
        ),
    ]
