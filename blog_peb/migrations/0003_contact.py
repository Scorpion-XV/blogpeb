# Generated by Django 4.2.1 on 2023-05-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_peb', '0002_alter_article_miniature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('message', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
