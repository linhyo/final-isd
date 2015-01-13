from django import forms
from vietskill.models import StaffProfile, Recruitment, Assessment


class ProfileForm(forms.ModelForm):

    class Meta:
        model = StaffProfile
        fields = ('name', 'birthday', 'sex', 'position', 'email', 'address', 'phone_number', 'picture')


class RecruitmentForm(forms.ModelForm):

    class Meta:
        model = Recruitment
        fields = ('title', 'content', 'release_date', 'expiry_date')


class AssessmentForm(forms.ModelForm):

    class Meta:
        model = Assessment
        fields = ('staff', 'content', 'assess_point', 'date')