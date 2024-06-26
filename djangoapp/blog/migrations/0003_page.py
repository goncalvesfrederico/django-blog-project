# Generated by Django 5.0.6 on 2024-06-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_alter_tag_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(blank=True, default='', max_length=90, null=True, unique=True)),
                ('is_published', models.BooleanField(default=False, help_text='This field needs to be checked for the page to be published.')),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
    ]
