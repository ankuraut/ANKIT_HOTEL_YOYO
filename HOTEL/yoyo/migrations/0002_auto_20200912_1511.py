# Generated by Django 3.1.1 on 2020-09-12 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoyo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='meals',
            field=models.CharField(choices=[('BKFST', 'BREAKFAST'), ('DIN', 'DINNER'), ('NA', 'NOTHING'), ('LUC', 'LUNCH')], default='none', max_length=5),
        ),
        migrations.AlterField(
            model_name='room',
            name='types',
            field=models.CharField(choices=[('ACC', 'AC'), ('QUE', 'QUEEN'), ('NOR', 'NORMAL'), ('NAC', 'NON-AC'), ('KIG', 'KING'), ('XYX', 'COUPLE-FRIENDLY')], max_length=3),
        ),
    ]