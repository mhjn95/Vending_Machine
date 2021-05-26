# Generated by Django 3.1.7 on 2021-05-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210516_0216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_no', models.IntegerField(default=1)),
                ('coke', models.IntegerField(default=50)),
                ('pepsi', models.IntegerField(default=50)),
                ('soda', models.IntegerField(default=50)),
                ('one', models.IntegerField(default=50)),
                ('five', models.IntegerField(default=50)),
                ('ten', models.IntegerField(default=50)),
                ('twentyfive', models.IntegerField(default=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Items',
        ),
    ]