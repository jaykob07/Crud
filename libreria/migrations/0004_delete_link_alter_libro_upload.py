# Generated by Django 4.2.7 on 2023-11-12 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_libro_upload'),
    ]

    operations = [
        migrations.DeleteModel(
            name='link',
        ),
        migrations.AlterField(
            model_name='libro',
            name='upload',
            field=models.FileField(upload_to='archivos_pdf'),
        ),
    ]
