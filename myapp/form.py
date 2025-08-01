from django import forms
from .models import teachers,students,joinclass



class teacherform(forms.ModelForm):
    class Meta:
        model = teachers
        fields = '__all__' 

class studentform(forms.ModelForm):
    class Meta:
        model=students
        fields= '__all__'

class joinform(forms.ModelForm):
    class Meta:
        model=joinclass
        fields='__all__'