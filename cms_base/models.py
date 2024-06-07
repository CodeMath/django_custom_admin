from django.db import models


class Attachment(models.Model):
    class Meta:
        db_table = 'attachment'
        verbose_name = "첨부파일"
        verbose_name_plural = "첨부파일"

    url = models.FileField(upload_to='attachments/%Y/%m/%d', verbose_name='첨부파일', max_length=255)

    def __str__(self):
        return self.url.name