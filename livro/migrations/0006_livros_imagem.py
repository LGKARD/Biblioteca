# Generated by Django 4.2.2 on 2023-07-27 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0005_livros_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='imagem',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]