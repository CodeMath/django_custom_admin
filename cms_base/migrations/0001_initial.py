# Generated by Django 5.0.4 on 2024-04-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attachment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.FileField(upload_to="attachments", verbose_name="첨부파일")),
            ],
            options={
                "verbose_name": "첨부파일",
                "verbose_name_plural": "첨부파일",
                "db_table": "attachment",
            },
        ),
    ]