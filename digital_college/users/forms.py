from django.forms import ModelForm
from .models import Registered_User, Registered_College
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.core import validators


class User_Registration_Form(ModelForm):
    ROLE_CHOICES = (
        ('F', 'Faculty'),
        ('S', 'Student')
    )

    college_id = forms.ModelChoiceField(queryset=Registered_College.objects.all())
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0), ])
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'container'}))
    class Meta:
        model = Registered_User
        fields = ['first_name', 'last_name', 'email', 'role', 'college_id', 'activation_key', 'botcatcher', ]
        # fields = '__all__'


class College_Registration_Form(ModelForm):
    STATE_CHOICES=(
        ('AP', 'Andhra Pradesh'),
        ('AC', 'Arunchal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CH', 'Chattisgarh'),
        ('GO', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KN', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharastra'),
        ('MN', 'Manipur'),
        ('MZ', 'Mizoram'),
        ('MG', 'Meghalaya'),
        ('NG', 'Nagaland'),
        ('OR', 'Orissa'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangana'),
        ('TP', 'Tripura'),
        ('UL', 'Uttaranchal'),
        ('UP', 'Uttar Pradesh'),
        ('WB', 'West Bengal')
    )
    email = forms.CharField(widget=forms.EmailInput)
    State = forms.ChoiceField(choices=STATE_CHOICES)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0), ])
    class Meta:
        model = Registered_College
        fields = ['Name_Of_College', 'email', 'College_Registration_Number', 'City', 'State', 'botcatcher', ]
    )
    email = forms.CharField(widget=forms.EmailInput)
    State = forms.ChoiceField(choices=STATE_CHOICES)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)],)
    class Meta:
        model = Registered_College
        fields = ['Name_Of_College', 'email', 'College_Registration_Number', 'City', 'State', ]

