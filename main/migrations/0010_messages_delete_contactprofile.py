# Generated by Django 4.0.1 on 2022-02-02 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_portfolio_options_portfolio_importance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='Full Name*')),
                ('email', models.EmailField(max_length=254, verbose_name='Email*')),
                ('message', models.TextField(verbose_name='Message*')),
            ],
            options={
                'verbose_name': 'Messages',
                'verbose_name_plural': 'Messages',
                'ordering': ['timestamp'],
            },
        ),
        migrations.DeleteModel(
            name='ContactProfile',
        ),
    ]
