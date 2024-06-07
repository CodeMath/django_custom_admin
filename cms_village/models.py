from django.db import models
from django.contrib.auth.models import User, Group
from cms_base.models import Attachment
from django.contrib.contenttypes.fields import GenericRelation
from phonenumber_field.modelfields import PhoneNumberField




class AccommodationCategory(models.Model):
    class Meta:
        db_table = 'accommodation_category'
        verbose_name = '숙소 카테고리'
        verbose_name_plural = '숙소 카테고리'
    name = models.CharField(verbose_name="카테고리", max_length=10, unique=True)

    def __str__(self):
        return self.name


class Accommodation(models.Model):
    class Meta:
        db_table = 'accommodation'
        verbose_name = '숙소 관리'
        verbose_name_plural = '숙소 관리'

    category = models.ForeignKey(AccommodationCategory, on_delete=models.CASCADE,  verbose_name="카테고리")
    status = models.BooleanField(verbose_name="공개여부", default=True)
    name_kr = models.CharField(verbose_name="숙소 한글 명", max_length=250, unique=True)
    name_en = models.CharField(verbose_name="숙소 영문 명", max_length=250, unique=True)
    poster = models.ImageField(verbose_name="메인 이미지", upload_to='accommodation/', help_text="썸네일 이미지 업로드 필수")
    address = models.CharField(verbose_name="주소", max_length=250)
    phone = PhoneNumberField(verbose_name="전화번호", help_text="자동으로 +82 이 입력됩니다.")
    reservation_link = models.URLField(verbose_name="예약 링크", null=True, blank=True)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(verbose_name="등록일", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일", auto_now=True)
    attachment = GenericRelation(Attachment)

    def __str__(self):
        return f"[{self.category}] {self.name_kr}"


class AccommodationTag(models.Model):
    class Meta:
        db_table = 'accommodation_tag'
        verbose_name = '숙소 태그'
        verbose_name_plural = '숙소 태그'

    accommodation = models.ForeignKey(Accommodation, verbose_name="숙소", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="태그", max_length=30, unique=True)

    def __str__(self):
        return f"#{self.name}"


