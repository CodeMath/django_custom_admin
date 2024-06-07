from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime


class GallerySession(models.Model):
    class Meta:
        db_table = 'gallery_session'
        verbose_name = '갤러리 - 회차 정보'
        verbose_name_plural = '갤러리 - 회차 정보'

    year = models.IntegerField(verbose_name="년도", default=datetime.date.today().year)
    session = models.IntegerField(verbose_name="회차", default=1, help_text="자동으로 숫자가 올라갑니다.")

    def __str__(self):
        return f"[{self.year}] {self.session} 회차"


@receiver(pre_save, sender=GallerySession)
def set_session_number(sender, instance, **kwargs):
    if instance.pk is None:
        # 새로운 인스턴스일 때만 처리
        latest_session = GallerySession.objects.filter(year=instance.year).order_by('-session').first()
        if latest_session:
            instance.session = latest_session.session + 1
        else:
            # 해당 년도에 해당하는 첫 번째 세션
            instance.session = 1


class Gallery(models.Model):
    class Meta:
        db_table = 'gallery'
        verbose_name = '갤러리'
        verbose_name_plural = '갤러리'
    CATEGORY_CHOICES = (
        ('event', '이벤트'),
        ('market', '마켓'),
        ('etc', '기타'),
    )

    session = models.ForeignKey(GallerySession, on_delete=models.SET_NULL, verbose_name="회차")
    status = models.BooleanField(default=True, verbose_name="공개 여부")
    poster = models.ImageField(verbose_name="메인 이미지", upload_to='gallery', max_length=255)
    category = models.CharField(verbose_name='카테고리', choices=CATEGORY_CHOICES, max_length=30)
    description = models.CharField(verbose_name="갤러리 1줄 설명", max_length=255)
    view_count = models.PositiveIntegerField(verbose_name="조회수", default=0)
    created_at = models.DateTimeField(verbose_name="등록일", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일", auto_now=True)

    def __str__(self):
        return f"{self.category}/{self.session} - 갤러리"


def gallery_image_path(instance, filename):
    return f'gallery/{instance.gallery.category}/{datetime.datetime.now().strftime("%Y/%m/%d")}/{filename}'


class GalleryAttachment(models.Model):
    class Meta:
        db_table = 'gallery_attachment'
        verbose_name = '갤러리 리스트'
        verbose_name_plural = '갤러리 리스트'
        unique_together = ('gallery', 'ordering')  # 이 라인을 추가

    gallery = models.ForeignKey(Gallery, verbose_name="갤러리", on_delete=models.CASCADE)
    url = models.ImageField(verbose_name="이미지", max_length=255, upload_to=gallery_image_path)
    ordering = models.PositiveIntegerField(verbose_name="순서", default=1)

    def __str__(self):
        return f"[{self.gallery.get_category_display()}] {self.url.name} - {self.ordering}"

