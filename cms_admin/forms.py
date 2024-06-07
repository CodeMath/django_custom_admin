from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from cms_admin.models import *


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'  # 필요한 필드만 명시할 수 있습니다.


class AffiliateCompanyForm(forms.ModelForm):
    class Meta:
        model = AffiliateCompany
        fields = '__all__'


class FacilityAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FacilityAdminForm, self).__init__(*args, **kwargs)
        self.fields['category'].label = '카테고리'
        self.fields['category'].help_text = "카테고리: 1개~3개 까지 선택 가능"

    category = forms.MultipleChoiceField(
        choices=Facility.CATEGORY_TYPES,
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Facility
        fields = '__all__'

    def clean_category(self):
        return self.cleaned_data['category']


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
