from django.db import models
from cms_base.models import Attachment


class Event(models.Model):
    class Meta:
        db_table = 'event'
        verbose_name = '이벤트'
        verbose_name_plural = '이벤트'

    status = models.BooleanField(verbose_name='공개', default=True, unique=True, help_text="1개만 공개됩니다.")
    start = models.DateField(verbose_name="시작일")
    end = models.DateField(verbose_name="종료일")
    poster = models.ImageField(verbose_name="메인 이미지", upload_to='beer', max_length=255)
    title = models.CharField(verbose_name="제목", max_length=200, help_text="제목 노출")
    content = models.TextField(verbose_name="내용")
    description = models.CharField(verbose_name="일정 설명", max_length=255, help_text="1줄 소개")

    def __str__(self):
        return f"[이벤트] {self.title} | {self.start} ~ {self.end}"


class EventAttachment(models.Model):
    class Meta:
        db_table = 'event_attachment'
        verbose_name = '이벤트 첨부 파일'
        verbose_name_plural = '이벤트 첨부 파일'

    event = models.ForeignKey(Event, verbose_name="일정", on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment, verbose_name="첨부파일", on_delete=models.CASCADE)

    def __str__(self):
        return f"[첨부 파일] {self.event} - {self.attachment}"


class Market(models.Model):
    class Meta:
        db_table = 'market_schedule'
        verbose_name = '마켓 일정 관리'
        verbose_name_plural = '마켓 일정 관리'

    status = models.BooleanField(verbose_name='공개', default=True, unique=True, help_text="1개만 공개")

    start = models.DateField(verbose_name="개장 시작일", help_text="도르프 청년 마켓 개장일")
    end = models.DateField(verbose_name="개장 종료일", help_text="도르프 청년 마켓 종료일")

    start_time = models.TimeField(verbose_name="개장 시작 시간",)
    end_time = models.TimeField(verbose_name="개장 종료 시간",)

    poster = models.ImageField(verbose_name="대표 이미지", upload_to='dorf', max_length=255)
    title = models.CharField(verbose_name="제목", max_length=200)
    content = models.TextField(verbose_name="내용")
    link = models.URLField(verbose_name="링크", max_length=255)
    description = models.CharField(verbose_name="일정 설명", max_length=255, help_text="1줄 소개")

    def __str__(self):
        return f"[마켓] {self.title} | {self.start} ~ {self.end}"


class MarketAttachment(models.Model):
    class Meta:
        db_table = 'market_attachment'
        verbose_name = '마켓 첨부 파일'
        verbose_name_plural = '마켓 첨부 파일'

    market = models.ForeignKey(Market, verbose_name="마켓", on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment, verbose_name="첨부파일", on_delete=models.CASCADE)

    def __str__(self):
        return f"[첨부 파일] {self.market} - {self.attachment}"