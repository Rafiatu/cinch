# Generated by Django 3.1.2 on 2020-11-24 12:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='avatar_url',
            field=models.URLField(default='http://res.cloudinary.com/cinchapi/image/upload/v1605789407/re1ouirm2sujfwz5afgx.png', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='country_code',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, null=True)),
                ('url', models.URLField()),
                ('cover_art_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.artist')),
            ],
        ),
    ]
