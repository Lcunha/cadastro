# Generated by Django 2.0.8 on 2018-08-20 22:49

import campanha.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campanha', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('sigla', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Eleitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('telefone', models.IntegerField(max_length=15)),
                ('origem', models.CharField(max_length=80)),
                ('envio', models.BooleanField(default=False)),
                ('cidade', models.ForeignKey(on_delete=models.SET(campanha.models.get_cidade_brasilia), related_name='eleitores', to='campanha.Cidade')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 20, 22, 49, 15, 574552, tzinfo=utc)),
        ),
    ]
