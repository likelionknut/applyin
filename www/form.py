from django import forms
from django_summernote import fields as summer_fields
from .models import *


class ApplicationForm(forms.ModelForm):
    # content = summer_fields.SummernoteTextFormField(error_messages={'required': '데이터를 입력해주세요', })

    class Meta:
        model = Application
        fields = ['name', 'email', 'phone', 'address', 'prev_company', 'prev_date_join', 'prev_date_leave', 'prev_department', 'prev_location', 'prev_position']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "이름"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "이메일"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "연락처"}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "주소"}),
            'prev_company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "회사명"}),
            'prev_department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "부서명"}),
            'prev_date_join': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "입사일"}),
            'prev_date_leave': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "퇴사일"}),
            'prev_position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "직급/직책"}),
            'prev_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "지역"}),
        }
        labels = {
            'name': '',
            'email': '',
            'phone': '',
            'address': '',
            'prev_company': '',
            'prev_department': '',
            'prev_date_join': '',
            'prev_date_leave': '',
            'prev_position': '',
            'prev_location': '',
        }
