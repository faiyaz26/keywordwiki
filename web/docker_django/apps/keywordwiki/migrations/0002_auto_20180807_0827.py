# Generated by Django 2.1 on 2018-08-07 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keywordwiki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Category title')),
                ('description', models.TextField(blank=True, verbose_name='Category description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AlterField(
            model_name='keyword',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='keyword',
            name='categories',
            field=models.ManyToManyField(to='keywordwiki.Category'),
        ),
    ]