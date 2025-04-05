# Generated by Django 5.1 on 2025-04-04 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_id', models.CharField(max_length=24)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('vat_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('default_qty', models.PositiveIntegerField()),
                ('currency_id', models.CharField(max_length=4)),
                ('is_tax_exempt', models.IntegerField(choices=[(0, 'False'), (1, 'True')], default=0)),
                ('note', models.CharField(max_length=255)),
            ],
        ),
    ]
