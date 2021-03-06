# Generated by Django 3.2.8 on 2021-11-03 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workout',
            options={'ordering': ['race_type']},
        ),
        migrations.RemoveField(
            model_name='workout',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='goal',
        ),
        migrations.AlterField(
            model_name='workout',
            name='race_type',
            field=models.CharField(choices=[('800m', '800m'), ('half-marathon', 'Half Marathon'), ('mile', '1600m'), ('5k', '5k'), ('marathon', 'Marathon')], default='5k', max_length=100),
        ),
    ]
