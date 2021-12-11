from django import forms
from .models import Department, Employee,Salary,Leave,Job
from .models import GENDER_CHOICE


class EmployeeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Employee
        exclude = ['user']
        fields = ['name','image','phone','gender','department','aadhar_card_no']


        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'department':forms.Select(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),     
            'aadhar_card_no':forms.TextInput(attrs={'class':'form-control'}),     
        }



class LeaveUserApply(forms.ModelForm):

    class Meta:
        model = Leave
        fields = ['leave_from','leave_till','leave_reason']

        widgets = {
            'leave_from':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'leave_till':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'leave_reason':forms.TextInput(attrs={'class':'form-control','placeholder':'Reason For Leave'}),
        }


class JobAddForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['position','company_name','exp_in_company']

        widgets = {
            'position':forms.TextInput(attrs={'class':'form-control','placeholder':'Position/Job Role'}),
            'company_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Company Name'}),
            'exp_in_company':forms.TextInput(attrs={'class':'form-control','placeholder':'Exp in months'}),
        
        }


class JobUpdateForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['position','company_name','exp_in_company']

        widgets = {
            'position':forms.TextInput(attrs={'class':'form-control'}),
            'company_name':forms.TextInput(attrs={'class':'form-control'}),
            'exp_in_company':forms.TextInput(attrs={'class':'form-control'}),
        
        }
