# Generated by Django 5.0 on 2023-12-25 00:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_registration'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_1', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota')),
                ('average', models.DecimalField(blank=True, decimal_places=1, max_digits=3, verbose_name='Promedio')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course', verbose_name='Curso')),
                ('student', models.ForeignKey(limit_choices_to={'groups__name': 'estudiante'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Estudiante')),
            ],
            options={
                'verbose_name': 'Nota',
                'verbose_name_plural': 'Notas',
            },
        ),
    ]