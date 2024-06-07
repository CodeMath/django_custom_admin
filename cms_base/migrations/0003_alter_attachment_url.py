# Generated by Django 5.0.4 on 2024-05-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cms_base", "0002_alter_attachment_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attachment",
            name="url",
            field=models.FileField(
                max_length=255, upload_to="attachments/%Y/%m/%d", verbose_name="첨부파일"
            ),
        ),
    ]