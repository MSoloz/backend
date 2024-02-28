# Generated by Django 4.2.3 on 2024-02-19 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('required', models.CharField(max_length=255)),
                ('pdf', models.FileField(upload_to='pdfs/')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel.channel')),
            ],
            options={
                'db_table': 'conditions',
            },
        ),
    ]
