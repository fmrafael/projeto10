# Generated by Django 4.0 on 2022-01-03 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableAffiliate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_affiliate', models.CharField(max_length=200)),
                ('photo_affiliate', models.ImageField(blank=True, upload_to='images')),
                ('name_affiliate', models.TextField()),
                ('website_affiliate', models.TextField()),
                ('commission_affiliate', models.CharField(max_length=200)),
                ('description_affiliate', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo_title', models.ImageField(blank=True, upload_to='images/')),
                ('subheading1', models.CharField(blank=True, max_length=255)),
                ('body1', models.TextField(blank=True)),
                ('photo_body1', models.ImageField(blank=True, upload_to='images/')),
                ('subheading2', models.CharField(blank=True, max_length=255)),
                ('body2', models.TextField(blank=True)),
                ('photo_body2', models.ImageField(blank=True, upload_to='images/')),
                ('subheading3', models.CharField(blank=True, max_length=255)),
                ('body3', models.TextField(blank=True)),
                ('conclusion', models.TextField(blank=True)),
                ('post_links', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]