# Generated by Django 2.2.3 on 2019-07-31 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='noidajobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('compnay', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
            ],
        ),
    ]