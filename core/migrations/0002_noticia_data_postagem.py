# Generated by Django 2.0.6 on 2018-06-04 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='data_postagem',
            field=models.DateTimeField(null=True),
        ),
    ]
