from django.db import models
from django.contrib.postgres.fields import ArrayField

from cms_base.models import Attachment


class Information(models.Model):
    class Meta:
        db_table = 'information'
        verbose_name = "문의 정보"
        verbose_name_plural = "문의 정보"
    phone = models.CharField(verbose_name="문의 전호 번호", max_length=100, help_text="070-000-0000")
    email = models.EmailField(verbose_name="대표 이메일", max_length=100, help_text="055-000-0000")


class Notice(models.Model):
    class Meta:
        db_table = 'notice'
        verbose_name = "공지사항"
        verbose_name_plural = "공지사항"

    title = models.CharField(verbose_name="제목", max_length=100)
    content = models.TextField(verbose_name="내용")
    view_count = models.IntegerField(verbose_name="조회수", default=0)
    created_at = models.DateTimeField(verbose_name="등록일", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일", auto_now=True)


    def __str__(self):
        return f"[공지사항] {self.title}"


class NoticeAttachment(models.Model):
    class Meta:
        db_table = 'notice_attachment'
        verbose_name = '공지사항 첨부 파일'
        verbose_name_plural = '공지사항 첨부 파일'

    notice = models.ForeignKey(Notice, verbose_name="공지사항", on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment, verbose_name="첨부파일", on_delete=models.CASCADE)

    def __str__(self):
        return f"[첨부 파일] {self.notice} - {self.attachment}"


class Question(models.Model):
    class Meta:
        db_table = 'question'
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

    title = models.CharField(verbose_name="제목", max_length=100)
    content = models.TextField(verbose_name="내용")
    view_count = models.IntegerField(verbose_name="조회수", default=0)
    created_at = models.DateTimeField(verbose_name="등록일", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일", auto_now=True)

    def __str__(self):
        return f"{self.title}"


class QuestionAttachment(models.Model):
    class Meta:
        db_table = 'question_attachment'
        verbose_name = 'FAQ 첨부 파일'
        verbose_name_plural = 'FAQ 첨부 파일'

    question = models.ForeignKey(Question, verbose_name="문의사항", on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment, verbose_name="첨부파일", on_delete=models.CASCADE)

    def __str__(self):
        return f"[첨부 파일] {self.question} - {self.attachment}"



class Facility(models.Model):
    class Meta:
        db_table = 'facility'
        verbose_name = '시설 안내'
        verbose_name_plural = '시설 안내'

    CATEGORY_TYPES = (
        ('reserve', '예약 필수'),
        ('meeting', '회의'),
        ('seminar', '세미나'),
        ('laptop', '노트북'),
        ('food', '음식물 반입'),
        ('drink', '마실 것만 가능'),
    )

    category = ArrayField(
        models.CharField(verbose_name="카테고리", max_length=10, choices=CATEGORY_TYPES),
        size=6, default=list, verbose_name="카테고리"
    )
    title = models.CharField(verbose_name="시설 명", max_length=255)
    address = models.CharField(verbose_name="위치", max_length=255)

    poster = models.ImageField(verbose_name="대표 이미지", upload_to='facility')
    content = models.TextField(verbose_name="내용", blank=True, null=True)

    open_time = models.TimeField(verbose_name="오픈 시간")
    close_time = models.TimeField(verbose_name="마감 시간")

    def __str__(self):
        return f"[시설] {self.title}"


class FacilityTag(models.Model):
    class Meta:
        db_table = 'facility_tag'
        verbose_name = '부대시설 태그'
        verbose_name_plural = '부대시설 태그'

    facility = models.ForeignKey(Facility, verbose_name="부대시설", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="태그", max_length=30, help_text='태그는 30자 제한')

    def __str__(self):
        return f"#{self.name}"