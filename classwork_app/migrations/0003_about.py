# Generated by Django 2.2.5 on 2020-03-16 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classwork_app', '0002_auto_20200313_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]