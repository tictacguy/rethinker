# Generated by Django 5.1.7 on 2025-03-26 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('context_embedding', models.JSONField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
