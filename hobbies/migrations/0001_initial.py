# Generated by Django 2.2.6 on 2020-01-02 00:18

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Illstrations',
            fields=[
                ('profile_pic', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='static/images/profiles')),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'illstrations',
                'managed': True,
            },
        ),
    ]