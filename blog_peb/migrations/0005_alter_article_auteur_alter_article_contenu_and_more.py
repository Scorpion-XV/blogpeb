# Generated by Django 4.2.1 on 2023-05-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_peb', '0004_alter_article_auteur_alter_article_contenu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='auteur',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='contenu',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='miniature',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='resume',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='titre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='prenom',
            field=models.CharField(max_length=100),
        ),
    ]
