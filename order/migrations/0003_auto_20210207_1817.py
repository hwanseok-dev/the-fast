# Generated by Django 3.1.6 on 2021-02-07 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210207_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('대기중', '대기중'), ('결제대기중', '결제대기중'), ('결제완료', '결제완료'), ('환불', '환불')], default='대기중', max_length=64, verbose_name='상태'),
        ),
    ]
