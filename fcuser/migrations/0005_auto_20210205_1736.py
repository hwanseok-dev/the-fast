# Generated by Django 3.1.6 on 2021-02-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0004_auto_20210205_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='비밀번호'),
        ),
    ]
