# Generated by Django 2.1.2 on 2018-10-05 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('holaserver', '0009_auto_20181005_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetailstable',
            name='carId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='carstatustable',
            name='carId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='holaserver.CarDetailsTable', verbose_name='carId'),
        ),
    ]