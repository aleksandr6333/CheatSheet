# Generated by Django 4.1.1 on 2022-09-20 03:46

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_subtitles'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='rtfbody',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='subtitles',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Подзаголовок'),
        ),
    ]
