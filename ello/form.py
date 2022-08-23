# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from django.db import transaction
# # from ello.models import PA
# from ello.models import User
# # from .paytm import Checksum
# from django.shortcuts import redirect, render
# # import PaytmChecksum
# import json
# # MERCHANT_KEY = str("XRSzvi52564295581047")

# class PASignUpForm(UserCreationForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     phone_number = forms.CharField(required=True)
#     state = forms.CharField(required=True)
#     email= forms.CharField(required=True)

#     class Meta(UserCreationForm.Meta):
#         model = User
    
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_pastudent = True
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         user.save()
#         pa = PA.objects.create(user=user)
#         pa.phone_number=self.cleaned_data.get('phone_number')
#         pa.email=self.cleaned_data.get('email')
#         pa.state=self.cleaned_data.get('state')
#         pa.save()
#         return user