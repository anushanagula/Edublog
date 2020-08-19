# Generated by Django 3.0.3 on 2020-07-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='contact_facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='contact_linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='image',
            field=models.ImageField(blank=True, default='accounts/img/default_profile.png', upload_to='../accounts/img'),
        ),
    ]
