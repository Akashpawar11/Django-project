# Generated by Django 3.2.13 on 2022-07-09 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fees_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=100)),
                ('duration', models.IntegerField(default=0)),
                ('fees', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('Entry_id', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('fees_plan', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='memb_app.fees_plan')),
                ('role', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='memb_app.role')),
            ],
        ),
    ]
