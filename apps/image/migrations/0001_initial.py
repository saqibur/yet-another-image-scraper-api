# Generated by Django 4.0.5 on 2022-06-19 22:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_column='uuid', default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='modified_at', verbose_name='Modified at')),
                ('image', models.ImageField(db_column='image', upload_to='scraped_images/', verbose_name='Image')),
                ('scraped_from', models.URLField(db_column='scraped_from', verbose_name='URL scraped from')),
                ('metadata', models.JSONField(blank=True, db_column='metadata', null=True, verbose_name='Image metadata')),
            ],
            options={
                'verbose_name': 'Scraped image',
                'verbose_name_plural': 'Scraped images',
                'db_table': 'scraped_image',
                'ordering': ['-created_at'],
            },
        ),
    ]
