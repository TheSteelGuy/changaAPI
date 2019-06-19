# Generated by Django 2.2.1 on 2019-06-19 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chamaa', '0003_chamaa_contribution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamaa',
            name='account_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='chamaa',
            name='contribution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contributions.Contribution'),
        ),
    ]
