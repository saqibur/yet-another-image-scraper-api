# Generated by Django 4.0.5 on 2022-06-20 02:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_column='uuid', default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='modified_at', verbose_name='Modified at')),
                ('size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], db_column='size', max_length=10, verbose_name='Image size')),
                ('image', models.ImageField(db_column='image', upload_to='scraped_images/', verbose_name='Image')),
                ('scraped_image', models.ForeignKey(db_column='scraped_image', on_delete=django.db.models.deletion.CASCADE, related_name='image_variant', to='image.scrapedimage', verbose_name='Scraped image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]