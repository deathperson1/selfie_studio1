# Generated by Django 3.1.5 on 2021-05-20 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='Name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='products',
            name='detail',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='products',
            name='heroimage',
            field=models.ImageField(default='there is no image', upload_to='products'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
