# Generated by Django 3.1.6 on 2021-02-06 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcuser',
            name='level',
            field=models.CharField(choices=[('admin', 'admin'), ('admin', 'user')], default='user', max_length=8, verbose_name='등급'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fcuser',
            name='password',
            field=models.CharField(max_length=256, verbose_name='비밀번호'),
        ),
    ]
